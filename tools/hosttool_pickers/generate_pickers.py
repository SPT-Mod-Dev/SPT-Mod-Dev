"""Host tool picker generator: rebuilds the focus picker and national-spirit picker.

Run it after any change to focus trees or national spirits:
    python generate_pickers.py --mod "<mod folder>" [--game "<Hearts of Iron IV folder>"]
It rewrites these four files in the mod folder:
    common/decisions/host_tool_focus_picker.txt
    common/decisions/host_tool_spirit_picker.txt
    localisation/english/ht_focus_picker_l_english.yml
    localisation/english/ht_spirit_picker_l_english.yml
"""
import argparse, os, sys, glob, re, shutil, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdxparse import read_text, parse, inner_block_text

ap = argparse.ArgumentParser(description='Rebuild the host tool focus and national-spirit pickers.')
ap.add_argument('--mod', required=True, help='the mod folder (the one with descriptor.mod)')
ap.add_argument('--game', default=r'C:\Program Files (x86)\Steam\steamapps\common\Hearts of Iron IV',
                help='the Hearts of Iron IV folder (default: the standard Steam location)')
args = ap.parse_args()
MOD = os.path.abspath(args.mod)
VAN = os.path.abspath(args.game)
if not os.path.isfile(os.path.join(MOD, 'descriptor.mod')):
    sys.exit(f'No descriptor.mod in {MOD} - point --mod at the mod folder.')
if not os.path.isdir(os.path.join(VAN, 'common', 'national_focus')):
    sys.exit(f'Hearts of Iron IV not found at {VAN} - pass --game "<folder with hoi4.exe>".')
OUT = tempfile.mkdtemp(prefix='ht_pickers_')

# Load set per folder, as the game builds it: a replace_path'd folder loads the mod's files only;
# otherwise vanilla loads too, with a mod file shadowing the vanilla file of the same name.
REPLACED = set()
with open(os.path.join(MOD, 'descriptor.mod'), 'rb') as fh:
    for m in re.finditer(r'(?m)^[ \t]*replace_path[ \t]*=[ \t]*"([^"]+)"', fh.read().decode('latin-1')):
        REPLACED.add(m.group(1).strip('/').lower())

def pool(sub):
    mod_files = glob.glob(os.path.join(MOD, *sub.split('/'), '*.txt'))
    if sub.lower() in REPLACED:
        return sorted(mod_files)
    files = {os.path.basename(p).lower(): p
             for p in glob.glob(os.path.join(VAN, *sub.split('/'), '*.txt'))}
    for p in mod_files:
        files[os.path.basename(p).lower()] = p
    return [files[k] for k in sorted(files)]

# Hidden (non-spirit) AI-control ideas; each is offered only if the mod defines it.
CURATED_HIDDEN = ['Spies_no_capture', 'ai_annex', 'ai_tradelaw', 'ai_war',
                  'no_faction', 'novols', 'noresistance', 'ai_conscription_laws']

report = []
def rep(msg):
    report.append(msg)
    print(msg)

# ---------- scan focus pool ----------
def is_hidden(fnode):
    # A focus can carry more than one allow_branch (brazil.txt BRA_invite_foreign_companies);
    # any of them being always = no hides it.
    for ab in fnode.find_all('allow_branch'):
        if ab.children is not None and any(
                c.key and c.key.lower() == 'always' and c.value and c.value.lower() == 'no'
                for c in ab.children):
            return True
    return False

trees = {}        # tree_id -> set(focus ids in tree, incl shared refs)
focus_info = {}   # fid -> dict(hidden, avail_text or None, file)
focus_trees = {}  # fid -> set(tree ids)
add_map = {}      # idea -> set(tree ids granting it via non-hidden focus)
dups = []

MACRO_DEF = re.compile(r'(?m)^[ \t]*@([A-Za-z0-9_]+)[ \t]*=[ \t]*(-?[0-9.]+)')
MACRO_USE = re.compile(r'@([A-Za-z0-9_]+)')

