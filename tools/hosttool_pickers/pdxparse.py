"""Minimal Paradox-script tokenizer/parser shared by the host-tool generators.
Byte-safe: files are read as bytes and decoded latin-1 so re-emission preserves bytes.
"""
import re

def read_text(path):
    with open(path, 'rb') as f:
        raw = f.read()
    if raw.startswith(b'\xef\xbb\xbf'):  # strip UTF-8 BOM so the first token parses
        raw = raw[3:]
    return raw.decode('latin-1')

TOKEN_RE = re.compile(r'"(?:\\.|[^"\\])*"|[{}=]|[^\s{}=#"]+|#[^\n]*|\n')

def tokenize(text):
    """Yield (token, offset). Comments are skipped; newlines skipped."""
    for m in TOKEN_RE.finditer(text):
        t = m.group(0)
        if t == '\n' or t.startswith('#'):
            continue
        yield t, m.start()

class Node:
    """key = value | key = {children} | bare value"""
    __slots__ = ('key', 'value', 'children', 'start', 'end')
    def __init__(self, key=None, value=None, children=None, start=-1, end=-1):
        self.key = key; self.value = value; self.children = children
        self.start = start; self.end = end
    def find_all(self, key):
        return [c for c in (self.children or []) if c.key is not None and c.key.lower() == key.lower()]
    def find(self, key):
        r = self.find_all(key)
        return r[0] if r else None
    def val(self, key, default=None):
        n = self.find(key)
        return n.value if n and n.value is not None else default

def parse(text):
    """Parse whole file into a root Node with children."""
    toks = list(tokenize(text))
    pos = 0
    def parse_block(i, is_root=False):
        children = []
        while i < len(toks):
            t, off = toks[i]
            if t == '}':
                if is_root:
                    # stray closer at file level: PDX ignores it
                    import sys
                    print('WARN: stray } at file level ignored', file=sys.stderr)
                    i += 1
                    continue
                return children, i + 1, off + 1
            # lookahead for '='
            if i + 1 < len(toks) and toks[i+1][0] == '=':
                key = t
                j = i + 2
                # tolerate '==' style? (rare '>' '<' not handled; treat as value tokens)
                if j < len(toks) and toks[j][0] == '{':
                    sub, j2, endoff = parse_block(j + 1)
                    children.append(Node(key=key, children=sub, start=off, end=endoff))
                    i = j2
                else:
                    children.append(Node(key=key, value=toks[j][0] if j < len(toks) else None, start=off,
                                         end=(toks[j][1] + len(toks[j][0])) if j < len(toks) else off))
                    i = j + 1
            elif t == '{':
                sub, j2, endoff = parse_block(i + 1)
                children.append(Node(key=None, children=sub, start=off, end=endoff))
                i = j2
            else:
                children.append(Node(key=None, value=t, start=off, end=off + len(t)))
                i = i + 1
        if is_root:
            return children, i, toks[-1][1] if toks else 0
        # PDX parser auto-closes unbalanced blocks at EOF; mirror that leniently
        import sys
        print('WARN: auto-closed unbalanced block at EOF', file=sys.stderr)
        return children, i, toks[-1][1] + len(toks[-1][0]) if toks else 0
    children, _, _ = parse_block(0, is_root=True)
    root = Node(key='<root>', children=children)
    return root

def strip_quotes(s):
    if s and len(s) >= 2 and s[0] == '"' and s[-1] == '"':
        return s[1:-1]
    return s

def block_text(text, node):
    """Original source slice of a node's block including braces start..end."""
    return text[node.start:node.end]

def inner_block_text(text, node):
    """Source between the braces of key = { ... } (excludes braces)."""
    # find first '{' after start
    b = text.index('{', node.start)
    return text[b+1:node.end-1]
