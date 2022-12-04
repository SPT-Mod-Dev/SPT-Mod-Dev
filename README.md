# Saving Private Tryin' Historical MP Full Changelog

### 3.2.2 - Balancing Update

#### Axis Rules
- Removed rule number 2 for Italy allowing them to join the war whenever they wish

#### Allies Rules
- Added rule for France "Must have pulled out of mainland Europe by September 1940" 

#### Soviet Union 
- Some focus days have been increased: [Slightly delay industry focuses to delay factory buffs]
    - "Infrastructure Effort" `35 → 70`
    - "Heavy Industry" `35 → 70`
- Decreased the number of tech bonuses gained from "Soviet artillery" `2 -> 1` [Reduce the technological advantage of soviets over germany]
- Removed the `+5%` efficiency cap received from "PC of Mechanical Engineering" [Reduce max cap soviets are able to get]
- Revert the initial change to "Turkey Seizes Control Over the Bosporus" event so war support gained is now `10% -> 5%` [Slow down Soviet industry slightly but also increase pp cost which soviets can struggle with]

#### Mexico
- Removed option to return Trotsky to the Soviet Union [Returning trotsky gives soviets a buff which is only available if allies have plenty of players which dosent make too much sense]

#### Australia
- Reduced number of tech bonuses from "CAC Woomera" `2 -> 1`

#### Tank Designer
- Modules:
    - Auto Loader: [Only Soviets and Spain use this thanks to focuses so nerf it slightly]
        - Decreased soft attack `+25% → +15%` 
        - Decreased hard attack `+25% → +15%`
        - Decreased ic cost `+2.5 -> +2`
    - Sloped Armor: [Buff as the 20% armour bonus is generally not worth 10% ic cost]
        - Decreased ic cost multiplier `+10% -> +5%`
    - Easy Maintenace: [Slight nerf as outweighs wet ammo storage IF u have spare research]
        - Increased ic cost `0 -> +1`
    - Dozer Blade: [Slight buff as not seen used as the cost outweight the gain]
        - Addded breakthrough modifier `-10%` 
        - Increased defense `+2.5 -> +10` 
    - Small Cannon: [Buff as Cost is too high to outweigh picking it over Heavy mg]
        - Decreased ic cost `+4 -> +2`
        - Increased soft attack `+5 -> +7.5`
    - Smoke Launchers: [Slight nerf as their ic cost makes it normally not a bad choice]
        - Increased ic cost `+0.25 -> +0.5`
    - Additional Machineguns: [slight buff to make them a cheap alternative to small cannon/heavy mg]
        - Decreased ic cost `+0.75 -> 0.5`

- Armaments:
    - Medium Fixed Superstructure: [ Changed to remove meta mediums and give heavy more of an advantage of higher stats]
        - Removed that it allowed heavy cannons to be used.
    - Automatic Cannon 1:
        - Decreased soft attack `+24 -> 20` [same as auto 2]
    - Automatic Cannon 2:
        - Decreased soft attack `+36 -> 32` [Nerf as it outweighed other turrets for light and enabled to high stats for cheap lights] 
    - Medium Cannon 2:
        - Increased soft attack `25.5 -> 30` [Buff as medium 1's were better than 2's (resources ic and very similar stats) and small guns were better for the most part]
        - 
- Turrets: [Slight nerf on 3 man as theres little reason to not either go fixed for tds and arty or 3 man for regulars ]
    - Light two man turret:
        - Increased ic cost `+0.75 -> +1`
    - Light three man turret:
        - Increased ic cost `+1 -> +1.5`
    - Medium two man turret:
        - Increased ic cost `+2.5 -> +3`
    - Medium three man turret:
        - Increased ic cost `+3 -> +4`
    - Heavy two man turret:
        - Increased ic cost `+5 -> +4`
        - Decreaseed speed `-0.4 -> -0.5` [ nerf heavies as they could go too fast with ok reliability]
     - Heavy three man turret:
        - Increased ic cost `+5 -> +4`
        - Decreaseed speed `-0.4 -> -1` [ same as 2 man]   

- Chasis:
    - Heavy 1:
        - Increase ic cost `+16 -> +20` [Increase ic cost gap between mediums and heavys]
    - Heavy 2:
        - Increase ic cost `+16 -> +20` [same as heavy 1]




### 3.2.1 - Tungsten Update

- Updated to Tungsten hoi4 version (1.12.6)

#### France
- Push into Italy decision
    - Replaced condition of katowice being controlled [typo mistake] to Alpes
    - Added condition that France has to have fallen
    - Makes the decision available to England if there is not french player [Incase france leaves allies can still remove defense modifier if they have retaken france]

#### Hungary
- Changed days of "Claim Overlordship of Slovakia" `70` -> `35`
- Remove the cores gained from completing "Claim Overlordship of Slovakia"
- Added focus "Integrate Slovakia":
    - Requires "Claim Overlordship of Slovakia"
    - Takes `35` days    
    - Gives cores on Slovakia


### 3.2.0 - Mediterranean Front Update

#### Tutorial
- Added a few decisions to give some extra info to new players: "General Multiplayer Info", "Pacific Front Info" and "Med Front Info"

#### Axis Rules
- Removed rule "Cannot have units in Africa before Italy joins World War 2." for all Axis members

#### Italy
- Removed check that Italy have an enemy that is a major for "Supermarina" [Unlocks very powerful navy focuses earlier on]
- Removed balance of power checks and rewards for focuses if Italy is in WW2 [As theyre starting bop is removed]

#### France
- Added decision "Push into Italy" which removes all the "Home Defence" state modifiers (see below) in Italy once the allies has retaken Paris and their land East of the Rhone

#### Ethiopia
- Hid decision to ask UK to host Ethiopia in exile [Ethiopia doesnt fight on so pacifiying them is easier]

#### Mediterranean Front
- Added a balance of power mechanic to the Mediterranean front similar to the previous system.
- When certain positions are captured by England (or their allies) or Italy (or their allies) the balance of power (bop) will move `15%` to the side who just captured the island
- English targets
    - Sardegna
    - Sicillia
    - Crete
    - Dodecaneso
    - Tripoli
    - Benghasi