nf_files = pool('common/national_focus')
for path in nf_files:
    text = read_text(path)
    root = parse(text)
    # @macros are file-local: inline the source file's numeric values into anything pasted
    # out of it; a gate that still holds an unresolved macro is dropped later.
    macros = dict(MACRO_DEF.findall(text))
    def reg_focus(fnode, tree_id):
        fid = fnode.val('id')
        if not fid:
            return
        if fid in focus_info and focus_info[fid]['file'] != path:
            dups.append((fid, focus_info[fid]['file'], path))
        av = fnode.find('available')
        avail_text = None
        if av is not None and av.children is not None:
            t = inner_block_text(text, av)
            if t.strip():
                avail_text = MACRO_USE.sub(lambda m: macros.get(m.group(1), m.group(0)),
                                           t.rstrip('\r\n').replace('\r\n', '\n'))
        focus_info[fid] = {'hidden': is_hidden(fnode), 'avail': avail_text, 'file': path,
                           'text': fnode.val('text')}
        if tree_id:
            focus_trees.setdefault(fid, set()).add(tree_id)
        # idea grants
        if not focus_info[fid]['hidden']:
            # joint focuses grant through their originator/member reward blocks
            for rk in ('completion_reward', 'completion_reward_joint_originator',
                       'completion_reward_joint_member'):
                cr = fnode.find(rk)
                if cr is None:
                    continue
                def walk(n):
                    for c in (n.children or []):
                        if c.key and c.key.lower() == 'add_ideas':
                            if c.value is not None:
                                add_map.setdefault(c.value, set()).add(fid)
                            elif c.children is not None:
                                for g in c.children:
                                    if g.key is None and g.value:
                                        add_map.setdefault(g.value, set()).add(fid)
                        if c.children is not None:
                            walk(c)
                walk(cr)
    for top in root.children:
        k = (top.key or '').lower()
        if k == 'focus_tree' and top.children is not None:
            tid = top.val('id')
            if not tid:
                continue
            trees.setdefault(tid, set())
            for c in top.children:
                ck = (c.key or '').lower()
                if ck == 'focus' and c.children is not None:
                    trees[tid].add(c.val('id'))
                    reg_focus(c, tid)
                elif ck in ('shared_focus', 'joint_focus') and c.value is not None:
                    trees[tid].add(c.value)
        elif k in ('shared_focus', 'joint_focus') and top.children is not None:
            reg_focus(top, None)

# attach shared focuses to referencing trees (incl. chains: shared focuses whose
# prerequisite/relative parents are shared roots referenced by trees). HOI4 loads a
# shared root and its whole shared subtree; tree membership via referenced root only
# covers the root. Build shared child->root closure via relative_position_id/prerequisite.
shared_children = {}  # fid -> set(parent fids) among shared defs
for path in nf_files:
    text = read_text(path)
    root = parse(text)
    for top in root.children:
        if (top.key or '').lower() in ('shared_focus', 'joint_focus') and top.children is not None:
            fid = top.val('id')
            parents = set()
            for c in top.children:
                ck = (c.key or '').lower()
                if ck == 'relative_position_id' and c.value:
                    parents.add(c.value)
                elif ck == 'prerequisite' and c.children is not None:
                    for g in c.children:
                        if g.key and g.key.lower() == 'focus' and g.value:
                            parents.add(g.value)
            shared_children[fid] = parents

changed = True
while changed:
    changed = False
    for fid, parents in shared_children.items():
        for p in parents:
            for tid, members in trees.items():
                if p in members and fid not in members:
                    members.add(fid)
                    changed = True
for tid, members in trees.items():
    for fid in members:
        if fid in focus_info:
            focus_trees.setdefault(fid, set()).add(tid)

# ---------- focus decisions ----------
included, skipped_hidden, skipped_orphan = [], [], []
for fid in sorted(focus_info):
    if focus_info[fid]['hidden']:
        skipped_hidden.append(fid)
        continue
    ts = sorted(focus_trees.get(fid, ()))
    if not ts:
        skipped_orphan.append(fid)
        continue
    included.append((fid, ts))

rep(f'focus pool: {len(focus_info)} defs in {len(nf_files)} files, {len(trees)} trees')
rep(f'focus picker: {len(included)} decisions; skipped hidden={len(skipped_hidden)} orphan-shared={len(skipped_orphan)}')
rep(f'duplicate focus ids across files: {len(dups)} {dups[:5]}')
if skipped_orphan:
    rep(f'  orphan sample: {skipped_orphan[:20]}')

gate_dropped = []