- Italian targets
    - Malta
    - Suez
    - Gibraltar
    - Corsica
    - Cyprus
    - Algiers

- Added an event when one of the defensive targets is lost [To ensure the player is aware they are losing targets]
- Added a state modifier to the Italian (minus Sicily) and English homeland that initially gives `+60%` core attack and defense.
- Bop ranges
    - Stalemate (`25% - 0% - 25%`)
        - For Italian and England "Impenetrable Home Defense" which gives
            - `+60%` core attack
            - `+60%` core defense
    - Low Italian Dominance (`25% - 50%`)
        - Italy:
            - `+5%` recovery rate
            - `+5%` division attack
            - `+5%` division defense
            - `+10%` war support
        - England:
            - `-5%` recovery rate
            - `-5%` division attack
            - `-5%` division defense
            - `-10%` stability
            - Replaces "Impenetrable Home Defense" with "Strong Home Defense" which gives
                - `+40%` core attack
                - `+40%` core defense
    - Medium Italian Dominance (`50% - 75%`)
        - Italy:
            - `+10%` recovery rate
            - `+10%` division attack
            - `+10%` division defense
            - `+20%` war support
            - `+10%` political power gain
        - England:
            - `-10%` recovery rate
            - `-10%` division attack
            - `-10%` division defense
            - `-20%` stability
            - Replaces "Strong Home Defense" with "Weakened Home Defense" which gives
                - `+20%` core attack
                - `+20%` core defense

    - Total Italian Dominance (`75% - 100%`)
        - Italy:
            - `+15%` recovery rate
            - `+15%` division attack
            - `+15%` division defense
            - `+30%` war support
            - `+20%` political power gain
            - `-15%` resistance activity
        - England:
            - `-15%` recovery rate
            - `-15%` division attack
            - `-15%` division defense
            - `-30%` stability
            - `-10%` political power gain
            - Removed "Weakened Home Defense"
    - Low English Dominance (`25% - 50%`)
        - Italy:
            - `-5%` recovery rate
            - `-5%` division attack
            - `-5%` division defense
            - `-10%` stability
            - For Italy replaces "Impenetrable Home Defense" with "Strong Home Defense" which gives
                - `+40%` core attack
                - `+40%` core defense
        - England:
            - `+5%` recovery rate
            - `+5%` division attack
            - `+5%` division defense
            - `+10%` war support
    - Medium English Dominance (`50% - 75%`)
        - Italy:
            - `-10%` recovery rate
            - `-10%` division attack
            - `-10%` division defense
            - `-20%` stability
            - For Italy Replaces "Strong Home Defense" with "Weakened Home Defense" which gives
                - `+20%` core attack
                - `+20%` core defense
        - England:
            - `+10%` recovery rate
            - `+10%` division attack
            - `+10%` division defense
            - `+20%` war support
            - `+10%` political power gain
    - Total English Dominance (`75% - 100%`)
        - Italy:
            - `+15%` recovery rate
            - `+15%` division attack
            - `+15%` division defense
            - `+30%` war support
            - `+20%` political power gain
            - `-15%` resistance activity
        - England:
            - `-15%` recovery rate
            - `-15%` division attack
            - `-15%` division defense
            - `-30%` stability
            - `-10%` political power gain
            - Removed "Weakened Home Defense"

- Added "Offensive targets" and "Defensive targets" dummy decisions to show which positions should be attacked and defended
- Added "Feign Weakness" decision
    - `30` cp cost
    - `180` days till it re-enables
    - For `60` days gives:
        - `+30%` division attack
        - `+30%` division defence 
    - Moves bop `10%` towards the enemies side [Similar to P]
    - Fires event on enemy which notifies them that you seem weak [Allows the other player to either counter the decision with their own or try and save their bop and hold off the attack]   
- Added "Fortify Positions" decision
    - `25` pp cost
    - Can only be fired `1` time
    - For `50` days gives:
        - `+100%` coastal fort construction speed
        - `+100%` land fort construction speed
- Added "Expand Capacity Decision" decision 
    - `50` pp cost
    - Can only be fired `1` time
    - For `100` days gives:
        - `+10%` supply consumption
        - `+100%` railway construction speed
        - `+100%` naval base construction speed





### 3.1.4 - Small designer tweaks
#### Tank Designer
- Added module limit of `1` for extra ammunition storage
- Made all tank designs not cost xp
#### Air Designer
- Made all plane designs not cost xp

### 3.1.3 - Minor bugfixes
#### UK
 - Fixed "Reinforce The Empire" being in the wrong position
#### Soviet Union
 - Patched exploit from "Restore Cossack Units" by removing the 1 infantry division you gain [Renaming any template to the infantry name would spawn that division when the focus was done. Doesnt work for horse divions btw]

### 3.1.2 - Performance Addition
- Merged Spot Optimization Mod which does:
    - Lag days for lower speed = `30`
    - Lag days for pause = `8`
    - Game speed seconds = `{ 1.0, 0.25, 0.1, 0.05, 0.0 }`
    - Event process offset = `30`
    - Map icon passes = `10`
- Added two console commands
    - SPT_Remove_Pacific_Front
    - SPT_Activate_Pacifc_Front


#### Argentina
- Removed Argentina F

#### Pacific Front
- Added event for when the pacific war begins


### 3.1.1 - Minor bugfixes

- Fixed bug of medium cannons not showing

#### Hungary
- "Claim Overlordship Over Slovakia" no longer requires Slovakia to exist
- Replaced at peace with Hungary prerequisite with in faction with Hungary for "Claim Overlordship Over Slovakia"
- Removed manpower prerequisite for "Claim Overlordship Over Slovakia"
- Removed Demand Transylvania,Southern Slovakia,Vojvodina and "Proclaim Greater Hungary" focuses
 

### 3.1.0 - Pacific Front Update

#### Pacific Front
- Added a balance of power mechanic to the pacific front similar to the previous system.
- When certain islands are captured by USA (or their allies) or Japan (or their allies) the balance of power (bop) will move `10%` to the side who just captured the island
- American targets
    - Okinawa
    - Taiwan
    - Iwo Jima
    - Marcus Island
    - Saipan
    - Kuril Islands
    - Palau
    - Caroline Islands
    - Marshall Islands
    - Hainan