# Country tags the game knows (the country_tags load set) + dynamic tags.
known_tags = {f'D{i:02d}' for i in range(1, 100)}
for p in pool('common/country_tags'):
    known_tags |= set(re.findall(r'(?m)^[ \t]*([A-Z][A-Z0-9]{2})[ \t]*=', re.sub(r'#[^\n]*', '', read_text(p))))
NOT_TAGS = {'AND', 'NOT', 'NOR', 'XOR', 'ALL', 'ANY', 'NAND'}
TAG_SCOPE = re.compile(r'(?<![A-Za-z0-9_.:@])([A-Z][A-Z0-9]{2})\s*=\s*\{')
TAG_VALUE = re.compile(r'=\s*([A-Z][A-Z0-9]{2})(?![A-Za-z0-9_])')

# Scripted triggers (the scripted_triggers load set).
scripted_triggers = {}
for p in pool('common/scripted_triggers'):
    t = read_text(p)
    for top in parse(t).children:
        if top.key and top.children is not None:
            scripted_triggers[top.key] = inner_block_text(t, top)
TRIGGER_CALL = re.compile(r'(?<![A-Za-z0-9_.:@])([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?:yes|no)\b')

# Every idea of every category (the ideas load set).
all_ideas = set()
for p in pool('common/ideas'):
    for top in parse(read_text(p)).children:
        if (top.key or '').lower() == 'ideas' and top.children is not None:
            for cat in top.children:
                for idea in (cat.children or []):
                    if idea.key:
                        all_ideas.add(idea.key)
HAS_IDEA = re.compile(r'(?<![A-Za-z0-9_])has_idea\s*=\s*([A-Za-z0-9_]+)')

def _strip(text):
    return re.sub(r'#[^\n]*', '', text)

def _uses_root_or_top_prev(s):
    if re.search(r'(?<![A-Za-z0-9_.:@])ROOT(?![A-Za-z0-9_])', s, re.I):
        return True
    depth = 0
    for m in re.finditer(r'\{|\}|(?<![A-Za-z0-9_.:@])PREV(?![A-Za-z0-9_])', s, re.I):
        tok = m.group(0)
        if tok == '{': depth += 1
        elif tok == '}': depth -= 1
        elif depth == 0: return True
    return False

def _unknown_tag(s):
    for rx in (TAG_SCOPE, TAG_VALUE):
        for tg in rx.findall(s):
            if tg not in known_tags and tg not in NOT_TAGS:
                return tg
    return None

_trigger_verdict = {}
def _trigger_unsafe(name, stack=()):
    """Reason string if scripted trigger `name` (or anything it calls) is unsafe to paste."""
    if name in _trigger_verdict:
        return _trigger_verdict[name]
    if name in stack:
        return None
    s = _strip(scripted_triggers[name])
    why = None
    if _uses_root_or_top_prev(s):
        why = f'trigger {name} uses ROOT/PREV'
    elif _unknown_tag(s):
        why = f'trigger {name} names undefined tag {_unknown_tag(s)}'
    else:
        for callee in TRIGGER_CALL.findall(s):
            if callee in scripted_triggers:
                why = _trigger_unsafe(callee, stack + (name,))
                if why:
                    break
    _trigger_verdict[name] = why
    return why

def gate_unsafe(text):
    """Reason string if a pasted `available` body cannot be evaluated correctly from the
    decision: ROOT is the HOST there and a top-level PREV is the marked state (also through
    scripted triggers), undefined country tags never resolve, @macros are file-local."""
    s = _strip(text)
    if _uses_root_or_top_prev(s):
        return 'ROOT/PREV'
    tg = _unknown_tag(s)
    if tg:
        return f'undefined tag {tg}'
    if '@' in s:
        return 'unresolved @macro'
    for idea in HAS_IDEA.findall(s):
        if idea not in all_ideas:
            return f'undefined idea {idea}'
    for callee in TRIGGER_CALL.findall(s):
        if callee in scripted_triggers:
            why = _trigger_unsafe(callee)
            if why:
                return why
    return None