- Japanese targets
    - Hawaii
    - Johnston Atoll
    - Midway Island
    - Wake Island
    - Guam
    - Manilla
    - Mindanao
    - Papua
    - Bismarck
    - Solomon Islands

- Added an event when one of the defensive targets is lost [To ensure the player is aware they are losing targets]
- Added a state modifier to the Japanese homeland and the USA west coast that initially gives `+60%` core attack and defense.
- Bop ranges
    - Stalemate (`25% - 0% - 25%`)
        - For Japan and USA "Impenetrable Home Defense" which gives
            - `+60%` core attack
            - `+60%` core defense
    - Low Japanese Dominance (`25% - 50%`)
        - Japan:
            - `+5%` recovery rate
            - `+5%` division attack
            - `+5%` division defense
            - `+10%` war support
        - USA:
            - `-5%` recovery rate
            - `-5%` division attack
            - `-5%` division defense
            - `-10%` stability
            - Replaces "Impenetrable Home Defense" with "Strong Home Defense" which gives
                - `+40%` core attack
                - `+40%` core defense
    - Medium Japanese Dominance (`50% - 75%`)
        - Japan:
            - `+10%` recovery rate
            - `+10%` division attack
            - `+10%` division defense
            - `+20%` war support
            - `+10%` political power gain
        - USA:
            - `-10%` recovery rate
            - `-10%` division attack
            - `-10%` division defense
            - `-20%` stability
            - Replaces "Strong Home Defense" with "Weakened Home Defense" which gives
                - `+20%` core attack
                - `+20%` core defense

    - Total Japanese Dominance (`75% - 100%`)
        - Japan:
            - `+20%` recovery rate
            - `+20%` division attack
            - `+20%` division defense
            - `+30%` war support
            - `+20%` political power gain
            - `-15%` resistance activity
        - USA:
            - `-20%` recovery rate
            - `-20%` division attack
            - `-20%` division defense
            - `-30%` stability
            - `-10%` political power gain
            - Removed "Weakened Home Defense"
    - Low American Dominance (`25% - 50%`)
        - Japan:
            - `-5%` recovery rate
            - `-5%` division attack
            - `-5%` division defense
            - `-10%` stability
            - For Japan replaces "Impenetrable Home Defense" with "Strong Home Defense" which gives
                - `+40%` core attack
                - `+40%` core defense
        - USA:
            - `+5%` recovery rate
            - `+5%` division attack
            - `+5%` division defense
            - `+10%` war support
    - Medium American Dominance (`50% - 75%`)
        - Japan:
            - `-10%` recovery rate
            - `-10%` division attack
            - `-10%` division defense
            - `-20%` stability
            - For Japan Replaces "Strong Home Defense" with "Weakened Home Defense" which gives
                - `+20%` core attack
                - `+20%` core defense
        - USA:
            - `+10%` recovery rate
            - `+10%` division attack
            - `+10%` division defense
            - `+20%` war support
            - `+10%` political power gain
    - Total American Dominance (`75% - 100%`)
        - Japan:
            - `+20%` recovery rate
            - `+20%` division attack
            - `+20%` division defense
            - `+30%` war support
            - `+20%` political power gain
            - `-15%` resistance activity
        - USA:
            - `-20%` recovery rate
            - `-20%` division attack
            - `-20%` division defense
            - `-30%` stability
            - `-10%` political power gain
            - Removed "Weakened Home Defense"

- Added "Offensive targets" and "Defensive targets" dummy decisions to show which islands should be attacked and defended
- Added "Prepare assault" decision
    - `50` pp cost
    - `90` day cooldown
    - For `30` days gives:
        - `-50%` invasion preparation time
        - `+100%` invasion planning speed
    - When removed adds:
        - Activates "Secure pacific target" mission which gives `30` days to try and capture an island. If it fails the bop moves to the other side by `5%`. [This is to create a risk vs reward mechanic where the players gets an option to increase chances of taking an island at the risk of bop going the opposite way if they fail]
        - Adds "Impending Japanese (or American) Assault" to the offensive targets and the lost defensive targets which gives:
            - `-30%` divison defense
- Added "Fortify islands" decision
    - `50` pp cost
    - Can only be fired `1` time
    - For `100` days give:
        - `+100%` coastal fort construction speed

- On capitulation of either side the bop will be removed and the winning country will get the permenant buffs of Total Victory

#### Italy
 - Prevented "Supremacy in the skies" to give a variant with a jet engine unless jet engines have been researched


### 3.0.0 - By Blood Alone Update

- XP cap increased `500 → 1000`
- Division template XP cost removed:
  - Battalion `5 → 0`
  - Support company `10 → 0`
  - New Battalion type `25 → 0`
- Ahistorical focus paths of playable countries have been hidden
- Added 50% more building slots in each state
- Added impassable terrain around Gibraltar
- Removed adaptable trait
- Removed mine research
- Removed mine laying/sweeping technology focuses 
- Hid ahistorical political advisors
- Nerfed air production continuous focus `-10% → -5%`
- Total Mobilisation can only be selected if Germany is at war with the Soviet Union (Japan is an exception)
- Set agency upgrade cost to `0`
- Made Finland AI always refuse Soviet's ultimatum
- First land, navy, and air doctrine cost removed `100 → 0`
- Increased special forces battalion minimum cap `24 → 64`
- Removed some ahistorical event options
- Added 50-width training division to each player
- Researched basic trains for all players
- Removed all starting guarantees
- Moved #1143 and #12764 provinces into "Matrouh"(#452) state
- Moved #1060 and #11951 provinces into "Cyrenaica"(#663) state
- Changed refinery IC cost `14500 → 10800`
- Tripled the cost of all plane airframes
- Replaced civil war when grand council get total control with -50% stability
- Removed Blueprint Stealing operations
- Removed Blueprint Stealing upgrade
- Removed No Garrison occupation law
- Last stand and force attack org loss reduced `-100% → -90%`
- Designing ships no longer costs naval xp
- Extra fuel tank IC cost increased `+5% → +25%` of total IC
- Added new Loading Screens
- Added continuous focus which gives 1000 manpower a week
- Merged starting navies of majors
- Incorporated the Modifier Icons mod