def focus_decision(fid, ts):
    L = []
    L.append(f'\tht_fp_{fid} = {{')
    L.append('\t\ticon = generic_research')
    L.append('\t\tcost = 0')
    L.append('\t\tai_will_do = { factor = 0 }')  # host-only admin tool: an AI host must never pick it
    L.append('\t\tvisible = {')
    L.append('\t\t\tevent_target:ht_focus_state = { owner = { exists = yes } }')
    L.append('\t\t\tOR = {')
    L.append('\t\t\t\tAND = {')
    L.append('\t\t\t\t\thas_country_flag = ht_focus_unc')
    L.append(f'\t\t\t\t\tevent_target:ht_focus_state = {{ OWNER = {{ has_completed_focus = {fid} }} }}')
    L.append('\t\t\t\t}')
    L.append('\t\t\t\tAND = {')
    L.append('\t\t\t\t\thas_country_flag = ht_focus_com')
    L.append('\t\t\t\t\tevent_target:ht_focus_state = {')
    L.append('\t\t\t\t\t\tOWNER = {')
    if len(ts) == 1:
        L.append(f'\t\t\t\t\t\t\thas_focus_tree = {ts[0]}')
    else:
        L.append('\t\t\t\t\t\t\tOR = {')
        for t in ts:
            L.append(f'\t\t\t\t\t\t\t\thas_focus_tree = {t}')
        L.append('\t\t\t\t\t\t\t}')
    L.append(f'\t\t\t\t\t\t\tNOT = {{ has_completed_focus = {fid} }}')
    av = focus_info[fid]['avail']
    why = gate_unsafe(av) if av is not None else None
    if why:
        # A gate that would be evaluated against the wrong country (or not at all) is
        # dropped; complete_national_focus ignores `available` anyway.
        gate_dropped.append((fid, why))
        av = None
    if av is not None:
        L.append('\t\t\t\t\t\t\tAND = {')
        L.append(av)
        L.append('\t\t\t\t\t\t\t}')
    L.append('\t\t\t\t\t\t}')
    L.append('\t\t\t\t\t}')
    L.append('\t\t\t\t}')
    L.append('\t\t\t}')
    L.append('\t\t}')
    L.append('\t\tcomplete_effect = {')
    L.append('\t\t\tif = {')
    L.append('\t\t\t\tlimit = { event_target:ht_focus_state = { owner = { exists = yes } } }')
    L.append('\t\t\tevent_target:ht_focus_state = {')
    L.append('\t\t\t\towner = {')
    L.append('\t\t\t\t\tif = {')
    L.append('\t\t\t\t\t\tlimit = { ROOT = { has_country_flag = ht_focus_unc } }')
    L.append(f'\t\t\t\t\t\tuncomplete_national_focus = {{ focus = {fid} uncomplete_children = yes refund_political_power = yes }}')
    L.append('\t\t\t\t\t}')
    L.append('\t\t\t\t\telse = {')
    L.append(f'\t\t\t\t\t\tcomplete_national_focus = {fid}')
    L.append('\t\t\t\t\t}')
    L.append('\t\t\t\t\tsave_global_event_target_as = ht_note_fp_a')
    L.append('\t\t\t\t}')
    L.append('\t\t\t}')
    L.append('\t\t\tif = { limit = { NOT = { has_country_flag = ht_notify_cd } } set_country_flag = { flag = ht_notify_cd days = 1 } news_event = { id = hosttool.73 } }')
    L.append('\t\t\t}')
    L.append('\t\t}')
    L.append('\t}')
    return '\n'.join(L)

fp_lines = ['# GENERATED FILE - do not edit by hand. Re-run generate_pickers.py after focus-tree changes.',
            'host_tool_focus_category = {']
for fid, ts in included:
    fp_lines.append(focus_decision(fid, ts))
fp_lines.append('}')
with open(os.path.join(OUT, 'host_tool_focus_picker.txt'), 'wb') as f:
    f.write(('\n'.join(fp_lines) + '\n').encode('latin-1'))
from collections import Counter
rep(f'available gates dropped: {len(gate_dropped)} '
    f'{dict(Counter(w.split(" ")[0] if not w.startswith("trigger") else "via-trigger" for _, w in gate_dropped))}')
rep(f'  via-trigger/tag/macro detail: {[(f, w) for f, w in gate_dropped if w != "ROOT/PREV"]}')