#### Australia
- "Support the Policy of Appeasement" focus gives a silent workhorse for free
- "Citizen Military Forces focus" ups your conscription by `1`
- You can now annex New Zealand if it's AI via decision
- Australia can now go free with the "Fight, Work or Perish" focus

#### Canada
- "Crown Corporations" focus gives you a captain of industry instead of just unlocking one
- Some focus days have been reduced:
  - "Crown Corporations" `70 → 35`
  - "Canadian Pacific Railway" `70 → 35`
  - "Maritime Colonial Railway" `70 → 35`
  - "Camp X" `70 → 35`
- "Imperial Oil" focus oil reward increased `14 → 28`
- Slight buffs to some spirits:
    - "War Bonds" consumer goods increased `-3% → -5%`
    - "Resources Mobilisation Act" factory output increased `2% → 5%`
    - "Bits and Peaces Program" factory output increased `2% → 5%`

#### New Zealand
- Slight buffs to some spirits:
    - "First labor government" consumer goods increased `-2% → -5%`
    - "First labor government" efficiency growth increased `2% → 5%`
    - "First labor government" factory output increased `2% → 5%`
    - "New Zealand Manpower Act" recruitable population factor increased `7% → 10%`
- Slight buff to some focuses:
    - "New Zealand Steel" steel reward increased `10 → 24`
    - "Taranaki Oil" oil reward increased `5 → 12`
    - 2NZEF focus ups your conscription by `1` now along with the vanilla buff it gives

#### South Africa
- Slight buffs to some spirits:
    - "Emergency Workers" civilian factory, military factory, infrastructure construction speed increased `7% → 10%`
    - "Cheap Labour 1" military factory & dockyard output increased `3% → 5%`
    - "Cheap Labour 2" military factory & dockyard output increased `3% → 5%`
    - "Cheap Labour 2" consumer goods increased `-3% → -5%`
    - "Cheap Labour 3" military factory & dockyard output increased `6% → 10%`
    - "Cheap Labour 3" consumer goods increased `-8% → -10%`
- "Expand the Cape Corps" focus ups your conscription by `1` now along with the vanilla buff it gives
- All army branch focus days are decreased `70 → 35`
- South Africa can now go free with the "Secure Interests in Africa" focus

#### British Raj
- Slight buffs to some spirits: 
    - "Indian Ghurkhas" recruitable population factor increased `2% → 5%`
    - "Princely States Donations" consumer goods factor increased `-3% → -5%`
    - "Princely States Donations Troops" consumer goods factor increased `-3% → -5%`
- Some focus days have been reduced:
    - "Indian Ghurkas" `70 → 56`
    - "Lions of the Great War" `70 → 56`
    - "Indian Gentlement Officers" `70 → 35`
    - "Revive the Screw Guns" `70 → 35`
    - "Expand Air Bases" `70 → 35`
- Removed Pakistani, Burmese, and Bangladesh cores
- Nepal has been annexed and cored into British Raj

#### Romania
- "King Carol's Empty Accounts" spirit days reduced `360 → 60`

#### Soviet Union
- Some focus days have been reduced:
    - "Claim Bessarabia" `70 → 7`
    - "Secure Leningrad" `70 → 7`
- "Turkey Seizes Control Over the Bosporus" event added war support for the Soviet Union increased `5% → 10%`
- Invade Iran focus can only be picked when World War 2 has begun

#### Italy
- "Prospect For Oil" oil reward increased `8 → 24`
- "Libyan Refineries" oil reward increased `4 → 12`
- "Albanian Oil" oil reward increased `2 → 16`
- Removed the bypass from "Ethiopian War Logistics" focus 
- All navy branch focus days have been reduced `70 → 35`
- Italy has been given a decision that boosts supply hub and railway construction speed for 6 months if they control Libya and Matrouh
- Added a decision to increase compliance by `80` in the occupied territories of Yugoslavia

#### Hungary
- "Secret Rearmament" focus gives Early Mobilisation
- Some focus days have been reduced:
    - "Synthetic Industry" `70 → 35`
    - "War Games" `70 → 35`
    - "Theoretical Air Efforts" `70 → 35`
- "Claim Overlordship Over Slovakia" can be done if Slovakia exists
- "Claim Overlordship Over Slovakia" gives Hungary Slovakia as cores only if Germany agrees
- "Strengthen the Fascists" spirit daily fascism has been increased `+0.03 → +0.05`

#### China
- Sinkiang, Xibei San Ma, Communist China, Shanxi, Yunnan, Guangxi Clique has been annexed and cored into China
- China has been renamed to Chinese United Front

#### Argentina
- Uruguay has been annexed and cored into Argentina
- Added decision and corresponding event chain for Argentina requesting Falkland Islands from UK
- Set game rule to not be able to join factions

#### Trade Federations
- Cuba, Haiti, Dominican Republic, Guatemala, Honduras, El Salvador, Nicaragua, Costa Rica, Panama, Colombia, Venezuela, Ecuador, Peru, Bolivia, Chile & Paraguay has been merged into American Trade Federation (Neutral Trade Nation)
- Saudi Arabia, Yemen & Oman has been merged into Middle East Trade Federation (Neutral Trade Nation)
- Tibet & Bhutan has been merged into Himalayan Trade Federation (Neutral Trade Nation)

#### Germany
- Added Lapland event which grants Germany resource rights to Lapland if they control Oslo
- Befriend Turkey focus removed from the focus tree
- Some focus days have been reduced:
    - "War with USSR" `70 → 14`
    - "Befriend Japan" `70 → 7`
- Rudolf Hess political power bonus increased `+15% → +25%`
- Jaegernotprogramm is now constantly visible, duration increased `90 → 365`, and only requires you to be at war

#### USA
- Added event when Denmark capitulates, Greenland gets transferred to USA

#### Siam
- Added decision and corresponding event chain for Siam requesting Indochina from Japan

#### Bulgaria
- Bulgaria can get their claimed territory by doing the "Approach Germany" focus

#### Yugoslavia
- Removed Anti-German military spirit 

#### Mexico
- "National Bank" focus now gives "Banco de Mexico" spirit instead of just unlocking it
- Wargoal option removed from Mexican nationalization of oil events
- Added event to object to Anschluss

#### France
- "Buy Time" focus gives the humble appeaser instead of just unlocking it
- Gets the Free French focus tree upon capitulation
- "Support the Finns" focus XP reward increased `20 → 100`

#### Vichy France
- Removed options to form Vichy France

#### Manchukuo
- Manchukuo starts with Mengukuo annexed and the focus to annex it removed
- Manchurian focus to core China has been removed, Manchukuo gets cores on China via "Obedience" focus 
- Manchukuo's low legitimacy can be fully removed by taking the "Chinese leadership" focus
- "Hoanyoku" focus for Manchukuo gives China -30% surrender limit, the AI cannot pick the focus  

#### UK
- Can develop New Zealand without developing Australia now
- Some focus days have been reduced:
    - "Crypto Bomb" `70 → 14`
    - "Vanguard" `70 → 28`
    - "Fortify the Rock" `70 → 35`
    - "Protect Suez" `70 → 35`
    - "Fortify Malta" `70 → 35`
    - "Sanction Japan" `70 → 35`
    - "The Singapore Strategy" `70 → 35`
    - "Landward Fortifications" `70 → 35`
    - "Peninsular War" `70 → 35`
    - "Hold Hong Kong" `70 → 35`
    - "Air Defenses" `70 → 35`
    - "Steady as She Goes" `70 → 35`
    - "Secure Iraq" `70 → 7`
    - "Secure Iran" `70 → 7`
- Indian Independence focus from UK focus tree removed
- UK's Imperial Conference focus no longer has autonomy prerequisites

#### Japan
- "Secure China" focus has been removed
- "Supremacy of Technology" spirit's infantry research has been buffed `+5% → +10%`
- "Strengthen the Divine Wind" no longer requires Jet technology
- "Alliance With Siam" now annexes Siam if it is AI
- "Chinese Resources" focus is available if any country in a faction with Japan controls the required states
- "Agility Focus" now removes the "Duplicate Research Efforts" spirit
- "Unified Fighter Development" no longer removes the "Duplicate Research Efforts" spirit
- "Unified Fighter Development" now gives a `100%` research boost for fighter models AND heavy fighter models
- "State Shintoism" spirit now gives a `+20%` attack & defense bonus on core territory
- "Militarism" spirit now gives `+15%` building speed for military factories & dockyards
- "Zaibatsus" spirit no longer has `+5%` consumer goods debuff
- "Tora Tora Tora" spirit is added once Japan declares war on the Allies
- Added decision to declare war on Allies
- "Secure the Philippines" focus has been removed
- "Strike On The Southern Resource Area" focus has been removed

#### Army Spirit
#####  Spirit of the Academy
- Meticulous Preparation
    - Added `+7.5%` max planning bonus
- Engineering Schools:
    - Added `+15%` entrenchment speed
    - Added `+5%` max entrenchment
    - Increased Engineer XP gain `+20% → +100%`
    - Increased Fortress Buster and Scavenger XP Gain `+10% → +50%`
- Political Loyalty:
    - Increased military leader cost reduction buff `-50% → -90%`

##### Spirit of the Army
- Professional Officer Corps:
    - Increased doctrine cost reduction `-5% → -10%`
- Elevated Engineering Corps:
    - Removed `+50%` XP gain towards Engineer trait
    - Added `+10%` max entrenchment
    - Increased railway gun bombardment bonus `5% → 100%`
- Proper Heritage:
    - Added `+25%` recon bonus
    - Increased Cavalry attack `+5% → +50%`
    - Added `+50%` cavalry defense
    - Removed supply on core territory bonus 
- State Serves the Military:
    - Added army advisor cost reduction `-25%`
- Tip of the Spear:
    - Increased naval invasion capacity `+10 → +20`
    - Added `+5`% land night attack
    - Added `-10%` special forces cap limit
    - Removed special forces design cost factor
    - Increased supply grace period `+24 → +72`
    - Removed max planning
    - Increased naval invasion planning speed `+20% → +25%`
- Overwhelming Firepower:
    - Increased artillery experience gain `+10% → +100%`
    - Added `+5%` breakthrough
    - Added `+15%` artillery attack
    - Added `+5%` supply consumption
    - Removed design cost factors
- Motorization Drive:
    - Added `+15%` motorised attack & defense
    - Added `+10%` mechanised attack & defense
    - Added `+20%` supply truck attrition
    - Added `+5%` breakthrough
    - Increased motorized & mechanized experience gain `+10% → +25%`
    - Removed design cost factors
- Ideological Loyalty:
    - Reduced encirclement penalty `-20% → -25%`
    - Added `+20%` division recovery rate
- Quick Improvisation:
    - Reduced command ability cost factor `-20% → -25%`
    - Increased command power gain factor `+20% → 25%`
    - Increased planning speed factor `+20% → +50%`

##### Spirit of Division Command
- Aggressive Reconnaisance:
    - Increased Reconnaissance `15% → 50%`
    - Increased infiltration assault pick chance `+100% → +200%`
    - Increased intel from combat `15% → 50%`
    - Added `+10%` land night attack
    - Added `+10%` terrain penalty reduction
    - Added `+10%` supply consumption
- Victory or Death:
    - Increased human wave defense pick chance `+100% → +200%`
    - Decreased organization loss when below 25% `-15% → -50%`
    - Added `+10%` army attack
    - Added `-20%` army defense
- Maneuver Warfare:
    - Added `+10%` armor max speed
    - Increased unexpected thrust pick chance `+100% → +200%`
    - Removed `+5%` army speed
    - Increased coordination `5% → 20%`
    - Added `+10%` breakthrough
    - Added `-40%` organization loss when moving
    - Added `+15%` supply consumption
    - Added `+30%` truck attrition
    - Added `+10%` out of supply penalties
    - Added `+10%` army fuel consumption factor
- Smoke and Fire:
    - Increased suppressive barrage pick chance `+100% → +200%`
    - Added `+30%` artillery attack
    - Added `+10%` coordination
    - Added `+15%` supply consumption
    - Added `+5%` army defense