# ---------- scan idea pool ----------
idea_files = pool('common/ideas')
country_ideas = {}   # idea -> file
hidden_pool = set()
idea_name_field = {} # idea -> name= value if set
for path in idea_files:
    text = read_text(path)
    root = parse(text)
    for top in root.children:
        if (top.key or '').lower() == 'ideas' and top.children is not None:
            for cat in top.children:
                if cat.key is None or cat.children is None:
                    continue
                for idea in cat.children:
                    if idea.key is None or idea.children is None:
                        continue
                    if cat.key == 'country':
                        country_ideas.setdefault(idea.key, path)
                        nm = idea.val('name')
                        if nm:
                            idea_name_field[idea.key] = nm
                    elif cat.key == 'hidden_ideas':
                        hidden_pool.add(idea.key)

host_own = {i for i, p in country_ideas.items() if os.path.basename(p) == 'hostool.txt'}
excluded_hidden_named = {i for i in country_ideas if 'hidden' in i.lower()}
sp_pool = sorted((set(country_ideas) - host_own - excluded_hidden_named)
                 | {h for h in CURATED_HIDDEN if h in hidden_pool})
missing_curated = [h for h in CURATED_HIDDEN if h not in hidden_pool]
rep(f'idea pool: country={len(country_ideas)} hidden={len(hidden_pool)}; sp decisions={len(sp_pool)}')
rep(f'excluded: hosttool-own={sorted(host_own)} hidden-named={len(excluded_hidden_named)}; curated missing from pool={missing_curated}')

# idea -> granting trees
idea_trees = {}
for idea, fids in add_map.items():
    ts = set()
    for fid in fids:
        ts |= focus_trees.get(fid, set())
    if ts:
        idea_trees[idea] = sorted(ts)
addable = [i for i in sp_pool if i in idea_trees]
rep(f'ADD-able spirits (tree-granted): {len(addable)}')

def spirit_decision(idea):
    ts = idea_trees.get(idea)
    L = []
    L.append(f'\tht_sp_{idea} = {{')
    L.append('\t\ticon = generic_research')
    L.append('\t\tcost = 0')
    L.append('\t\tai_will_do = { factor = 0 }')  # host-only admin tool: an AI host must never pick it
    L.append('\t\tfire_only_once = no')
    L.append('\t\tvisible = {')
    L.append('\t\t\tevent_target:ht_focus_state = { owner = { exists = yes } }')
    L.append('\t\t\tOR = {')
    L.append(f'\t\t\t\tAND = {{ has_country_flag = ht_spirit_remove event_target:ht_focus_state = {{ owner = {{ has_idea = {idea} }} }} }}')
    if ts:
        gate = ' '.join(f'has_focus_tree = {t}' for t in ts)
        L.append(f'\t\t\t\tAND = {{ has_country_flag = ht_spirit_add event_target:ht_focus_state = {{ owner = {{ NOT = {{ has_idea = {idea} }} OR = {{ {gate} }} }} }} }}')
    L.append('\t\t\t}')
    L.append('\t\t}')
    L.append('\t\tcomplete_effect = {')
    L.append('\t\t\tif = {')
    L.append('\t\t\t\tlimit = { event_target:ht_focus_state = { owner = { exists = yes } } }')
    L.append('\t\t\tevent_target:ht_focus_state = { owner = {')
    L.append(f'\t\t\t\tif = {{ limit = {{ ROOT = {{ has_country_flag = ht_spirit_remove }} }} remove_ideas = {idea} }}')
    L.append(f'\t\t\t\telse = {{ add_ideas = {idea} }}')
    L.append('\t\t\t} }')
    L.append('\t\t\t}')
    L.append('\t\t}')
    L.append('\t}')
    return '\n'.join(L)

sp_lines = ['# GENERATED FILE - host tool national-spirit picker (ADD + REMOVE). Re-run generate_pickers.py after idea/focus changes.',
            '# Spirit: Rem (ht_spirit_remove) lists spirits the marked owner HAS; Spirit: Add (ht_spirit_add) lists spirits its focus tree(s) grant that it lacks.',
            'host_tool_spirit_category = {']
for idea in sp_pool:
    sp_lines.append(spirit_decision(idea))
sp_lines.append('}')
with open(os.path.join(OUT, 'host_tool_spirit_picker.txt'), 'wb') as f:
    f.write(('\n'.join(sp_lines) + '\n').encode('latin-1'))