- Logistical Focus:
    - Increased well-planned attack pick chance `+100% → +200%`
    - Decreased supply & fuel consumption `-5% → -20%`
    - Added `+72` no supply grace
    - Added `-10%` out of supply factor
    - Added `-10%` supply penalties on core territories
- Operational Reserves:
    - Increased  relentless assault pick chance `+100% → +200%`
    - Increased HP factor `+10% → +25%`
    - Added `-10%` reinforcement rate
    - Added `+15%` army defense
    - Added `+15%` CAS damage reduction

#### Air Spirit
##### Spirit of the Air Force
- Dive Bombing:
    - Increased CAS research speed `+5% → +25%`
    - Added `+25%` naval bomber research speed
- Material Destruction:
    - Added tactical bomber research speed `+5% → +25%`
- Industrial Destruction:
    - Increased strategic bomber research speed `+5% → +25%`
    - Added `+25%` tactical bomber research speed

##### Spirit of Air Force Command
- Battlefield Air Interdiction:
    - Removed `+5%` ground attack
    - Removed `+5%` escort efficiency
    - Added `+20%` organization damage to divisions from CAS
- Centralized Control:
    - Increased fighter detection `+10% → +20%`
    - Decreased air mission efficiency `+10% → 5%`
- Home Defence:
    - Added `+15%` air home defense factor
    - Added `+10%` damage reduction against CAS
    - Added `+10%` air defense
    - Removed `+50%` ace effectiveness
- Veteran Air Instructors:
    - Added `+25%` ace generation chance
    - Decreased air XP loss when ace killed `-25% → -50%`
- Steel Wings, Steel Hearts:
    - Decreased untrained pilot penalty `-33% → -50%`
    - Added `+20%` air home defense factor
    - Added `+10%` ace generation chance
    - Added `+15%` damage reduction against CAS
    - Added `+10%` air defense
- Air Power Projection:
    - Increased air power projection factor `+10% → +25%`
    - Added `+25%` air range
- Continuous Strike:
    - Added `+25%` organization damage to divisions from CAS
    - Added `+25%` ground attack

#### Navy Spirit
##### Spirit of Naval Academy
- Signals Training:
    - Added `+10%` positioning
    - Added `+10%` coordination
- Grand Fleet:
    - Increased ironside and tactician XP gain `+20% → +100%`
    - Added `+5%` capital ship attack
- Convoy Warfare:
    - Increased seawolf and blockade runner XP gain `+20% → +100%`
    - Added `+5%` submarine attack
- Integrated Air Arm:
    - Increased air controller and fleet protector XP gain `+20% → +100%`
    - Added `+20%` carrier attack

##### Spirit of the Navy
- Naval Refit Yards increased ship repair speed `+15% → +25%`
- Global Presence:
    - Increased battleship and cruiser research speed `+20% → +25%`
    - Added `-10%` visibility
    - Added `-25%` naval attrition
    - Added `+10%` capital ship attack
    - Removed heavy hull design cost
- Submarine Primacy:
    - Added `+25%` submarine combat XP gain
    - Increased submarine research speed `+20% → +25%`
    - Added `+20%` sub retreat speed
    - Added `+10%` submarine attack
    - Removed submarine design cost
- Mobile Force:
    - Increased carrier research speed `+20% → +25%`
    - Added `+50%` XP gain for carriers
    - Added `+25%` naval air attack, targetting, and agility from carriers
    - Added `+25%` sortie efficiency
    - Removed carrier design cost

##### Spirit of Naval Command
- Surprise Attacks:
    - Removed retreat after initial combat buffs
    - Added `+50%` naval invasion speed
    - Added `+30%` coordination
    - Added `-20%` enemy retreat chance
    - Added `+50%` ships at the start of the battle
    - No longer locked behind base strike
- Efficient Communications:
    - Added `+15%` fleet coordination
    - Increased positioning `+15% → +20%`
    - Added `-25%` invasion preparation time
    - Added `+25%` naval invasion speed
- Surface Raiders:
    - Increased screening without ships `+20% → +25%`
    - Increased retreat speed and decision chance `+10% → +25%`
    - Added `+30%` convoy raiding efficiency
    - Added `+15%` capital ship attack
    - Added `-20%` submarine attack and retreat speed
- Decisive Battle:
    - Added `+25%` attack and defense for all ships
    - Added `-10%` convoy escort efficiency
    - Added `-20%` convoy retreat speed
    - Removed `+10%` hit chance-
    - Increased retreat speed and chance `10% → -25%`
    - Added `+10%` screening efficiency
    - Added `-25%` strike force movement org loss
    - Added `+5%` attack when with pride of the fleet 
- Inclement Weather Experience:
    - Now locked behind the base strike
    - Decreased bad weather penalty `-40% → -50%`
    - Added `-25%` accident chance
    - Added `+25%` sortie efficiency
    - Added `+20%` spotting speed
- Brave Commanders:
    - Added `+10%` damage
    - Decreased retreat chance `-5% → -15%`
    - Increased critical score chance `15% → 25%`
    - Added `+10%` critical receiver chance
    - Added `+50%` morale

#### Tank Designer
- Removed all dismantle costs
##### Upgrades
- Engine upgrade:
    - Decreased reliability `-1.5% → -2.5%`
- Armour upgrade:
    - Added `+1` chromium and `+1` steel for 10+ levels
    - Added `+2` chromium and `+1` steel for 15+ levels
    - Decreased reliability per level `-1.5% → -2.5%`
    - Decreased armor per level `+8.5% → +5%`
    - Removed `+1.25` breakthrough per level
##### Engines
- Gasoline engine:
    - Increased IC cost `+1 → +1.5`
    - Increased fuel consumption `+2 → +3`
    - Increased max speed `+0.5 → +1`
    - Increased max speed factor `+15% → +20%`
    - Added `-10%` reliability
- Diesel engine:
    - Decreased fuel consumption `+2 → +1.5`
    - Decreased reliability `+25% → +15%`
- Petrol-Electric engine:
    - Increased reliability `-50% → -25%`
    - Increased breakthrough `2 → 5`
    - Increased defense `2 → 5`
    - Increased breakthrough factor `+15% → +25%`
    - Increased defense factor `+15% → +25%`
    - Increased IC cost factor `+15% → +20%`
- Gas turbine engine:
    - Decreased IC cost `+3 → +2`
    - Increased fuel consumption `+4 → +5`
    - Increased max speed `+0.5 → +2`
    - Increased max speed factor `+25% → +40%`
##### Armour
- Riveted armour:
    - Removed `-20%` IC cost
- Welded armour:
    - Increased breakthrough `+2 → +3`
    - Increased defense `+2 → +3`
    - Added `+10%` build cost
    - Decreased armor value `+40% → +25%`
##### Suspension
- Bogie suspension:
    - Added `+0.5` ic cost
- Interleaved suspension:
    - Increased IC cost `+1 → +1.5`
    - Increased breakthrough `+4 → +10`
    - Removed conversion from torsion bar
- Wheeled suspension:
    - Added `+50%` speed,
- Half-track suspension:
    - Added `+0.25` build cost
    - Added `+25%` max speed factor
##### Turrets
- Light turrets forbid medium, heavy, super, and anti-tank armaments
- Light one-man turret added `+0.25` max speed
- Light fixed turret:
    - Forbids AA type
    - Removed conversion from light turret
- Medium turrets forbid heavy and super armaments
- Medium one-man turret:
    - Increased IC cost `+1 → +2`
    - Added `+0.1` max speed
    - Removed `-25%` hard and soft attack
- Medium two-man turret:
    - Increased IC cost `+1.5 → +2.5`
    - Added `-0.1` max speed
- Medium three-man turret:
    - Increased IC cost `+2 → +3`
    - Decreased max speed `-0.25 → -0.3`
- Medium fixed turret:
    - Forbids AA type
    - Removed conversion from medium turret
- Heavy turrets:
    - Forbids super armaments
    - Forbids AA type
    - Removed conversion from heavy turret
- Heavy two-man turret:
    - Added `-0.4` max speed
    - Added `+5%` soft and hard attack
- Heavy three-man turret:
    - Decreased max speed `-0.25 → -0.5`
    - Added `+10%` soft and hard attack
- Super heavy three-man turret:
    - Increased IC cost `+10 → +12`
    - Decreased max speed `-0.2 → -0.5`
    - Increased breakthrough `+24 → +35`
    - Increased hard attack `-10% → +15%`
- Super heavy four-man turret:
    - Decreased IC cost `+12 → +10`
    - Increased max speed `-0.5 → -0.2`
    - Decreased breakthrough `+35 → +24`
    - Added `+20%` soft attack 
    - Added `+20%` hard attack
- Modern turret:
    - Added `+15%` soft attack
    - Added `+15%` hard attack
##### Cannons
- Heavy MG:
    - Increased soft attack `+5 → +12`
    - Decreased hard attack `+2 → +1`
    - Removed build cost
    - Decreased piercing `+10 → +7.5`
    - Added `+6` breakthrough
    - Increased conversion cost `+0.5 → +1`
- Flamethrower:
    - Increased soft attack `+5 → +20`
    - Increased conversion cost `+0.5 → +1`
- Auto-cannon:
    - Increased soft attack `+15 → +24`
    - Decreased hard attack `+5 → +2`
    - Decreased piercing `+20 → +15`
    - Added `+2` breakthrough
    - Added `+1` steel
    - Increased conversion cost `+1.5 → +3`
- Auto-cannon 2:
    - Increased soft attack `+20 → +36`
    - Decreased hard attack `+7 → +5`
    - Decreased piercing `+35 → +30`
    - Added `+18` breakthrough
    - Added `+2` steel
    - Decreased max speed `-0.1 → -0.2`
    - Decreased reliability `-10% - -15%`
    - Increased conversion cost `+2 → +3.5`
- Anti-air cannon:
    - Increased air attack `+16 → +20`
    - Increased conversion cost `+2 → +4`
- Anti-air cannon 2:
    - Increased air attack `+32 → +40`
    - Increased conversion cost `+3 → +5`
    - Decreased reliability `-10% → -15%`
    - Removed `+2` steel
- Anti-air cannon 3:
    - Increased air attack `+43 → +53`
    - Increased conversion cost `+4 → +6`
    - Decreased reliability `-10% → -20%`
    - Removed `+3` steel
    - Added `+1` chromium
- Small cannon: 
    - Increased soft attack `+10 → +12.5`
    - Increased hard attack `+6 → +10`
    - Increased piercing `+25 → +30`
    - Decreased IC cost `+1.5 → +0.75`
    - Increased max speed `-0.15 → -0.1`
- Small cannon 2:
    - Increased soft attack `+15 → +19`
    - Decreased hard attack `+15 → +10`
    - Decreased piercing `+50 → +30`
    - Decreased IC cost `+3 → +1.5`
    - Increased max speed factor `-20% → -15%`
    - Decreased reliability `-10%→ -15%`
    - Increased conversion cost `+3 → +5`
- Close support gun:
    - Increased soft attack `+25 → +38.5`
    - Added `+9.5` breakthrough
    - Decreased max speed `-0.2 → -0.3`
    - Decreased reliability `-10% → 15%`
    - Increased conversion cost `+4 → +5`
    - Replaced `+1` steel cost with `+1` tungsten cost
- Medium cannon:
    - Increased soft attack `+20 → +22.5`
    - Decreased piercing `+60 → +45`
    - Removed `+2` breakthrough
    - Increased conversion cost `+3 → +5`
    - Removed steel cost
    - Increased tungsten cost `+1 → +2`
- Medium cannon 2:
    - Decreased soft attack `+32 → +25.5`
    - Decreased hard attack `+20 → +16.5`
    - Decreased piercing `+90 → +68`
    - Removed `+4` breakthrough
    - Increased conversion cost `+4 → +5`
    - Removed steel cost
    - Increased tungsten cost `+1 → +3`
    - Decreased reliability `-15% → -20%`