# ---------- localisation ----------
# Keys may sit at column 0 (vanilla toa_focus_l_english.yml does) or be indented.
# A trailing `# comment` after the closing quote is legal (vanilla SEA_focus_l_english.yml).
LOC_RE = re.compile(r'^[ \t]*([A-Za-z0-9_.\-]+):\d*[ \t]+"(.*)"(?:[ \t]*#.*)?\s*$')
loc = {}
def load_loc(files):
    for p in files:
        try:
            with open(p, 'rb') as fh:
                txt = fh.read().decode('utf-8-sig', errors='replace')
        except OSError:
            continue
        for line in txt.splitlines():
            m = LOC_RE.match(line)
            if m:
                loc[m.group(1)] = m.group(2)
load_loc(sorted(glob.glob(os.path.join(VAN, 'localisation', 'english', '**', '*.yml'), recursive=True)))
load_loc(sorted(glob.glob(os.path.join(MOD, 'localisation', '**', '*.yml'), recursive=True)))

def pretty(ideaid):
    s = re.sub(r'^[A-Z]{2,4}_', '', ideaid)
    s = s.replace('_', ' ').strip()
    return s.title() if s else ideaid

# focus loc: the focus's own display key (text = override, else its id) when that key exists;
# an unresolved $key$ renders blank in game, so fall back to a readable id.
fp_loc = ['﻿l_english:']
fp_unresolved = []
for fid, _ in included:
    key = focus_info[fid]['text'] or fid
    if key in loc:
        fp_loc.append(f' ht_fp_{fid}:0 "${key}$"')
    else:
        fp_unresolved.append(fid)
        fp_loc.append(f' ht_fp_{fid}:0 "{pretty(fid)}"')
with open(os.path.join(OUT, 'ht_focus_picker_l_english.yml'), 'wb') as f:
    f.write(('\r\n'.join(fp_loc) + '\r\n').encode('utf-8'))
rep(f'focus loc: {len(included)} keys, {len(fp_unresolved)} unresolved->prettified {fp_unresolved}')

unresolved = []
sp_loc = ['\ufeffl_english:']
for idea in sp_pool:
    key = idea_name_field.get(idea, idea)
    txt = loc.get(key)
    if txt is None:
        txt = loc.get(idea)
    if txt is None:
        txt = pretty(idea)
        unresolved.append(idea)
    txt = txt.replace('"', "'")
    sp_loc.append(f' ht_sp_{idea}:0 "{txt}"')
with open(os.path.join(OUT, 'ht_spirit_picker_l_english.yml'), 'wb') as f:
    f.write(('\r\n'.join(sp_loc) + '\r\n').encode('utf-8'))
rep(f'spirit loc: {len(sp_pool)} keys, {len(unresolved)} unresolved->prettified (sample {unresolved[:10]})')

# ---------- self-verification ----------
from pdxparse import parse as reparse
for fn in ('host_tool_focus_picker.txt', 'host_tool_spirit_picker.txt'):
    t = read_text(os.path.join(OUT, fn))
    r = reparse(t)
    cats = [c for c in r.children if c.key in ('host_tool_focus_category', 'host_tool_spirit_category')]
    n = len(cats[0].children) if cats else -1
    rep(f'reparse {fn}: top-level cats={len(r.children)} decisions={n}')
    assert len(r.children) == 1, fn
o, c = 0, 0
for fn in ('host_tool_focus_picker.txt', 'host_tool_spirit_picker.txt'):
    t = read_text(os.path.join(OUT, fn))
    # brace balance outside comments
    t2 = re.sub(r'#[^\n]*', '', t)
    rep(f'{fn}: brace delta = {t2.count("{") - t2.count("}")}')

for fn, rel in (('host_tool_focus_picker.txt', 'common/decisions'),
                ('host_tool_spirit_picker.txt', 'common/decisions'),
                ('ht_focus_picker_l_english.yml', 'localisation/english'),
                ('ht_spirit_picker_l_english.yml', 'localisation/english')):
    dest = os.path.join(MOD, *rel.split('/'), fn)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(os.path.join(OUT, fn), dest)
    print('wrote', dest)
shutil.rmtree(OUT, ignore_errors=True)
print('DONE')