- Medium howitzer:
    - Increased soft attack `+35 → +45`
    - Increased hard attack `+1 → +3`
    - Removed `-2` breakthrough
    - Increased conversion cost `+4 → +6`
    - Removed steel cost
    - Increased tungsten cost `+1 → +2`
    - Added `+1` chromium cost
- Medium howitzer 2:
    - Increased soft attack `+45 → +51`
    - Increased hard attack `+2 → +6`
    - Removed `-2` breakthrough
    - Decreased reliability `-20% → -25%`
    - Increased conversion cost `+5.5 → +7.5`
    - Removed steel cost
    - Increased tungsten cost `+1 → +3`
    - Increased chromium cost `+1 → +2`
- Rocket launcher:
    - Increased soft attack `+35 → +66.5`
    - Decreased reliability `-10% → -20%`
    - Removed `-4` breakthrough
    - Reduced conversion cost `+5 → +4.5`
    - Increased tungsten cost `+2 → +3`
- High-velocity cannon:
    - Increased soft attack `+10 → +12.5`
    - Decreased hard attack `+26 → +20`
    - Increased piercing `+68 → +90`
    - Decreased reliability `-5% → -10%`
    - Increased conversion cost `+3 → +4`
    - Decreased steel cost `+2 → +1`
- High-velocity cannon 2:
    - Decreased soft attack `+20 → +15`
    - Decreased hard attack `+35 → +22`
    - Increased piercing `+125 → +135`
    - Increased reliability `-17.5% → -15%`
    - Increased max speed `-0.3 → -0.2`
    - Increased conversion cost `+5 → +7`
    - Decreased steel cost `+2 → +1`
    - Increased tungsten cost `+2 → +3`
- High-velocity cannon 3:
    - Decreased soft attack `+25 → +17`
    - Decreased hard attack `+45 → +40`
    - Decreased piercing `+200 → +188`
    - Increased max speed `-0.4 → -0.3`
    - Increased conversion cost `+7 → +9`
    - Decreased steel cost `+3 → +1`
    - Increased tungsten cost `+2 → +4`
- Heavy cannon:
    - Increased soft attack `+20 → +31`
    - Increased hard attack `+20 → +25`
    - Decreased piercing `+90 → +60`
    - Increased conversion cost `+6 → +7.5`
    - Increased chromium cost `+1 → +2`
    - Removed `+2` steel cost
- Heavy cannon 2:
    - Increased soft attack `+25 → +37.5`
    - Decreased hard attack `+35 → +27.5` 
    - Decreased piercing `+125 → +90`
    - Decreased reliability `-25% → -30%`
    - Increased conversion cost `+7 → +9`
    - Increased chromium cost `+1 → +2`
    - Removed `+2` steel cost
- Heavy cannon 3:
    - Increased soft attack `+30 → +42.5`
    - Decreased hard attack `+40 → +37.5`
    - Decreased piercing `+170 → +125`
    - Decreased reliability `-30% → -35%`
    - Increased conversion cost `+8 → +11`
    - Increased chromium cost `+1 → +2`
    - Removed `+3` steel cost
- Heavy howitzer:
    - Increased soft attack `+55 → +68`
    - Increased hard attack `+2 → +6`
    - Removed `-4` breakthrough
    - Increased conversion cost `7 → 8`
    - Increased tungsten cost `+1 → +2`
    - Increased chromium cost `+1 → +3`
    - Removed `+3` steel
- Super heavt cannon:
    - Increased soft attack `+35 → +51`
    - Decreased piercing `+225 → +188`
    - Decreased reliability `-35% → -40%`
    - Decreased tungsten cost `+5 → +3`
    - Increased chromium cost `+2 → +4`
##### Modules
- Radio:
    - Increased breakthrough `+15% → +25%`
- Radio 2:
    - Increased breakthrough `+30% → +50%`
    - Increased defense `+45% → +50%`
- Radio 3:
    - Increased breakthrough `+45% → +76%`
    - Increased defense `+65% → +75%`
- Secondary Heavy MG:
    - Increased IC cost `+1 → +2`
    - Increased soft attack `+3 → +5`
    - Increased hard attack `+1 → +2`
    - Removed `+1` breakthrough
    - Added `+3` defense
    - Reduced reliability `-5% → -7.5%`
- Secondary small cannon:
    - Increased hard attack `+3 → +6`
    - Increased IC cost `+2 → +4`
    - Decreased max speed `-0.25 → -0.3`
    - Decreased reliability `-10% → -15%`
    - Removed `+2` breakthrough
    - Decreased armor `-5% → -10%`
- Sloped armour reduced XP cost  `+10 → +1`
- Stabiliser:
    - Increased IC cost `+2 → +2.5`
    - Increased breakthrough `+5 → +7.5`
    - Added `+3` soft attack
    - Added `+3` hard attack
- Smoke launcher:
    - Decreased IC cost `+0.5 → +0.25`
    - Increased defense `+2 → +5`
    - Increased breakthrough `+1 → +2`
    - Increased reliability `-10% → -5%`
    - Removed `+2` breakthrough
    - Removed `+4` defense
    - Added `+10%` soft attack
    - Added `+10%` hard attack
    - Added `-10%` defense
    - Added `-10%` breakthrough
- Wet ammo storage:
    - Increased IC cost `+1 → +1.5`
    - Added `-10%` soft attack
    - Added `-10%` hard attack
- Squeezebore adapter:
    - Added `+5%` hard attack
    - Added `-5%` soft attack
- Armour skirts:
    - Increased armor `+2 → +5`
    - Decreased breakthrough `+3 → +2`
    - Increased IC cost `+0.5 → +2`
    - Added `+3`
    - Added `+5%` hardness
- Dozer blades: 
    - Increased IC cost `+1 → +1.5`
    - Added `+2` defense
    - Added `+2.5%` hardness
    - Added `-10%` max speed
- Autoloader:
    - Increased IC cost `+2.5 → +3`
    - Increased breakthrough `+4 → +6`
    - Removed `+4` defense
    - Added `+25%` soft attack
    - Added `+25%` hard attack
- Easy maintenance:
    - Increased reliability `+10% → +20%`
- Additional machine guns
    - Decreased defense `+2 → +1`
    - Increased IC cost `+0.5 → +0.75`
