# Saving Private Tryin' Historical MP Full Changelog

### 3.14.11 help

#### General
 - Reduced game speed 1 to 60 seconds per tick to mitigate unintended unpauses
 - Special project 'Jet Engines' now also requires research 'Experimental Rockets'
 - Research 'Experimental Rockets' Year 1942->1941
 - Special Project facilities have been returned to their vanilla IC build cost but are now affected by infrastructure level

#### Germany
 - MEFO Bills base monthly increase in Consumer Goods Factory factor: 3%->3.5%
 - Eisernes Sparen politlcal power cost 75 -> 50
 - Seize the Ukranian Grain harvest political power cost 100->75
 - Kreditkasse decision political power cost 200->100
 - Abolish the Hauszinssteuer political power cost 100->150
 - Steuergutscheine political power cost 100->150

#### Italy
 - Removed flame tank effects from focus 'Italian Tankettes' (avoiding a bug around special project progress >100%)
 - Focus 'Regional Development' time to complete reduced to 35 days, from 70
 - Focus 'Polizia della Africa Italiana' time to complete reduced to 35 days, from 70
 - Focus 'Strengthen Ascari Corps' time to complete reduced to 35 days, from 70
 - Focus 'Novus Ordo' time to complete reduced to 35 days, from 70
 - Focus 'Reorganize the Party' political power reward reduced to 50, from 100
 - Focus 'Economic Reforms' time to complete increased to 70 days, from 35
 - Focus 'Improve The Industries' time to complete increased to 70 days, from 35

#### Japan
 - No longer able to double dip on resource decisions targetting China

#### British Raj/India
 - Focus 'Government of India Act' time to complete increased to 70 days, from 35 days
 - Focus 'Work with Local Leaders' time to complete increased to 70 days, from 35 days
 - Focus 'Concessions to Industrialists' time to complete increased to 70 days, from 35 days
 - Focus 'Empower Provincial Authorities' time to complete increased to 70 days, from 35 days
 - Focus 'Curtail The Zamindars' time to complete increased to 70 days, from 35 days
 - Focus 'Expand the Zamindari System' time to complete increased to 70 days, from 35 days
 - Focus 'Reform the Agricultural Sector' time to complete increased to 70 days, from 35 days
 - Focus 'Local Recruitment Office' time to complete increased to 70 days, from 35 days
 - Focus 'Regimental loyalty' time to complete increased to 70 days, from 35 days
 - Focus 'Imperial Industry Initiative' efficiency cap reduced to 5%, from 10%
 - Focus 'Imperial Industry Initiative' efficiency growth reduced to 2.5%, from 5%
 - Focus 'Imperial Industry Initiative' now requires Industry and Tools level 3 techs
 - Focus 'The Great Recovery' factory output reduced to 5%, from 10%
 - Focus 'The Great Recovery' no longer grants civilian factories
 - Focus 'Lions of The Great War' special forces cap reduced to 10%, from 15%
 - Focuses 'The Dominion of India', 'Keep Calm and Carry On', and 'South East Asia Command' sub-branch removed
 - National spirit 'Congress Shipbuilding Effort' dockyard output reduced to 10%, from 15%
 - National spirit 'Congress Productivity Effort' factory output reduced to 7.5%, from 10%
 - National spirit 'Congresss Construction Effort' construction speed reduced to 5%, from 15%

### 3.14.10 'Grok, how do i make the Axis win?'

#### Map
 - Several Provinces in Burma and bordering states have been altered to be harder to defend
 - Properly updated map textures to display SPT's altered terrain (yes, you can finally see the gorgeous El Alamein Highlands)

#### Romania
 - Update focus 'Mobile Tank Destroyers' to vanilla (already unlocked Leonidas Works, now provides 2500 MIO funds)

#### Japan
 - Focus 'Defend The South Seas Mandate' time to complete reduced to 35 days, from 70
 - Focus 'Bulward on The Continent' time to complete reduced to 35 days, from 70
 - Focus 'Army Expansion Law' time to complete reduced to 35 days, from 70
 - Focus 'Dockyard Expansion' time to complete reduced to 35 days, from 70
 - Focus 'Starve The Archipelagos' time to complete reduced to 49 days, from 70
 - Focus 'Cruiser Modernization' technology bonus reward reduced to 100%, from 200%
 - Focus 'Attack the West on the Islands' now increases the duration of 'Tora! Tora! Tora!' national spirit by 90 days
  - Focus 'Larger Air Bases' now increases the duration of 'Tora! Tora! Tora!' national spirit by 90 days

#### British Raj
 - Focus 'The Great Recovery' requirement reduced to 35 owned civilian factories, from 40
 - National Spirit 'Recovering from the Great Depression' awarded by focus 'The Great Recovery' duration reduced to 550 days, from 1095 
 - Focus 'Rural Mechanization Program' technology bonus reduced to 50%, from 75%
 - Focus 'Ammunition Factory Khadki' no longer grants a military factory
 - Focus 'Cordite Factory Aruvankadu' no longer grants a military factory
 - Focus 'Ordnance Factory Kanpur' no longer grants a military factory
 - Focus 'Engineering Revolution' reward reduced to 1 military factory, from 2
 - Focus 'The Calcutta Line' now requires being at war with Japan to be taken

### 3.14.9

#### Industry
 - Can now switch between dispersed and concentrated industry per level.
 - Adds 10% Ship Refit/Repair boosts to conversion techs

#### Germany
 - Reworked 'Autarky' and related focuses.
   - Penalty for reaching 100% on MEFO Bills/Economy of Conquest removed (was: +10% Expected Consumer Goods, -20% Factory Output, -20% Dockyard Output)
   - Limit for MEFO Bills/Economy of Conquest raised from +100% to approximately +300% Consumer Goods Factory factor (this is a cap, not a goal, but we'd all love to see it)
   - Germany now starts with Hjalmar Schacht as advisor for free. He will be replaced with Walther Funk for free after mid-1938 by focus 'End the Charade', or removed by taking 'Prioritizing Economic Growth'
   - Focus 'Autarky Efforts' no longer limits Germany to a special trade law. However, Free Trade is locked (and would be replaced by Export Focus)
   - Focus 'Autarky Achieved' removed and replaced with new focuses to mitigate, but not eliminate, inflation
   - Focus 'Geräuschlose Kriegsfinanzierung' allows additional, somewhat more expensive options than Price Controls to reduce CGF
   - Subtree 'Form the Zentrale Planung' moved below 'Kriegsfinanzierung' and now requires war with the Soviet Union. All focus times reduced, and dockyard output bonuses transferred to factory output.
   - Focus 'Wirtschaftlicher Raubkrieg' allows Germany to continue fighting inflation by seizing key cities and exploiting Reichskommissariats in the western Soviet Union (these RKs should be more stable than in Vanilla and can be formed from allied occupation)
   
#### Navy
 - Unified core slot requirements across hull types. All Hulls now require Primary Armament, Engine and Armor (if applicable).
 - Battleships require front slot filled in addition
 - Carriers require all slots where a hangar dech can be fitted to be filled in addition
 - Added cruiser armor 0 module to freely fulfill armor requirements. Free to fit, very cheap to dismount.
 - Added 1 armor to cruiser armor 0/dds to circumvent divide by zero
 - Fixed designs to comply with these construction rules in all relevant nations
 - adjusted upper end of penetration damage curve to have more gradual drop between 50/10% pen. now with pen ratios of at least 2.00/1.00/0.75/0.50/0.33/0.20/0.10/0.00 you deal 1.00/1.00/0.70/0.40/0.30/0.20/0.10/0.05 times damage (added 0.33,0.2 thresholds with relevant damage mults)
 - addjusted supremacy so that being active in a zone now gives equal/more supremacy than strike force

### 3.14.8

#### Hungary
 - Swapped Fiat MIO to current Italian version (Standardized Production, not Fast Tank)

#### Japan
 - Spirit 'Tropedo Cruiser' removed +100% torpedo damage to torpedo cruisers
 - MIO trait 'The Zero' for Mitsubishi and Yokosuka now properly checks what MIO upgrade path the player has chosen
 - Focus 'Italian Exchange' now requires Italy being in faction with Germany to be taken, instead of requiring Italy to be at war with England
 - Occupation law 'Pan-asian Integration' fixed to apply to a wider variety of asian and pacific islander tags to prevent any oddities with its usage

### 3.14.7 Mr President, I told you it would come to this. I was right! Landon is taking over!

#### USA
 - Rework Landon
 - Focus "Build The Pentagon" now grants +5% max planning instead of +10% planning speed

#### Germany
- Spirit "MEFO bills" reduced civillian, army, airforce and navy intel reduction from -25% to -15%

### 3.14.6

#### British Raj
 - Political power gain per famine state penalty: -1% -> -3%
 - Stability per famine state penatly: -1% -> -3%
 - Famine small aid package effect halved
 - Ordnance Factory Board: PE Cap +10% -> +5%
 - Ordnance Factory Board: PE Gain +10% -> +5%
 - Focus 'Confer with the Congress' no longer gives Political Power
 - Focus 'Favor the Muslim League', 'The Indian Parliament', and 'Court the Princes' political power gain: 10%->5%
 - Independence Branch no longer available
 - Hid 'Burma Road' subbbranch due to it being impossible to take
 
#### Mongolia
 - Reduced cavalry buff in Golden Corp
 - Allow focus 'Annex Tannu Tuva' to be taken after focus 'End Isolation'

#### Soviet Union
 - Decision to annex AI Mongolia now includes Tannu Tuva

#### Japan
 - Focus 'Intensify Carrier Research' research and ahead of time penalty reduction tech bonuses reduced to 50% and 1.0 years AHoT respectively, from 100% and 2.0 years
 - National Spirit 'Finishing Maru 2 Keikaku' dockyard output reduced to 10%, from 15%
 - Focus 'Fighter Modernization' research bonus to fighters and heavy fighters reduced to 75%, from 100%
 - Focus 'Samurai Legacy' time to complete reduced to 35 days, from 70
 - State modifier 'Urban Development' construction speed bonus reduced to 5%, from 10%
 - Focus 'Invest In Urban Centers' state modifier duration increased to 200 days, from 150
 - Event 'Overseeing Production Quotas' efficiency cap (from challenging zaibatsus) reduced to 7.5%, from 10%
 - Focus 'Pan Asia Movement' no longer requires being at peace to be taken
 - Base 'Economic Decline' cg increase per 120 days increased to 1.0%, from 0.5%
 - Event 'The Price of War' now has a new option allowing for a denial of the increase in cg per 120 days, available only when the focus 'Allow the Zaibatsu to Help' has been completed
 - Event 'Solving The Grain Market Inflation' option B consumer goods added reduced to 1.0%, from 1.5%
 - Economy law 'Controlled Economy' civilian intel to others reduce to -20, from -35

### 3.14.5 

#### General
 - Misc 1.16.6 changes
   - Tank Destroyer brigades now have a +15% baseline piercing modifier
   - Easy Maintenance reliability 20%->10%, IC cost reduction 0%->7.5%
 - Ship Sonar 2 1939->1937
 - Changed AA CAS Damage reduction scaling. now linear to 90% reduction at 26.7 aa attack (was 75% at 10.8)
 - Research Years for Large/MK2 Air Cannons moved to 41/43 (-2 Years)
 - Jet Engines: Reduced Breakthrough point need by 1
 - Jet Engines: reduced Range Malus by 20% each

#### UK
 - Removed Focus "Coastal Command"
 - Focus "Fighter Command": Research Bonuses changed from 2x100 Light Airframe to 1x100 Light Airframe, 1x75 Aircraft

#### Spain
 - Automated Portuguese peace conference

#### Japan
 - 'Grain Market Inflation' should fire an appropriate number of times (1)
 - 'Controlled Economy' now correctly grants +10% resource gain when upgraded

### 3.14.4 'The Smallest Changelog for the Biggest Update'

#### General
 - 'Surface Raiders' Screening without screening 25%->12.5%
 - General tooltip update. These are NOT balancing changes!
    - State infrastructure construction speed modifiers should now say 'Infrastructure construction speed' instead of 'construction speed'
    - Soviet focus 'The Modern War in the Skies' now correctly displays night operations penalty reduction
    - Modifiers that affect the Air Superiority land battle bonus now state 'Air Superiority in-battle effect' for clarity
    - Reworded Army, Navy, and Military Leader Cost effects
 - Added Tutorial Info click overview of Balance changes

#### Navy
 - Changed Carrier limit to 6 before 50% per extra CV penalty

#### Special Forces
 - Reworked Paratrooper Doctrine tree
 - Paratroopers can no longer paradrop

#### Japan
 - Minor rework

#### Brazil
 - Focus 'The Washington Accords' is now available when in faction

#### British Raj
 - Occupation law 'Princely Subjugation' Resistance target 60% -> 20%
                                         Local factories 60% -> 20%
 - Add tooltip warning to focus 'The Indian Parliament'
 - Focus 'South East Asia Command' Special Forces Capacity Multiplier +25%->0%
 - Focus 'Free Abyssinia" Special Forces Capacity Multiplier +10%->0%
 - Focus 'Lions of the Great War' now adds idea 'Indian Special Forces': Special Forces Capacity Multiplier 15%
    - Army Experience 30->0
 - Going independent under 'His Majesty's Loyal Government' no longer partitions India

#### Denmark
 - Removed Burmeister & Wain trait 'Efficient Scrap Recycling' (the second one)
 - Reduced Focus 'Reclaim Norway' compliance 80%->60%
 - Reduced Focus 'Administrate Norway' compaliance 60%->40%

#### Germany
 - Focus 'Panzerschiff Raiders' Screening without Screens 10% -> 0%
 - Focusses "Dive Bombers"/"Form the Jagdwaffe" now grant BF 109 E Variant with no modules

###  3.14.3

 - Focus 'Princely State Donations' no longer triggers 'Fight Funds' event
 - Fixed button bug

###  3.14.2

#### General
 - Implemented 1.16.5
 - Added event notifying Axis powers when Britain takes focus 'Secure Iraq'
 - Paratrooper doctrine 'Combat Insertion' now available
 - Resealed King Tut's tomb due to unforeseen consequences

#### Brazil
 - Focus 'Secure our Borders' now sends a faction join request to the UK
 - Focus 'The Washington Accords' no longer bypasses if already in faction with US

#### British Raj
 - Reduced focus times on independence path (on top of 1.16.5 reductions)
    - 'A Congress Resurgent': 70 -> 35 days
    - 'India United': 70 -> 35 days
    - 'Cabinet Mission Plan': 70 -> 35 days
    - 'A Permanent Muslim Governmental Seat': 70 -> 35 days
    - 'Inclusive Nationalism': 70 -> 35 days
 - Focuses 'Holding the gates of india', 'Defense of burma', 'Fortify el alamein', 'The defense of hong kong', 'Defense of malaya', 'fortify aden', the aden protectorate':
    - Halved number of forts and anti-air given
    - Halved the duration of the state modifiers applied

#### Germany
 - Removed focus 'Demand Slovenia'

###  3.14.1

#### General
 - Implemented most of 1.16.2 and 1.16.3
    - Armored Car cost changes only
    - Tank cost and attack changes are not implemented
 - Set default host tool nation to Germany
 - King Tut's tomb has been properly unsealed

#### Australia
 - Focus 'Introduce Unconventional Warfare' no longer grants a Special Forces Branch Specialism. Time reduced from 70 -> 35 days.
 - Australia now has access to the 'Diversify Special Forces' decision

#### British Raj
 - Focus 'Defense of India Act' no longer cancels if War Support falls below 50%
 - Add Focus 'India Indivisible' under 'Tryst with Destiny'

#### France
 - Focuses 'Levee en masse' and 'Fortification Focus' now accept either of 'Firepower Kills' or 'Methodical Battle' as prerequisite
 - Focus 'Special Forces' now accepts 'Levee en masse' as prerequisite
 - Focus 'Fusiliers Marins' now accepts 'Grande Batterie' as prerequisite

###  3.14.0 Graveyard of DLC

#### General
 - Implemented Graveyard of Empires (as of v1.16.1)
 - Annexed new GoE puppets back into colonial overlords
 - Added decision to add/remove a convoy to force convoy recalculations

#### Brazil
 - Removed ability to have Lindolfo Collor and Minervino de Oliveira as both leader and advisor (again)

#### Bulgaria
 - Focus 'Illusions of a Non-Partisan System" no longer cancels if Democracy support falls below 20%

#### Denmark
 - Focus 'Reclaim Norway' compliance should now be working (?)

#### Germany
 - 'Second Vienna Award' Days 35 -> 14
 - No longer guarantees Finland 

#### Hungary
 - Focus 'Demand Burgenland' now available
 - Focus 'Demand Southern Slovakia' removed
 - Focus 'Claim Overlordship of Slovakia' Days 70 -> 35
 - Now can core the Second Vienna Award states via decision 
 - Focus 'Fighter Competition' Days 70 -> 35 and no longer fires the event

#### Italy
 - 'Trade Vojvodina for Guarantees' now includes West Banat and cost 75 -> 10

#### Spain
 - Now can manually complete 'Unify the Nationalist Front' in case of a skill issue

#### South Africa
 - Historical flavor event on the replacement of Prime Minister Hertzog with Smuts now fires immediately upon declaration of war

#### USA
 - 'Escort Fighters' cost 70 days -> 35 days bonus 100% -> 150%
 - 'Neutrality Act' war support reduction removed
 - Focus 'Soviet Aid' Soviet Union capitulation progress reduced to 35%, from 40%
 - Focus 'Soviet Aid' now grants 20k guns, 2k artillery, and 2k support equipment, from 10k, 1k, and 1k respectively
 - National spirit 'American Aid' now grants +10% surrender cap for the Soviet Union

###  3.13.7 Another Week another minor UpdatE

#### General
 - Infantry Tank MIO speed fixed
 - Make Static AA Air superiority reduction per level 25 (was 5). Still requires at least 1 active wing in airzone to apply properly.
 - Land/Navy/Air Facility: -2000 IC base Cost, +2000 IC incremental cost
 - Base bonus to attack from CAS in battles now 20% (was 25%)
 - Air superiority bonus base now 25% (was 35)
 - Reduction by AA increase, base 25% now cancelled out at 80 Division AA (was at 112)

#### Germany 
 - Focus 'Ruhr Dam' now accessible from Autarky
 - Advisor 'Ludwig Erhard' added 10% civ construction speed
 - Focus 'Totaler Krieg' now requires total mobilisation

#### Soviets
 - Focus 'Superior War Machines' no longer requires improved medium chassis

#### South Africa
 - Removed Barotziland and Northeast Rhodesian cores on formable
 - Added decision to take control of Mozambique

#### Naval designer
 - Added "Helicopter Facilities" module. Uses catapult slotting rules. Better sub detection, worse surface detection, built in depth charge attack instead of air attack compared to catapults. Gained from helicopter special project.

#### Air designer
 - 1924 Airframe IC cost reduced from 4 to 1
 - 1936 Airframe IC cost reduced from 5 to 2
 - 1936 Airframe gains additional support module slot (was 2, now 3)
 - Turret Modules now give 2 Air Attack and 1 Air Defense per weight, and -2.5% Speed per turret (was 1/1/-3,75%)
 - Armor Plates Unified at 1.5 Air defense per Weight (was 2/1/0.8 for light/medium/heavy airframe)
 - AP Bomb Locks: Renamed to Multipurpose bomb locks. Ground attack damage increased to 8 (was 2). Still less weight-efficient than regular locks and equal to bomb bays.
 - Heavy Bomb Locks: Ground attack damage increased to 10 (was 8). For being a later tech now actually more weight efficient for CAS damage/weight than small bombs.
 - Bomb Locks & Multipurpose Bomb Locks: added 1 strat bombing when on strat bombing mission
 - Heavy Bomb Locks / Small Bomb Bay: added 2 strat bombing when on strat bombing mission
 - Heavy Bomb Locks now allow for strat bombing
 - Medium Bomb Bay: Increased strat bombing from 6 to 7
 - Bomb Sights / Air to ground radar: decreased flat strat bombing buff in exchange for % modifier


#### Tank designer
 - Tank destroyer combat width increased to 3 from 2
 - Standardized Buffs and Debuffs with Self-Propelled Artillery (Supply Consumption, Recovery Rate, HP, Breakthrough, Stats Multipliers)
 - High Velocity Cannon: Soft Attack Reduced to 8 from 10
                         Hard Attack Increased to 25.5 from 22.5
 - High Velocity Cannon II: Soft Attack Reduced to 10 from 12
                            Hard Attack Increased to 32 from 28
 - High Velocity Cannon III: Soft Attack Reduced to 14 from 17
                             Hard Attack Increased to 35 from 30
- Super Heavy Cannon: Soft Attack Reduced to 49.5 from 51
                      Hard Attack Reduced to 44 from 45

#### Air Technologies
 - Survivability Studies now 1937 technology
 - Aircraft Cannons 1 now 1938 technology

#### Artillery Technologies
 - Improved Artillery II: Increased Self-Propelled Artillery Soft Attack to +10% from +5%
 - Anti-Tank Upgrade: Increased Tank Destroyer Piercing to +5% from 0
 - 1940 Anti-Tank: Added Tank Destroyer Hard Attack +10% from 0

#### Army Command
 - Inventive Leadership: Planning Speed Increased to +15% from +10%

 - Bayonet Strength: Infantry Attack Reduced to +10% from +15%
                     Infantry Defence Reduced to 0 from +15%
                     Recovery Rate Increased to +10% from 0%

 - Professional Officer Corps: Daily Command Power Gain Reduced to 0 from +0.25

 - Elevated Engineering Corps: Entrenchment Speed Reduced to 0 from +10%
                               Railway Gun Bombardment Reduced to 50% from 100%

 - Quick Improvisation: Planning Speed Reduced to 0 from +50%

 - Proper Heritage: Recon Reduced to 0 from 25%
                    Cavalry Attack Bonus Reduced to +15% from +25%
                    Cavalry Defence Bonus Reduced to +15% from +25%

 - Ideological Loyalty: Weekly Manpower Reduced to 0 from +500
                        Encirclement Penalty Reduction Reduced To +7.5% from +10%

 - State Serves The Military: Political Power Gain Increased to 0% from 10%

 - Motorization Drive: Motorized Attack Reduced to 10% from 15%
                       Motorized Defence Reduced to 10% from 15%
                       Supply Truck Attrition Reduced to 0 from +20%

 - Overwhelming Firepower: Supply Consumption Penalty Reduced to 0 from 5%

 - Tip Of The Spear: Paratrooper Supply Grace Reduced to 0 hrs from 72 hrs
                     Marine Supply Grace Reduced to 0 hrs from 72 hrs

 - Static Warfare: Org Loss When Moving Penalty Reduced to 0 from +15%
                   Entrenchment Speed Reduced to +15% from +25%
                   Max Entrenchment Reduced to +15% from +25%
                   Land Fort Effectivness Added +10%

 - Flexible Organisation: Org Loss When Moving Reduced to -15% from -10%
                          Max Planning Penalty Reduced to 0 from -5%
                          Planning Speed Increased to +15% from +10%
                          Prefered Tactic Selection Cost Bonus Reduced to 0 from -20
                          Army Speed Reduced to 0 from +5%

 - Aggresive Recon: Infiltration Assult Tactic Selection Bonus Reduced to 0 from +200%
                    Supply Consumption Penalty Reduced to 0 from +5%
                    Reconnaisance Redued to 0% from +50%

 - Victory or Death: Encirclement Penalty Reduction Increased To +7.5% from +0%
                     Attack Bonus Reduced to 0 from +10%
                     Defence Penalty Reduced to 0 from -20%

 - Maneuver Warafare: Supply Truck Attrition Reduced to 0% from +15%
                      Non-Combat Out of Supply Penalties Reduced to 0% from +10%
                      Coordination Reduced to +10% from +20%
                      Supply Consumption Reduced to 0 from +10%
                      Army Speed Increased to +7.5% from 0
                      Coordination Reduced from +20% from +7.5%

 - Smoke and Fire: Supply Consumption Reduced to 0 from +15%
                   Division Defence Reduced to 0 from +5%
                   Artillery Attack Reduced to +25% from +30%

 - Logistical Focus: Navy Fuel Consumption Reduction Reduced to -10% from -20%
                     Air Fuel Consumption Reduction Reduced to -10% from -20%
                     Army Fuel Consumption Reduction Incresed to -10% from 0%
                     Supply Consumption Recuction Reduced to 0 from -20%
                     Supply Combat Penalties on Core Territory Reduction Reduced to 0 from -10%

 - Operational Reserves: Reduced HP bonus to +10% from +15%
                         Reinforce Rate Penalty Removed

#### Superior Firepower Doctrine
 - Integrated Support: Self-Propelled Artillery Added Recovery Rate +0.2 from 0
                                                Added Organisation +3.0 from 0

 - Regimental Combat Teams: Self-Propelled Artillery Added Soft Attack +10%
                                                     Added HP +5

 - Dispersed Support: Tank Destroyer Added Recovery Rate +0.2 from 0
                                     Added Organisation +3.0 from 0
                      Support Companies Added Recovery Rate +0.1
                                        Added Organisation +5
                                        Added Hard Attack +25%

 - Regimental Combat Teams: Tank Destroyer Added Hard Attack +10%
                                           Added HP +5%
 - Mechanized Offensive: Stats bonuses now equal with mechanized offensive in GBP/MW. Removed 10% Armor Breaktrough.
 - Concentrated Fire Plans & Centralized Fire Control: Modifiers swapped
 - Centralized Fire Control: Added +2% reinforce rate
 - Forward Observers/Combined Arms: Swapped Sides.
 - Forward Observers: Added 10% Army Breakthrough.
 - Combined Arms: Added 10% Armor breakthrough
 - Advanced Firebases/Tactical Control: Swapped Sides.
 - Tactical Control: Now has modifiers of old Advanced Firebases
 - Advanced Firebases: Now has 5% soft/hard on inf/mot/mech & artillery (Tactical Control in its position was +2% reinforce rate)
 - Shock and Awe: Removed 5% soft/hard on inf/mot/mech & artillery

#### Mass Assault Doctrine 
 - Large Front Operations: Tanks Added +2 HP
                           Added Max Planning +5%

 - Operational Concentration: Reinforce Rate Decreased to 4 from 5

 - Mechanized Wave: Armoured Car Recon Removed Organisation to Infantry
                    Light Tank Recon Added 1+ Organisation to Tanks
                    Tanks and Armor Variants Increased Organisation to 3 from 2

 - Continous Offensieve: Reinforce Rate reduced to 0 from 5

 - Infantry Offensive: Reinforce Rate reduced to 0 from 5

 - Human Wave Offensive: Reinforce Rate reduced to 5 from 8

#### Battlefield Support Doctrine
 - Direct Ground Support: Decreased ground support modifier from +20% to +15%

### 3.13.6

#### Soviets
 - Fixed Iran focus

#### Germany
 - Limited convoy to cruiser decision to 5 clicks
 - 'Trade with Sweden' removed
 - 'Operation Weserbung' civilian factory shipping mechanic now works
 - 'Demand Sweden' now provides resource rights for both states
                   35 -> 70 days

### 3.13.5a

#### UK
 - 'Home Defence' time 70 -> 35
 - 'Prepare for the Inevitable' time 35 -> 70
 - 'Global Defence' time 70 -> 35
                    war support 0 -> 2.5
 - 'Naval Rearmament' dockyards 8 -> 3
                      xp 50 -> 30
 - New focus 'Focus on Naval Rearmament' Added
 - 'Britannia Rules the Waves' time 70 -> 35

### Infantry Tank MIO
 - Traits moved to unhide Merge Plant Trait
 - Speed -5% -> -10%
 - Adaptable Turret Ring 5% piercing -> -5% speed
 - Anti-Tank Role hard attack 10% -> 5%

### 3.13.5 'Twilight of the Game Stability'

#### General
 - Axis Armour Pack warning added
 - United the Baltics
 - Iran and Afghanistan annexed in to Middle Eastern Trade Federation
 - Added additional automation to Japanese decision "Hakkō Ichiu"
 - If in the Allies, Mexico and/or Brazil joins all British wars, namely the war against the European Axis
 - Add Pacific Front tutorial tips to Brazil and Mexico
 - Training limit increased to 1M
 - Updated Infantry Tank MIO to vanilla

#### Navy
 - Reduced all Concentrated Industry dockyard output 15% -> 12.5%
 - Increased all Dispersed Industry dockyard output 10% -> 12.5%
 - Reduced convoy cost from 70 -> 65 IC
 - +25% to sub Hull costs
 - Reduced raiding area capability per taskforce by 33%
 - Added Destroyer Escort special project, cheaper shittier destroyers
 - Destroyers can now carry 2 sets of Hydrophones
 - +2 Sub detection to both tiers of Sonar. Second sonar tech made 1939 tech.
 - Radio Navigation: Surface, Sub Detection moved from mission to general stats
 - Radio Navigation II: Surface, Sub Detection moved from mission to general stats

#### Special Projects
 - Proximity fuse is now completeable in land or navy facility
 - Radar project can only be done once
 - Panzerschiffe are now Special Project

### Allies
 - 'Disrupted Shipping Routes' national spirit air and navy fuel consumption buffed to -10%, from -15%
 - Africa front allies debuff: Tier 2 Attack modifier against Germany/Italy -5% -> 0%
                                      Defence modifier against Germany/Italy -5% -> 0%
                                      Army attrition rate 0% -> 3%
                               Tier 3 Attack modifier against Germany/Italy -10% -> -5%
                                      Defence modifier against Germany/Italy -10% -> -5%
                                      Army attrition rate 0% -> 3%

#### Germany
 - Anschluss army strength requirement now starts ticking down after January 1st 1937 instead of November 5th 1937
 
#### Soviets
 - Focus 'Preemptive Invasion of Iran' Time 35 -> 14
                                       No longer makes Iran a Puppet
                                       Now directly transfers states 'Tibriz', 'Gilan', 'Tehran', 'Khorasan' to Soviets and 'Khuzestan', 'Fars' to UK 
 - Removed recurring Stalin Admiral decision due to lag
 - Intelligence Angency operation 'Prepare Collaboration Government' Increased Cost by 100% to compensate for single nation baltic
 - Decision 'Send Ultimatum to Latvia' Political Power cost 75 -> 175 (Compensate for single nation baltic)

#### Finland
 - Added decision to allow sending volunteers after the Soviets are near capitulation

#### Netherlands
 - Removed faction check for Malaysia in focus 'The Singapore Conference'

#### UK
 - Focus "Naval Rearmament" grants 5 more dockyards.

#### Denmark
 - Nerf Danish naval tree
 - Focus 'Administer Norway' compliance should now be working

#### Hungary
 - Focus 'Join the Axis' is now available even if fucked over by German deals
 - 'Restrict Voting Rights' time 35 -> 70
 - 'Act of Defence' time 70 -> 35
 - 'Wherever the Cross Points' time 70 -> 35
 - Made Slovakia always accept annexation 

#### South Africa
 - Added historical flavor event on the replacement of Prime Minister Hertzog with Smuts

#### Mongolia
 - Added Super-Heavy Railway Gun production cost decrease to idea 'Streamlined Artillery Production'

#### Romania
 - Added Super-Heavy Railway Gun production cost decrease to idea 'Karl Manufacturing Plant'

#### Mexico
 - Added new decision 'Support the Republicans' in the Spanish Civil War from vanilla, as a source of early Army and Navy XP

#### Transport Planes
 - 1940 
    IC 50 -> 40
    Range 1400 -> 1500
 - 1945
    IC 50 -> 30
    Range 1800 -> 2000
    Speed 480 -> 500

### 3.13.4 "Python"

#### General
 - Topbar Resources updated (thanks Lennard)

#### Germany
 - Trade deal with Sweden returned to old mechanics

#### Japan
 - Cleaned up tooltip for Focus 'The Zero'

#### USA
- 'Air Support' localisation cas -> fighter 

#### Hungary
- 'Legacy of the Black Army':
    Org 10% -> 5% 
    Cavalry attack 5% -> 2.5%
    Cavalry defence 10% -> 5%
- 'Heirs of the Huns' reductions: 
    Supply consumption 5% -> 2.5%
    Cavalry attack 5% -> 2.5%
- 'Expand the Honvedseg' pop 1% -> 1.5%
- 'Make the Magyar Légierö Known' 
    Doctrine 50% -> 30% 
    Air XP now 15 -> 50
- 'Develop the Weiss WM-21 Sólyom' 3x15% -> 2x50% 
- 'Quantity over Quality' research 25% -> 50%
- 'Anounce the Györi Program' production bonus uses 2 -> 1
- 'Restrict Voting Rights' time 70 -> 35
- 'Promote Hungarianism' time 70 -> 35

#### Romania
- 'Demand Transnistria' time 7 -> 35
- 'Expand the Galati Shipyards' dockyards 2 -> 3 and prioritises Northern Dobruja

### 3.13.3 "Where were you when mod was fix?"

#### General
 - Added Land and Naval Warfare facility variants of the "Radar" special project, so that countries are not railroaded into building the Air Warfare facility
 - Fixed early truck tooltip
 - Performance and stability improvements (confirm)
 - Armoured maintenance III recovery made vanilla

#### Germany
 - Autarky requirements now can be met by Germany, subject or allied countries

#### Soviets 
 - 'PC of Mechanical Engineering' Cap 0% -> 2.5% and tooltip fixed 
 - Added a decision to annex AI Mongolia 

#### Siam
 - Focus 'Train Development' train research bonus reduced from 300% to 100%
 - 'Infantry Equipment Development'  tech boost now works for infantry equipment

#### Manchu
 - 'Develop Manchukan shipyards' now adds 'Overworking dockyard workers' spirit
 - 'Embrace the Opium Trade' stability -10% -> -5%
 - 'New Chinese Economic Policy TM' recruitable population -30% -> -10% 
 - Happier Baba noises 

#### AI
 - Siam should no longer join Axis

### 3.13.2 "Projects as special as PDX balance"

#### General
 - Fixed Austria and Germany Historical AI focus orders
 - Disabled ahistorical Spanish Civil War event options
 - Made some focus trees look better
 - Performance and stability improvements?
 - Reduced breakthrough gain from tech to 75% of Vanilla
 - Incorporated naval module balance changes from 1.15.2
 - Improved the Fast Tank Designer MIO
    - "Improved Boogies" speed +2% -> +5%
    - "Improved Ventillation" breakthrough +5%
    - "Improved Tracks and Suspension" speed +5% -> +10% 
    - "Sloping Armor" armor +5%
    - "Lighter Materials" Production Resource Penalty Factor -10% -> Reliability +5%
    - "Enlarged Breech" hard attack +5%
    - "Quality Assurance Routines" reliability +5% -> Production Resource Need Factor -10%
    - "Streamlined Production" Production Efficiency Gain Factor +5%

#### Special Projects
 - Land cruiser: Base Hull IC cost x2, Module IC cost x5
 - Superheavy Railway Gun: -25% Damage, +50% IC cost.
 - Mothership Aircraft: 190/60/44 ATK/DEF/AGI to 100/45/40 ATK/DEF/AGI
 - Some project unlocks moved from start of game/1924 tech level to 1936 techs

#### UK
 - 'Operation Fork' is now available if Norway does not exist

#### Germany, Main Character of WW2
 - Removed "Diversify Special Forces" decision
 - Fixed 'Recovering Economy' not receiving the +75% consumer goods modifier it should have
 - No longer capable of removing 'MEFO bills' spirit through decision
 - Trait 'Der Fuhrer' no longer grants production efficiency cap
 - Trait 'Der Fuhrer' no longer grants construction speed
 - National Spirit 'Recovering Economy' now grants 5% expected consumer goods
 - Returned 'Second Vienna Award'

#### France
 - Removed "Diversify Special Forces" decision

#### Hungary
 - Removed army and manpower requirements from focus 'Claim Overlordship Over Slovakia'
 - Reverted reward of focus 'Reaffirm Territorial Claims' to Death or Dishonor version (cores + 1 claim on Banat)
 - Removed the demands branch while events are worked on

#### South Africa
 - Focus 'Secure Interests in Africa' now grants benefits immediately instead of requiring event decisions
 - Focus 'Secure Interests in Africa' now has anti-exploit checks for state control

#### Manchukuo
 - States transfered by 'Return of The Qing' focus/events no longer retain Pan-Asian Integration state modifiers


### 3.13.1 "Holy crap lois, that's a dlc"

#### General
 - Updated the mod to work with the new Götterdämmerung DLC
 - Several Nuclear Special Project focus rewards reduced and/or rebalanced
 - 'Assault Gun Manufacturer' MIO type now has access to multiple tank-focused policies it previously lacked

#### Japan
 - 'Bushido Spirit' trait infantry attack bonus reduced to 10%, from 20%
 - 'Bushido Spirit' trait breakthrough bonus reduced to 20%, from 25%

#### USA
 - Focus 'Tank Experiments' time to complete reduced to 35 days, from 70
 - Focus 'Tank Destroyer Board' time to complete reduced to 35 days, from 70
 - Focus 'Main Battle Tanks' time to complete reduced to 35 days, from 70

#### UK
 - Focus 'Every Man Will Do His Duty' time to complete increased to 70 days, from 35
 - Focus 'Every Man Will Do His Duty' spawn-in division count doubled
 - Focus 'Every Man Will Do His Duty' spawn-in division template changed to 12 width, from 14
 - Focus 'Every Man Will Do His Duty' spawn-in division template changed to irregular infantry, previously infantry

#### Navy
 - included PDX balance changes with buffs to Sonar detection, Depth charge module damage and reduction in Range for sub 1/2
 - brought new Sub Hull Slots inline with existing changes

### 3.12.11 "The Not Biased Update"

#### AI
 - Added Manchukuo AI to complete all industry focuses

#### Army
 - Nerfed armoured cars stats
 - Added a modifier to hills and desert for armoured cars 

#### Navy
 - Reduced dd tankiness

#### Mexico
 - 'Army Expansion Program' now gives two mils per state

#### Hungary
 - Removed division requirements for 'Claim Overlordship of Slovakia'
 - Can no longer refuse the Molotov-Ribbentrop Pact if called upon

#### Bulgaria
 - Fixed Foreign Company decisions availability when becoming Germany's subject

#### Finland
 - Remove advisors that can never be bought 

#### Japan
 - Triparte Pact guarantees now removed in January 1942
 
#### Manchu
 - Made focus positions make more sense
 - Fixed Early Destroyer localisation

### 3.12.10 "Twilight of the Mod Devs"

#### General
 - Added additional automation to Japanese decision "Hakkō Ichiu"
 - USA joins the Allies immediately upon Japanese DoW
 - USA joins all British wars, namely the war against the European Axis

#### Navy
 - Converted carrier can now retain modules of source ships, allowing for Hybrid designs, wich will behave as Carriers.
 - Added two AA/Secondary only slots to dedicated Carriers.
 - Naval Spirit: Night fighting: returned 5% visibility reduction. when other spirits were rebalanced, it was left at original nerfed state. now thatother spirits are stronger, this should return it into consideration.
 - Naval Spirit: Suprise Attacks: Removed 30% Naval coordination Boost, added automatic opportunity to disengage after initial combat, as a chance to take advantage of a spotting advantage with smaller fleets.
 - Naval Spirit: Inclement Weather experience: Removed weather effect modifiers (possibly not applying). Added +10% Naval Hit chance.
 - Removed visibility/availability of minelaying techs
 - Added Naval Doctrine "Tech": CAG night operations. Independent of doctrine tree, costs air XP. Allows for carrier play without blocking slot for air spirits.

#### Tanks
 - Amphibious Tank Chassis IC cost increased to 6, from 4.5
 - Amphibious Tank Chassis can no longer use Light Tank Turrets
 - Amphibious Drive added IC cost multiplier of +10%
 - Dozer Blades entrenchment reduced to 1, from 1.5
 - Dozer Blades defense reduced to 8, from 10

#### Air
 - ~~Made Medium Navs classified as naval patrol bombers, possible~~ Reverted, causes crash without defineable error
 - All-Weather AIr advsor now gives 2/4/6% Buff to air mission efficiency instead of possibly not applying -10/-20/-30 weather% penalty
 - CAG Night Fighting spirit removed
 - Made Medium Navs, classified as naval patrol bombers, possible
 - Guided ASM +5 Naval Targeting
   
#### Army
 - Pioneers now get affected by engineers research
 - Pioneers: Jungle specialists defense boost brought inline with regular engineers
 - Support Rocket artillery now counts as support artillery for purposes of special forces doctrine modifiers
 - Armored cars stats increased to ~equal those of equal ic light tanks
 - Armored car tech levels moved to 1914/1936/1940 (was 1914/1940/1942)

#### Japan
 - "Alliance with Siam" grants 100% compliance when annexing AI Siam, instead of cores

#### Bulgaria
 - Focus "The Path Towards a Greater Bulgaria" no longer increases your economy law past Partial Mobilization, rewarding 150 political power instead if you already have reached it
 - Fixed Italian MIO availability when becoming Germany's subject

#### UK
 - Removed decisions "Invade Ireland", "The MacDonald Proposal", and "Invoke the Alliance of 1373"
   
### 3.12.9

#### General
 - Increased score in peace conferences
 - Added Mexico to host tool 
 - Super Heavy Tanks now can only use Super Heavy Turrets

#### USA
 - SPT version of operation "The Greenland Patrol" added to account for fascist Denmark route. Available from when Denmark joins the Axis until the USA is at war with Germany

#### Raj
 - 'Great Indian Peninsula Railway' 70 days -> 35 days
 - 'East India Railways' now prioritises Bengal

#### Mongolia
 - 'Motorise the Army' now adds early truck tech and always adds 1000 trucks to stockpile

#### Denmark
 - Foci 'Seize Power' and 'Ask for Support' are no longer bypassed by being fascist, ensuring the leader change takes effect

#### Italy
 - Leader BoPs should now correctly activate only when the Mediterranean BoP is not active 

#### Brazil
 - Ported vanilla change to Potenji Conference to ensure Brazil joins the existing war rather than declaring

### 3.12.8 "Missing Bracket"

#### General
 - Made 4 speed, 2 speed and 1 speed slightly faster

 - Updated rules on paratroopers
 - Fixed error causing some straits to not activate
 - Fixed error causing some straits to not activate
 - Brazil now has a decision to annex AI controlled Mexico
 - Embargos now require targeted country to generate 50 tension
 - Democracies no longer have embargo tension requirement lowered by 50%

#### Army Spirits
 - Added 'Accomplished Heritage' which grants medal cost -90%
                                 field officer promotion cost -90%
 - 'Flexible Organisation' reduced max planning malus to 5% from 10%
                           reduced org loss when moving bonus to 10% from 20%
                           reduced planning speed bonus to 10% from 20% 

#### Mexico
 - Gulf Coast Naval Yards and Pacific coast yards now give 1 more slot and dockyard

#### Soviet union 
 - Focus 'Superior War Machines' time to complete reduced to 56 from 70
 - Focus 'The Means To Wage War' time to complete reduced to 56 from 70
 - Focus 'PC Of Mechanical Engineering' time to complete reduced to 56 from 70
 - Fix issue where 'New Economic Plan' would lock lower export laws

#### Germany
 - Focus 'Integrate War Economies' Grants 2 fewer mills per accepted country for Germany
                                   Grants spirit 'Integrated War Economies'
                                   Now applies to Bulgaria
 - Added focus 'Standardization Program' which upgrades spirit 'Integrated War Economies' for the minor powers
                                         Grants smaller version of 'Integrated War Economies' for the Germany and Italy
 - Focus 'Align Romania' time to complete reduced to 14 days from 35
 - Focus 'Align Hungary' time to complete reduced to 14 days from 35
 - Focus 'Install Collaborationists in Poland' can no longer be taken after Poland is annexed, in the event a major Allied skill issue allows Poland to go to peace conference

 #### Denmark
 - Reduced "Administer Norway" from full cores to 80% collaboration & 30% resistance
 - Events annexing Norway no longer transfer democratic Norway's troops
 - Clarified effect of Pan-Scandinavian decisions in focus tooltip
 - Reduced bonus steel relative to vanilla by -36 to limit civ boosting potential

##### USA & UK
 - If country has specific radar tech unlocked, it will now also unlock for malaya and philippines (updates monthly)

#### Japan 
 - Spirit 'Tora Tora Tora' increased CV Plane DMG/Tageting/Agility Buff to 25% from 12%
                           Removed 50% overstacking penalty reduction. 
 - Added cores to Siam and Indochina when annexed as AI

#### Navy
- Regular heavy cruiser battery damage increased: Tier I   to 9 from 6
                                                  Tier II  to 12 from 8
                                                  Tier III to 15 from 10
                                                  Tier IV  to 18 from 12
(buffed to offer more dmg at their lower pierce point than heavy gun equivalents at higher pierce)

- Panzerschiff: Range reduced to 5000 from 7500
                Speed increased to 26 kn from 27kn
                Module Slot 1 may now fit Fuel tank (was just AA)
- Submarine 3 Speed reduced to 16 from 18
              Center slot can now also fit AA (was just snorkel/radar)
              Hull Cost Reduced to 420 from 42000
- Reenabled Submarine engine 3
- Submarine Torpedo tubes are now researched with torpedo launcher technology tree (was submarine hull technology tree)
- Cruiser Sub : Range reduced to 4000 from 4750, 
                Fuel tank availability moved from slot 1 to dedicated slot option shared with AA

- Fuel tanks: now increases range by 50% from 1000km
              Percentage cost modifier decreased to 10% from 25%
- Torpedo: Weapon hit profile reduced to 110 from 120 (vanilla 100)
- Wings launched Penalty % per Carrier over 4 reduced to 15% (was 20%)

#### Navy Spirits
- Spirit of Naval Command: Decisive Battle: Now availeable regardless of Doctrine
- Added 'Swift Response' new Spirit of Naval Command which grants: +25% Escort and Screening efficiancy
                                                                   +5% Damage
                                                                   +10% Spotting Speed and Sub Detection
                                                                   +20% convoy retreat speed
                                                                   +15% naval speed
                                                                   -25% Strike force Org loss
                                                                   Only available with 'Fleet in Being'

#### Navy Doctrine
- Floating Fortress Doctrine Point (all doctrines): Now grants +10 org to Battlecruiser 
- Massed Strikes Doctrine Point (Base strike): Replaced -20% overcrowding penalty with +20 Heavy Cruiser org
- Carrier Battlegroups Doctrine Point (Base strike capstone): Now grants +10 org to Battleships  
                                                              Now grants 10% CV Plane Damage 
                                                              Now grants -20% Strike force org loss 


### 3.12.7  'The return of Python'

#### General 
 - Reworked air zones Tobruk, Egypt and Upper Nile

#### India
 - Ishapore arsenal focus reduced to 56 days from 70

#### New Zealand
 - Expand the NZPAF - Removed subsidy, added air Experience +50 and 1x 50% reduction to air doc

#### Germany
 - Heavy water production decision: Number of research bonuses reduced from 2 to 1
                                    Research bonus reduced from 200% to 100%
                                    Time to complete decreased forom 365  to 160 days
                                    Added cost of 4 civs whilst active.

#### Australia
 - Useless railway focus now gives 1 infra in 2 states

#### Soviet Union
 - Removed random -25% Aircraft designer cost from "Expand the Aircraft Industry"

#### Italy
 - Specialization focus Removed
 - Standarization focus path changed 
 - Made long range and multi role aircraft mutually exclusive, Added 5% reduction to aircraft
 - Multi role aircraft focus removed air template cost and added 1 x 75% research boost for air 

#### Spirits 
 - Air spirit material destruction removed designer cost and added light aircraft research speed 10% and reduced Tactical bomber research from 25% to 20%
 - industrial destruction had large plane airframe design removed

### Romania
 - Expand the University of bucharest focus now continues when requirements are not met
 
### Germany 
 - Begin heavy water production now requires Telemark to be controlled by the axis while the decision is active - reduced time taken to 160 days, Reduced boost to 1x 100% boost and costs 4 civs during the time.  
 
#### USA
 - Alf Landons focuses requiering senate support no longer cancel when due to dropped senate support (now same as Roosevelt)
 - Fix issue where 'Defend the Seas' would spawn dockyards inland
 - National Spirit 'Temporary Relief' now removes if National Spirit 'The 1937 Recession' is removed

#### Navy
- Improved destroyer guns (pen, DMG)
- Improved CA guns (pen)
- Improved BB/C guns (pen, DMG)
- Unified secondary speed modifier (all mow at -2% except for 4th tier)
- basic Dp now availeable with 36 light guns
- SHBB guns now type Heavy Gun Slot Module, and SHBBs now fit all heavy guns
- SHBB Hull Ic Cost 5500->6000
- added secondary 3
- added plane catapult 3
- plane catapults now provide small amount of aa
- 1936/40 plane catapults now require the light airframe of the same year to research
- all DD engine speed mod modifier increased by 5%
- DD base speeds now 32;33;34;35 (was 32 flat)
- Sonars now reduces torpeedo damage
- BC Armor: Armor reduced, speed bonus increased
- Cruiser Armor 3/4: Armor increased, now makes ship capital ship
- Torpedo Cruiser Tech: Increases Cruiser Torpedo damage to bring torp attack per ic for cruisers closer to destroyer levels
- Panzerschiff: Build Cost 3500 -> 2700, Speed 2 -> 27, Visibility 22 -> 20, availeable as 36 cruiser subtech for all nations
- Changed damage and piercing modifiers on shell tech.
- Adjusted Convoy hitprofile to be in line with new torpeedo hit profile
- Carrier armour now add small AA modifier

Visbility Rework:
- DD: Remain at 10

- Cl(Armor <lvl3): remain at 15 
- Cl(Armor >lvl3): 15-> 20
- CAs: 15 -> 20

- BCs: 20 -> 25 Vis
- BBs: 20 -> 30 Vis
- SHBC: 20 -> 30 Vis
- SHBB: 20 -> 35 Vis

- Gun Hit profiles: Heavy guns 85 -> 90, Torps 100 -> 120

### 3.12.6 'Delayed by Deadlock'

### Rules
 - Added new General rule: 12. Licensed equipment can not be altered by the purchaser. Temporary IC modifiers may not apply when purchased.

### General
 - Added 1 funny thing (don't worry about it)

#### Tank balance
 - All medium tanks technologies moved to 1 year earlier [38->37  40->39  43->42]
 - 1937 medium tank research cost increased to 175 days from 100
 - 1939 medium tank research cost reduced to 175 days from 200

#### Airplanes
 - Increased supply from air supply mission to 0.03 supply per plane from 0.01
 - Increased Transport Plane production cost from 38 to 50

#### UK
 - Trade with switzerland (military) Production efficiency cap reduced to 5% from 10%
                                     Production efficiency growth reduced to 3% from 5%
 - Trade with switzerland (civilian) Consumer goods factor reduced to -10% from -15%
                                     Construction speed bonus reduced to 7.5% from 10%
### Italy
 - Prevented Political BoPs from being able to remove the Mediterranean Front BoP
 - Upon the start of the Mediterranean Front BoP Italy will now receive a National Spirit equal to the effects of the previously active Political BoP

#### British Raj
 - Focus 'East India Railways' replaced railways with infrastructure 
 - Focus 'Integrate Princely Railways' replaced railways with infrastructure

#### Germany
 - First tier of spirit 'Cannibalized Civilian Economy' now gives -3% construction speed
 - Second and Third tier of spirit 'Cannibalized Civillian Economy' now gives -5% construction speed
 - Third tier of spirit 'Cannibalized Civillian Economy' now gives -5% stability 
 - Spirit 'Arms Subsidies Program' now gives 7.5% military factory construction speed

#### Finland
 - Focus 'Increase Military Budget' research bonus no longer applies to motorisation 
 - Focus 'Suomen Maavoimat' removed land doctrine reduction cost
 - Higher levels of Sisu reduced: Tier 3 Sisu Recovery rate reduced to 10% from 15%
                                              Core Defence reduced to 10% from 15%

                                  Tier 4 Sisu Recovery rate reduced to 25% from 20%
                                              Core Attack reduced to 10% from 15%
                                              Core Defence reduced to 15% from 20%

                                  Tier 5 Sisu Recovery rate reduced to 20% from 30%
                                              Core Attack reduced to 15% from 25%
                                              Core Defence reduced to 20% from 25%
 - Finnish army: organisation bonus removed 

#### Soviet Union
 - Reduced VPs in the western part of the Soviet Union. Increased VPs in the eastern part of the Soviet Union
 - Fixed hardlock caused by Beryia being an active advisor
 - Focus 'PC of Mortar Armament' time to complete reduced to 35 from 70
                                 No longer gives event 'Soviet-German Artillery Development' if at war with germany
 - Focus 'Industrial Modernisation' and 'Optimize Production Lines' now only available if Stalin is the current country leader
 - Focus 'Industrial Modernisation' reduced tech bonus to 50% bonus + 1y ahead of time from 100% bonus + 2y ahead of time
 - Focus 'International Revolutionary Marxism' focus time reduced to 35 days from 70
 - Focus 'International Revolutionary Marxism' added increased spawn-ins after 40% and 60% cap progress
 - Purge Debuffs are now all timed so will eventually be removed even if access to 'loosen army restrictions' decision disapears


#### Mongolia
 - Focus 'The Tannu Tuvan Question' now adds Tannu Tuva as core
 - Focus 'Nationalist Coup D'ètat' now disables joining factions
 - Decision 'Mechanised Help' reduced research penalty to 3% from 10%
 - Decision 'Civilian Factories' now removes 3 civs instead of 6 from soviets
 - Decision 'Military Factories' now removes 3 mils instead of 4 from soviets
                                 Spirit 'Helping with building of military factory' time reduced (on soviets) to 45 days from 90
                                 Spirit 'Soviet engineering help' time increased to 210 days from 180
 - Decision 'International help' now removes 2 civs or 2 mils instead of 4 from asked country

#### Manchukuo
 - Fixed hardlock caused by not completing The Kwantung Veto focus before China has capitulated

#### Denmark
 - Added focus "Administer Norway" to occupation focus tree, allowing annexation of Norway with full cores (with German consent)
 - Added focus "Reclaim Norway" to alt-history fascist focus tree, allowing annexation of Norway with 60% collaboration (with German consent)


### 3.12.5

### Manchukuo
 - Reworked focus tree

### Germany 
- U-boat effort focus time increased to 70 days forom 35
- Naval effort focus time increased to 70 days forom 35

### Submarines
- Torpedo 3 hit chance bonus removed
- Cruiser submarine hull range reduced from 5000 to 4500

### Naval high command
 - Close combat torpeedo hit change modifier reduced to 10% from 20%

### AI
 - Made UK more reliable at guarding Mediterranean targets
 - Bulgaria now should be rejected from Allies
 - Siam now sends volunteers to Japan
 - Made Japan worse?


### 3.12.4

### General
 - Total Armor of a division now takes into account 25% of highest batallion, from 40%
 - Total Piercieng of a division now takes into account 30% of highest batallion, from 40%
 - Cutting Corners MIO policy Reliability, Soft Attack, Hard Attack, and Armor debuff reduced to -8%, from -2.5%
 - 'Mobile Warfare' Doctrine perk 'Volkstrum' recruitable population reduced to 1%, from 2%
 - 'Mobile Warfare' Doctrine perk 'Indiscriminate Conscription' recruitable population reduced to 1.5%, from 3%
 - 'Guerrila Tactics' tactic combat attacker penalty reduced to -40%, from -50%
 - 'Guerrila Tactics' tactic combat defender penalty reduced to -30%, from -40%

### Bulgaria
 - Lancia now checks for Italy's focuses

### Germany
 - Removed Reichskommissariat Netherlands for larger Belgium 

### Brazil
 - Removed communist advisors 
 - Focus 'Academia Militar' organization buff reduced to 1%, from 3%
 - Focus 'Establish CIGS' organization buff reduced to 1%, from 3%
 - Focus 'The Strength of The Common Soldier' organization buff reduced to 1%, from 2%
 - Advisors 'Gustavo Barroso', 'Miguel Reale', 'Oliveira Viana', 'Leoncio Basbaum', 'Apolonio de Carvalho' are no longer available
 - Removed mentions of International Market mechanics from the tree

### Denmark
 - Added new alt-history fascist branch

### AI
 - Spain no longer will join factions

### Tank Rebalance

#### Tank Destroyer Brigades
 - Breakthrough malus increased to -65% for all weight classes

#### gasoline engine
 - Flat IC cost replaced with +20% IC multiplier

#### diesel engine
 - Flat IC cost reduced to 0.5 ic, from 1.5
 - Added +20% IC multiplier

#### petrol electric engine
 - Flat IC cost reduced to 1.5, from 2.0
 - IC cost multiplier increased to +20%, from +10%
 - Reliability malus reduced to -15%, from -25%, and made it multiplicative instead of additive
 - Reduced Breakthrough and Defense bonuses to +20%, from 25%
 - Removed Flat Breakthrough and Defense bonuses

#### Gas turbine engine
 - Flat IC cost reduced to 1.0, from 2.0
 - Added IC multiplier of +20%
 - Reliability malus is now multiplicative, instead of additive
 
#### Small Cannon
 - Soft Attack incresed to 19, from 17
 - Hard Attack increased to 13.5, from 11.5
 - IC cost reduced to 0.5, from 0.75
 - Moved to Interwar Artillery (1934) Technology, from Artillery (1936) Technology

#### Improved Small Cannon
 - Soft Attack increased to 25.5, from 24
 - Hard Attack increased to 16, from 14
 - IC cost reduced to 1.7, from 2

#### Advanced Small Cannon
 - Added new cannon
 
#### Close Support Gun
 - IC cost reduced to 3.5, from 4
 
#### Medium Cannon
 - Soft Attack reduced to 24, from 24.5
 - Hard Attack reduced to 16.5, from 17
 - Reduced Tungsten cost to 1, from 2
 - Steel cost of 1 added
 - Moved to Towed Anti-Tank (1936) Technology, from Anti-Tank Upgrade (1939) Technology

#### Improved Medium Cannon
 - Soft Attack reduced to 28.5, from 30
 - Hard Attack reduced to 19, from 20.5
 - Piercing reduced to 60, from 67
 - Removed Chromium cost
 - Moved to Improved Anti-Tank (1940) Technology, from Improved Anti-Tank Upgrade (1941) Technology in the Anti-Tank Technology Path
 - Moved to Improved Artillery Upgrade 2 (1941) Technology, from Advanced Artillery (1942) Technology in the Artillery Technology Path

#### Advanced Medium Cannon
 - Added new cannon

#### Medium Howitzer 1
 - IC cost reduced to 3, from 4

#### Medium Howitzer 2
 - IC cost reduced to 5, from 5.5

#### Basic High Velocity Gun
 - IC cost reduced to 2.75, from 3

#### Improved High Velocity
 - IC cost reduced to 4.5, from 5

#### Advanced High Velocity
 - IC cost reduced to 6.5, from 7

#### Heavy Cannon 1
 - IC cost reduced to 5, from 6

#### Heavy Cannon 2
 - IC cost reduced to 6, from 7

#### Heavy Cannon 3
 - IC cost reduced to 7, from 8

#### Super Heavy Cannon 1
 - IC cost reduced to 11, from 12.5
 
#### Amphibious Drive
 - Removed IC multiplier
 
#### Heavy Machine Gun Module
 - IC cost reduced to 1.75, from 2
 
#### Small Cannon Module
 - IC cost reduced to 1.75, from 2
 
#### Stabilizer
 - IC cost reduced to 1.5, from 2.5
 - Breakthrough reduced to 6, from 7.5

#### Smoke Launcher
 - Removed Defense stat
 - Increased Breakthrough to 8, from 2

#### Armor Skirts
 - Removed Hardness

#### Dozer Blade
 - Removed Hardness
 - Entrenchment increased to 1.5, from 1
 - IC cost reduced to 1, from 1.5

#### Auto Loader
 - IC cost reduced to 2.5, from 3

#### Easy Maintenance
 - Removed IC cost

#### Additional Machine Guns
 - Soft Attack increased to 3, from 2

#### Extra Fuel Tank
 - IC cost reduced to 1, from 2

#### Wet Ammo Storage
 - IC cost reduced to 1, from 1.5
 - Removed Attack Penalties
 - Added Breakthrough multiplier of -10%

### 3.12.3

### Military Industrial Orgs
 - Policy 'Cutting Corners' effects halved

### Soviet Union
- Focus 'PC of mortar armament' now gives event to germany. Germany may accept or deny giving both or neither a research bonus
- Tank Refurbshment Plant MIO armor cost reduction bonuses reduced by -1%

### UK
 - Hid imperial federation discussion decision
 - Hid Narvik Crisis category

### USA
 - Unique Naval MIO traits granting dockyard output reduced to 2.5%, from 5%
 - National Spirit 'Subsidized Naval Industry' dockyard output reduced to 5%, from 10%

### Brazil
 - Focus 'Experimental Weapons Development' research bonus no longer applies to nuclear technology
 - Focus 'Programa Paralelo' Nuclear Technology research bonus reduced to 1 year ahead of time, from 2

### Hungary
 - Now gains Banat when handed all of Transylvania

### Mongolia
 - National Spirit 'Focusing on CAS production' CAS IC increased to -10%, from -30%
 - National Spirit 'Focusing on fighter production' CAS IC increased to -10%, from -30%
 - Focus 'Modern Day Heavy Cavalry' now grants 1 '1 year ahead of time' bonus, from 2 '2 year' bonuses


### 3.12.2

### Denmark
 - Scattered more steel throughout the focus tree for MP tradeback QoL

### SAF
 - 'Suppress the Stormjaers' now gives -5% Fascism 

### Soviet Union
 - Focus 'Paced Industrialization' time to complete increased to 70 days, from 35
 - Focus 'The Need for Policy Changes' political power reward decreased to 50, from 75
 - Focus 'Dissent In the Party' political power reward decreased to 50, from 100
 - Focus 'The Right Opposition' political power reward decreased to 25, from 75
 - National Spirit 'Desperate Measures' now lasts for 365 days, from 180
 - Focus 'Merge Tank and Material Plants' time to complete increased to 70 days, from 35

### France
 - Metropolitan and Colonial civilian factories now come with building slots

### Romania
 - Can no longer refuse Second Vienna Award

### Commonwealth Shared Tree
 - Focus 'Allied Economic Cooperation' MIO funds reward decreased to 500, from 750
 - Focus 'Expand the Mining Towns' building slot reward decreased to 2, from 3
 - Focuses 'Paratrooper Specialization' and 'Airplane Manufacturing' are no longer mutually exclusive

### Officer Corp
- Flexible Contracts, Global Presence, Surprise Attacks, Decisice Battle reworked

### Submarines
 - Removed Sub Engine 3, Sub 4, Snorkel 2
 - Torpedo 3 cost 120 -> 250
 - Reduced Snorkel 1 visibility -10% -> -5%
 - Cruiser subs limited to one range module 

### 3.12.1

### Artillery
 - Rocket artillery 1: Brkth 9 -> 18
                       Soft attack 30 -> 33
 - Rocket artillery 2: Brkth 12 -> 22
                       Soft attack 38 -> 42
 - Motorised rocket artillery 2: Brkth 12 -> 22
                                 Soft attack 36 -> 42           

### Soviet union


### Air High Command
 - Continuous strike: Cas mission efficiency +25% -> +15%
                      Organisation damage +25% -> +15%
                      Ground support +25% -> +15%

### Air Designer 
 - Rocket rail: Weight 1 -> 2
                Tungsten cost 0 -> 1

### 3.12.0 'Bigly'

### General
 - Paradox update implemented 
 - Political raids stability penalty -10% -> -8%
 - Updated generic organisations
 - Acctually fix German North Africa bug (most of the time)

### Commonwealth
 - Expanded Shared Focus Tree with new 'Allied Economy' branch

### Canada
 - Brought into parity with vanilla additions from recent patches

### United Kingdom
 - Added 'Global Defense' alt-historical path
 - Minor reorganization of 'Home Defense' focus branch
 - Focus 'Military Training Act' now improves national spirit 'Prepare for the Inevitable' by -25% training time
 - Focus 'Secure Iraq' now puppets Iraq and brings it into the war, instead of generating a war goal
 - Focus 'Secure Iraq' now requires the UK to lose Lower Egypt to be taken
 - Focus 'Embargo Germany' now causes all nations in faction with England to embargo germany
 - Focus 'Prepare for the Inevitable' now takes 35 days to complete, from 70
 - Focus 'Commonwealth Ties' now takes 70 days to complete, from 35

### Free France
 - Reworked intervention focuses

### Bulgaria
 - Added 'Appoint Right Wing Ministers' alt-historical path
 - Readded 'The Third Bulgarian Empire' Focus

### Soviet Union
 - Added 'The Right Opposition' alt-historical path
 - Tannu Tuva now starts as a puppet of the Soviet Union, to improve Right Opposition path experience

### Finland
 - 'Cooperation with Germany' adds military access with Germany
                              removed guarantee        
 - The Continuation War adds military access with the rest of the Axis  
 - 'Communist Pressure' from 'Secure Leningrad' 365 days -> 150 days
 - Upon Winter War Victory add 'Anti-Communist Pressure' for 90 days                 
 - Upon Winter War Defeat add 'Communist Pressure' for 90 days
 - Removed Market Subsidy from foreign amror and added -100% license cost and -5% Production to light tanks
 - Removed Market Subsidy from Foreign Aircraft

### New Zealand
 - 'Bob Semple Tank' now provides a bonus for all armour

### Denmark
 - Add in-game tutorial tip under SPT Info decision category
 - Streamline Danish occupation decisions for Germany, including reduced event times and removing options bad for everyone
 - Remove all additional mil occupation penalties
 - Further re-arrange and reduce time in Danish occupation focus tree
 - Butter Front no longer removed from Germany upon Danish independence
 - Add tooltip to 'Petition for Independence' focus to clarify that it unlocks the Danish political focus tree again
 - Lower the starting autonomy in the Overlord Balance of Power
 - Add German and Italian Tank MIOs to Denmark
 - Reduce truce times with Allies from 6 months -> 1 day to avoid truce violations after joining the war on the Axis

### AI 
 - AI Japan will now annex China rather than puppeting them (for real)
 - Added AI plan for Spain's focuses during the civil war

### Hungary
 - Joint air development - Removed market subsidy and changed to sharing group and 1 x100 boost to CAS/Fighters
 - Added a new focus Foreign production Assistance which give a -10% production reduction to fighters, CAS and Tactical bombers
 - Added a Mutally exclusive marine branch
 - Ingenius designs Changed to Funding the air force, Provides MIO funds and 2x 50% Air bonus
 - Form parachute Battalions changed- 1x 300% --> 1x 200%
 - Joint tank Procurment - removed subsidy, now joins research group, Gives German Tank License Agreement, which provides license cost -100% and Medium and heavy tank production -5%
 - Naval Tree Hidden 
 - Establish the airforce - Air Exp 25 --> 50
 - Added "Train with the Luftwaffe" and "Train with the Regia Aeronautica" - Mutally exclusive which provide air buffs

### Italy
 - Treaty with Germany - Removed subsidy, Added opinion factor, 1x 100% Synthetics ---> 2x 100% Synthetics 
 - 'Ultimatum to Yugoslavia' Active time 14 -> 60 days 
                             Yugoslavia will now always refuse

### Spain
 - Added 'Unite Iberia' focus
 - 'Join the Allies' removed branch
 - 'The Latin Bloc' removed branch

### Mexico
 - Heroic Military Collage 70 days --> 56 days
 - Army Expansion Program 70 days --> 56 days
 - Law On Industrial Promotrion 70 days --> 56 days
 - NAFINSA Added an extra building slot and Mil
 - Add tutorial tooltip to SPT Info
 
### Australia
 - Department of supply and development 70 --> 56 days

### Netherlands
 - Will now join Allies upon having a war declared against them


### 3.11.3 'Where were you when soviet was kill'

### General
 - Added Mongolia to the 'Select Country' screen
 - Added remaining playable nations to host tool
 - Updated admiral traits to be in line with vanilla 
 - Added new loading screen quotes

### Germany
 - Now can select which Quisling path Norway will choose
 - Fix the Norrland resource event when Quisling's Coup fires
 - 'Second Vienna Award' should no longer improperly bypass 
 - Reworked compliance branch focuses for Scandanavia and Benelux

### Japan
 - Added a date check for Steady Development
 - National Spirit 'Desperate Measures' will now be removed if BOP reaches at least 25% American Dominance
 - Focus 'Guide The Zaibatsus' now takes 35 days to complete, from 70

### Soviets
 - Winter War war goal now doesn't expire
 - 'Tula Arms Plant' production bonuses 10% -> 5%

### Norway
 - Removed the fascist resistance mechanic
 - Removed Quisling's war goal focuses 

### Spain
 - 'Restore the Monarchy' now requires not being fascist

### Brazil
 - 'Support the Marines' correctly gives amphibious chassis tech 
 - Added the mountaineer special forces focus branch
 - Removed ability to have Minervino de Oliveira as leader and advisor

### South Africa
 - 'Police Windhoek' nows give 5% stability
 - 'Secure Interests in Africa' nows give 10% stability

### New Zealand
 - 'Schofield Tank' now provides a bonus for all armour

### Netherlands
 -  Removed seawolf from Conrad Helfrich

### AI 
 - AI UK removed ability to warn for fleet size via naval treaty
 - AI Soviets no longer naval invades Finland
 - AI Japan will now annex China rather than puppeting them

### Army Command
 - 'Ideological Loyalty' Division recovery rate 20% -> 10% 
                         Encirclement penalty -25% -> -10%

### Air Force Command
 - 'Steel heart steel wings' Cas damage reduction 15% -> 5%
                             Air home defence factor 20% -> 10%
 - 'Airborn heroes' Cas damage reduction 10% -> 5%
                    Air home defence factor 15% -> 10%

 ### Support companies
 - Pioneers: marsh attack modifier +10% -> +20%


### 3.11.2 'https://hoi4.paradoxwikis.com/AI_modding'

### Major Nations
 - Greatly improved AI behaviour 

### Germany
 - Can now declare war on the Soviet Union 3 months earlier (1.1.1941 or 1.3.1941 depending on which industry branch they have chosen)

### France
 - Potentially fixed an issue where French North Africa flips to Germany upon capitlation

### Hungary
 - 'Trade Deal with Germany' now properly applies Interventionism 

### Siam 2.0
 - Fixed Cultural Mandate decisions
 - 'Elephants' and 'African Elephants': Added Elephant Recon Companies
 - Added Bangkok Flooding event and related Pad Thai branch

### 3.11.1 'wtf chafford went sicko mode'

### General
 - Removed Stickmiin's funny haha logo
 - Fixed back button on new game screen
 - Added all playable nations to 'interesting'
 - Southern El Alamein tile changed to hills
 - CAG Night Fighting fixed, and no longer limited to UK
 - Some other balance and fixes

### Army Spirits
- Clarified percentage chances of new officer traits from army spirits
- Moved Engineering Schools back to Superior Firepower

### Pacific Front
 - Added decisions to view targets before the bop is activated

### Mediterranean Front
 - Added decisions to view targets before the bop is activated

### Winter War
 - Added decisions to view objectives before the war begins

### Tank Designer
 - Heavy two man turret: soft and hard attack +5% -> +2.5%
                          IC cost 4.5 -> 4
 - Heavy three man turret: soft and hard attack +10% -> +5%
                          IC cost 6.5 -> 6
 - Heavy cannon I: Soft attack 29 -> 28.5
                   Hard attack 23 -> 22.5
 - Heavy cannon II: Soft attack 35 -> 34
                    Hard attack 26 -> 25
 - Heavy cannon III: Soft attack 40 -> 39
                     Hard attack 34 -> 33

### Submarine Designer
 - Submarine 3/4 cost increased 1000x to prevent their construction

### USA
 - Moved 'Pacifism no More' to be available before 'Money Only', requiring Germany to complete 'Fate of Czechoslovakia'

### France
 - Removed ability to deny Hatay
 - Make rearmament election event less punishing. Limited to France for now.

### Siam
 - Cultural Mandate focus overhaul
 - 'Educate the Population': Completion time 70 -> 35 days
 - 'Utilise Land': Building slots 2 -> 1
 - 'Learn from Japan': Now adds Co-Prosperity tech sharing group
 - 'Cooperate with Japan': Now adds more cooperation with Japan 
                          Fascism 10% -> 0%
 - 'Phibun, Prime Minister': Completion time 70 -> 7 days
 - 'Actions are Stronger than Words': Completion time 35 -> 14 days
 - RADAR focus builds RADAR
 - Propaganda Techniques focus rework
 - 'Thai Wartime Success' -> 'African Elephants'
 - New political advisors available
 - New MIOs available
 - Now starts with two generals
 - Better focus GFX for Zbra
 - Added AI strategy
 - Spelling and grammar fixes

### Brazil 
 - Base starting war support 50% -> 15%
 - 'Ensure Montinued Military Support' Base war support 10% -> 5%
                                       Focus time 35 days -> 70 days
 - 'The Cohen Plan' Focus time 70 days -> 35 days

### Japan
 - Now starts in Co-Prosperity tech sharing group

### Manchukuo
 - Fixed Baba's autonomy states
 - 'Invite Japanese Advisors': Now adds Co-Prosperity tech sharing group

### Finland
 - When joining the Continuation War, automatically declare on Monglia as well (if they are still in faction)

### Commonwealth Minors
 - Infrastructure focuses changed to prioritise useful states

### Denmark
 - Removed protectorate's resistance branch

### 3.11.0 '2 weeks in Helsinki'

#### General
 - New Siam Focus Tree
 - Readded Finland as a playable nation
 - Increased MIO cost to 1 due to bugs
 - SPT_no_resource_penalty now grants 50k base fuel gain

#### Germany
 - Prevented unintended focus tree paths (no more bokoen1 strategies sadge)
 - German War Economy now sets your economy law to Total Mobilisation
 - German War Economy now grants 4 military focuses, from 6
 - Nationalize Steel Production now grants 6 military factories, from 4
 - 'War with the USSR' mow available after 1st of march if germany does '3 year plan' path

#### France
 - Free France Focus Tree: added offmap civilian and military factories and dockyards to several focuses

#### Canada
 - Added decision to annex and core South Africa if it is controlled by AI

### 3.10.2

#### Soviet Union
- Significantly nerfed the tank refurbishment mio
- Increased consumer goods from "Third Five Year Plan" +10% -> +20%

### 3.10.1

#### General
 - Updated the mod for TOA
 - Made it free to set the mio for equipment

### 3.9.0 

### Commonwealth
 - Added new shared tree, unlocks once UK completes "Commonwealth Ties"

### Germany
 - Reworked industry path to allow for early war path
 - Focus "Short Term Rearmament" allows for Jaegernotprogramm decision 
 - Jaegernotprogramm war support -5% -> -10%
                     Decision active time 360 -> 180 days

### UK
 - Focuses "Develop the Raj", "Indian Autonomy", "Development in Canada", "Development in Australia", "Develop South Africa" focus time 70 day -> 56 days
  - Focus "Commonwealth Ties" -70 days -> 35 days

### USA
 - Focus "Subsidies For The Farmers" consumer goods -5% -> -10%

### Mongolia
 - Independent economy: Political power gain -0.1 -> -0.25
 - Collectivized Economy: Tanks cost modifiers -10% -> 0
                          Production efficiency cap 0% -> 10%

### Italy
 - Focuses that require Politcal BOP now available after Mediterranean BOP activates

### Army high command 
(Lowered to balance for extra experience gained from the shared commonwealth focus tree)
 - Relief of Command Army Experience 25% -> 15%
             Army Advisor Cost -50% -> 25%

### 3.8.7

### Mongolia
Indipendent economy: Political power gain -0.1 -> -0.25
Collectivized Economy: Tanks cost modifiers -10% -> 0
                       Production efficiency cap 0% -> 10%
                       
### 3.8.6

### General

 - Added new "Together For Victory" Joint Focus Tree for Commonwealth minors

### UK
 - Focus "Commonwealth Ties" time reduced to 35 days, from 70


### 3.8.6

### General
- Fixed the special forces specilisation decision
- Increased consumer goods from warbonds to 20%

### United Kingdom
- Re-added "Airborne Forces Depot" focus

### Finland
- Prevented them declaring on the Soviets when Germany does

### Portugal
- Disabled portugal from being able to send volunteers to the civil war


### 3.8.5

### General
- Integrated the Host Tool Mod 
- Spirit of the Academy "Meticolous Preparation" Planning bonus 7.5% -> 2.5%
- Added impassable terrain to Papua and Borneo
- Added Bab-el-Mandeb Strait (Yemen-Djibouti strait)

### Germany
 - Removed the communist advisor

### Soviet Union
 - Removed the ability to fire the head of the NKVD
 - Increased the consumer goods gained in "Third Five Year Plan" 2.5% -> 10%

### Japan

 - Nashin Ron Rapid Development spirits now last for 250 days, from 200
 - Decision "Ichi Go" available after 1 june 1939
 - Spirit "Challange the Zaibazus" mililitary and civilian factory construction speed 12.5% -> 10%
 - Focus "Long Term Planning" now grants +5% efficiency cap, from 10%
 - Focus "The Zaibatsus" tooltip now displays all possible bonuses before choosing a path and shows only the selected path once completed
 - Focus "Strike The Islands" now grants +15% naval invasion planning, from +20%
 - "Bushido Spirit" trait now reduces Armor attack and defense, to prevent unintended leader choices
 

### 3.8.4

### General

 - Added 2 new straits: Strait of Malacca and Sunda Strait

 ### Italy
  - Balbo and Grandi are now available leaders

### 3.8.3

### General
 - Changed in game speed to reflect old speed (games will now be played in 3/4 speed instead of 2/3)

### Rule Change
 - Changed War Rule 9 to not include support companies

### India
 - Focus "Assam Oil" increased oil resources 3 -> 10 oil
 - Focus "Integrate Princley Railways" focus time 35 -> 70 days
 - Focus "Strengthen Ties With British Investors" Autonomy value 150 -> 100
 - Focus "British Rail Investors" Autonomy value -250 -> -200
 - Focus "British Arms Investors" Autonomy value -250 -> -200
 - Focus "Imperial Service Troops" Autonomy value -50 -> +50
 

### 3.8.2


### General
 - Guerilla Tactics tactic now grants -50% attacker damage, from -70%
 - Guerilla Tactics tactic now grants -40% attacker damage, from -60%

### Rule Change
- Changed Spain rule 3 to "May join the Axis ONLY if French West Africa is under Axis control."

### Tank designer
- Modern and superheavy tanks can now use their correct turrets and cannon

### Mongolia
 - Spirit "Build an Independent Economy" all tank production now -15% (down from 15/20/25 for light/mediums/heavies)
 - Spirit "The Flying Circus" Special forces defence and attack +25% -> +10%
                              Encirclement penalty +25% -> 15%


### 3.8.1
### Australia
 - Expand the northern railway now takes 35 days, from 70

### Soviet Union
 - War support from "Turkey Seizes Control Over the Bosporus" 10% -> 5%

### Manchukuo
 - Focus "From Mountaineer regiments": Removed special mountaineer buff
                                       Added 4 75% special forces doctrine cost reductions
 - Clarified Big/Small Manchu event

### MIO
 - Made Vickers-Armstrong available for all commonwealth nations
 - Vickers-Armstrong: "Expand production facilities" production effeciency cap and efficiency gain 10% -> 5%
 - Infantry tank designer: "Production Division" production efficiency gain 10% -> 5%
                           "Modular Construction" production efficiency gain and efficiency cap 10% -> 5%
 - Standardized Prodction: "Standardized Components" production efficiency gain 15% -> 5%
 - Halved all Air Mio effects of "Light aircraft manufacturer", "CAS aircraft manufacturer", "High Agility Fighter Aircraft manufacturer" and "Range Focused Aircraft Manufacturer"

### 3.8.0

#### General
 - Updated to work with AAT
 - Advisors updated to match new AAT consumer goods rework
 - Disabled International Market for all countries
 - Disabled the special forces tech "Combat Insertion"

#### Finland
 - (Temporarily) Reverted Finland back to vanilla and remove them as a playable nation 

#### USA
 - Rebalanced spirits and focuses to better fit the new consumer goods rework
 - Focus "Money Only" now takes 35 days to complete, from 70
 - National spirit "Forming New Cabinet" now lasts for 365 days, from 200
 - Focus "Federal Construction" now takes 35 days to complete, from 70
 - Focuses "Rebuilding America", "Lower Taxes", and "Federal Construction" now reduce the duration of Ongoing Recession mission by 30 days each
 - All War Plan Upgrade focuses now take 70 days to complete, from 35
 - Focus "Standard Oil of California" now requires "Campaign for Votes" instead of "Industrial R&D"
 - National spirit "Rallying the Nation" now grants +15% Military Factory Construction Speed
 - Focus "Boots on the Ground" now grants 7.5% attack, recovery rate, and organization, from 10%
 - National spirit "Subsidised Military Industry" now grants 5% factory output, from 10%
 - National spirit "Subsidised Naval Industry" now grants 10% dockyard output, from 15%
 - Focus "Review The Budget" now unlocks "Pay Farm Subsidies" decision
 - Focuses "Subsidise the Military Industry" and "Subsidised the Naval Industry" now grant +15% MIO funds gain
 - Focus "Break the Monopolies" now grants +25% MIO funds gain
 - Focus "Booming Interior Economy" now grants +1 building slot for every state with the modifier "Booming Interior Economy"
 - Focus "Wartime Industry" now grants +1000 MIO funds

#### JAPAN
 - Rebalanced spirits and focuses to better fit the new consumer goods rework
 - National spirit "State Shintoism" now grants 10% factory output, from 20%
 - Focus "The Zaibatsus" now grants +5% resource gain efficiency instead of -2.5% consumer goods if Japan has "Nationalize the Zaibatsus" spirit
 - Focus "Stockpiling Strategies" now grants +5% resource gain efficiency instead of +10%
 - National spirit "Zaibatsus Challenged" now grants -10% tank, naval, materiel, and aircraft MIO cost
 - National spirit "Nationalize the Zaibatsus" now grants -25% tank, naval, materiel, and aircraft MIO cost
 - Focus "Seize Zaibatsu Dockyards" now takes 70 days to complete, from 35
 - Focus "Nationalize the Zaibatsus" no longer grants -5% stability
 - Focus "Let the Zaibatsus Expand" now grants +1 MIO size
 - Focus "Let the Zaibatsus Expand" now takes 70 days to complete, from 35
 - Focus "Let the Zaibatsus Expand" now grants national spirit "Zaibatsus Empowered"
 - Focus "Supremacy of Technology" now grants +10% MIO funds gain
 - Focus "Armored Divisions" now grants +1 MIO size to Osaka Army Arsenal (tank designer)
 - National Spirit "Supremacy of Will" now grants -5% army doctrine cost
 - Focus "Armored Divisions" now grants its bonus as an MIO trait, +1 MIO size to Osaka Army Arsenal, and an extra 5 army xp
 - Focuses "Range Focus" and "Agility Focus" are no longer mutually exclusive

### 3.7.3

#### General
- Nerfed "Feign Weakness" decision's attack and defense bonuses in the meditterenean bops `30%` -> `15%`
- Added some new focus gfxs
### 3.7.2

#### Rule Change
- Edit rule so Germany can now only declare on soviet union after 1941.06.01.

#### General
- Increased Concentrated Industry dockyard output `10%` -> `15%`
- State of Gibraltar now has two tiles [So it can be invaded from outside the med]
- Soviet Inion now get mill access to Republican Spain to avoid reinforcement glitch [volunteers wouldnt reinforce]
- Germany,Uk,USA and Romania got some new focus icons [stickmin made me give him credit]

#### Manchuko
- Name and colour now changes depending on whether they go Big or Small Manchu

#### Japan
- Name now changes to "Empire of Japan" if they take "大日本帝國" (which translates to Pan Asia) 
 
#### USA
- Reduced Bureau of ships days `70` -> `35` 
- Changed requirements to lend lease focus to fix bug

#### Germany
- Reduced focus days for "War with Soviet Union" `14` -> `7`


### 3.7.1

#### Rule Change
- Added rule "May only take coastal states when annexing China if Manchuko has completed "Chinese Leadership." for Japan.

#### General
- Increased compliance tickdown for harsquote `0.08`->`0.12`
- Decreased local factories for harsh quotas `25%` -> `20%`

#### Australia
- Made it quicker to access another research slot

#### Japan
- Focus "Long Term Planning" no longer grants -5% consumer goods
- Focus "The Manchurian Project" no longer requires Manchukuo to exist to be taken
- "Manchurian Project" decisions will now have their effects apply even if Manchukuo does not exist
- Focus "Nationalize War Industry" now grants 4 civilian factories, instead of 2 civilian and 2 military factories
- Focus "Nationalize Zaibatsus" now grants -5% stability
- Focus "The Armed Forces" now grants +5% max planning, from +10%
- Focus "Complete Industry Reorganization" now grants +10% max factories, from +20%
- Pan-Asian Integration state modifier now grants -10% non-core manpower, from -7.5%
- Focus "Army Expansion" now grants +30 army experience, from +15
- National Spirit "Tora! Tora! Tora!" now correctly lasts for only 6 months

##### South Africa
- Increased civs from "Expand the mining industry" `2` -> `4`
- Increased research bonuses for industry from "Heavy engineering" `1` -> `2`
- Increased the amount of infrastructure given from "Infrastructure Effort" `2` -> `4`

#### Tank Designer
- Reduced research cost for Medium 1 `2x` -> `1x``
- Increased medium tank cannon soft attack `23.5` -> `24.5` and hard attack `16` -> `17`
- Increased medium tank cannon 2 soft attack `28.5` -> `30` and hard attack `19` -> `20.5`
- Decreased medium tank cannon 2 tungsten cost `3` -> `2``
- Increased high velocity cannon hard attack `25.5` -> `28`
- Decreased high velocity cannon 2 tungsten cost `3` -> `2`
- Decreased heavy cannon 1 and heavy cannon 2 soft and hard attack by `1`


#### Ship Designer
- Increased Submarine 1 hull cost `220` -> `300`
- Increased Submarine 2 hull cost `250` -> `350`

### 3.7.0

#### General
- Game coded in some rules and removed them from the ruleset
- Reduced production reduction from mech upgrades `-10%` -> `-5%`
- Added topbar displaying your resources
- Fixed most of loading quotes being hidden
- Hid logistic strikes and minelaying, minesweeping air missions 


#### Romania
- Reworked the focus tree

#### USA
- Added alf landon's path

#### Mongolia
- Added Mongolia as a playable country with a new focus tree

#### Japan

- Nanshin Ron Steady Development Focuses now take 35 days to complete, from 70
- Nanshin Ron Rapid Development Focuses now grant their buffs for 200 days, from 365
- National Spirit "Rapid Development" now grants 60% mil construction speed, from 40%
- Focus "Rapid Development" now grants -40% mil construction speed, from -20%
- National Spirit "Quick Retooling" now grants 20% efficiency cap and 40% efficiency growth, from 15% efficiency cap and 30% efficiency growth
- Focus "Quick Retooling" now grants -20% efficiency growth and -10% efficiency cap, from -10% efficiency growth and -5% efficiency cap
- National Spirit "Factory Mobilization" now grants 40% factory output, from 30%
- Focus "Factory Mobilization" now grants -20% factory output, from -10%
- Focus "Long Term Planning" now grants -5% consumer goods
- Focus "Stockpiling Strategies" now grants 10% resource gain efficiency 


### 3.6.5

### General
 - Added allied debuffs for loosing the mediterranean front

 - Added temporary Allied supply and fuel consumtion debuff for losing Suez or Gibraltar

 - France and Soviet Union no longer start with small cannon 2

### Focus 
 - Spain Tangiers enclave no longer gives UK war goal

### 3.6.4

### General
- Finland
   - Finnish industrial Concern: Factory output 20% -> 12.5%

 - Soviet Union
   - Spirit "Victory in the winter war" if Finaln is player now lasts 210 day

 - Turkey kan no longer do focuses beyond "Reconfigure Turkish Foreign Policy" to prevent them from joinng factions
### Rules
 - Soviets may now only send 5 volunteers to China

### Focus
 - Spain
   - "Tangiers Enclave" can no longer give UK a war goal
   - "An Armoured Corps" no longer requires "Join The Axis"

 - Manchukuo
    - "Research And Education Department" required factories 50 -> 25
### Army Dooctrine

- Mobile Warfare
   - Mechanized Offensive: Motirized org +15 -> +5
                           Mechanised org +15 -> +5
                           Amtrack org +15 -> +5
### 3.6.3

### Focus Tree
### General
 - Italy 
    - Allowed starting units to be deleted
    - Removed decision to add compliance
    
 - Germany
    - Hid event about patience running thin with Yugoslavia

- Removed minesweeping and minelaying buttons
 
### Focus
 - USA
    - Major rebalance of new part of focus tree

 - Italy
    - Added focus to get compliance on Yugoslvavian cores

 - Soviet 
    - Removed "Mine Warfare" focus

### Airplane designer
 - Radio Navigation: Sub detection 4 -> 6
 - Radio Navigation II: Sub detection 6 -> 9


### USA 

    - Focus "Subsidise The Military Industry" now reduces Ongoing Recession by 90 days, from 60
    - Focus "Subsidise The Naval Industry" now reduces Ongoing Recession by 90 days, from 60
    - Focus "Subsidies for the Farmers" now reduces Ongoing Recession by 90 days, from 60
    - Focus "Subsidise the Mining Industry" now reduces Ongoing Recession by 90 days, from 60
    - Focus "Revitalised Interior Economy" now grants 10% construction speed from 5%, and 5% military construction speed and 5% civilian construction speed from 10%
    - National Spirit "Home Front" now grants 5% military construction speed, from 10%
    - National Spirit "Dust Bowl Relief" no longer grants -2.5% consumer goods, and had its Stability reduced to 2.5% from 5%
    - National Spirit "Subsidised Mining Industry" now grants 15% resources from 10%
    - National Spirit "Subisdised Farming Industry" now grants 2.5% consumer goods, from 5%, and 7.5% stability from 10%
    - National Spirit "The 1937 Recession" now grants -0.15 political power gain
    - National Spirit "Subsidised Naval Industry" no longer grants dockyard construction speed, instead it grants +15% dockyard output
    - National Spirit "Subsidised Military Industry" no longer grants military factory construction speed. And grants 10% factory output from 5%
    - War Plans focuses have been shortened to 35 days
    - War Plans focuses now start at 5% attack and defense vs targetted countries, but grant 2.5% attack and defense per focus completed.
    - Focus "The Giant Wakes" now requires 30% war support, from 35%
    - Focus "USACE Projects" now requires 20% war support, from 30%
    - Focus "Military Construction" completion time reduced to 35 days, from 70
    - Focus "Mobilise The People" now grants 2 less civilian factories
    - Focus "Prepare The War Industry" now grants 2 less military factories
    - Focus "Expand Federal Taxes" now has scaling senate opposition based on war support
    - Focus "National Youth Organization" now grants 2 building slots per state, from 3
    - Focus "Fair Labor Standards" completion time reduced to 35 days, from 70
    - Focus "Subsidies for the Farmers" completion time increased to 70 days, from 35
    - Focus "Subsidies for the Mining Industry" completion time increased to 70 days, from 35
    - "The Recession of 1937" event now also grants medium senate and house opposion

### 3.6.2

### General

 - All non-playable nations have had their ahistorical paths ,either blocked or removed, to prevent mishaps.

### Focus Trees
 - USA:
	- New expanded USA focus tree.
 
 - Hungary:
	- Hungary can now go down the Fascist King route.
 
 - Italy:
	- Request Control Of French Territories focus now asks for the correct territories and does not require Vichy to exist to be taken.
 
 - Finland:
	- Replaced "Retake Karjala" with "Mobilised The Nation"
	- Fixed add fascism popularity in "Proclaim Greater Finland"
	- Fixed the field hospital spirit in "The Great Red Menace".
    - Buffed "The Great Red Menace"

### Events

 - New Scuttle The French Navy event chain, which allows for Germany to capture a portion of the french navy after capitulating them. [ done to balance for a lack of Vichy France ].

 ### 3.6.1
### General

- Soviet Union
    - Third Five Year Plan focus Consumer Goods buff 0% -> 2.5%


### 3.6.0

### General
 - All of axis now affected by mediterranean balance of power
 - IEA will no longer make your eyes bleed
 - "Radio Propaganda" and "Utilize Domestic Film Industry" decisions now require higher World Tension values
 - Added new character Karnov (don't worry about it)
### Focus tree

- Japan
    - Rebalanced focus duration of several japanese focuses
    - Improved several japanese focus tooltips to better inform players of unique effects
    - Correct several japanese focuses to no longer spawn factories in Saipan, Iwo Jima, and Kurill Islands
    - Strike South Doctrine focus no longer requires Greater East-Asian Co-Prosperity Sphere focus


    - Supremacy of Will spirit no longer gives Division Attack and Division Defense, instead it gives +5% Org and +4% Reinforce Rate
    - Challenge The Zaibatsus: stability debuff -15% -> -10%
    - Zaibatsu Investments spirit Resource Gain Efficiency buff reduced from 15% to 10%
    - Strike the Indies: Removed escort efficiency
                         Division speed buff 5% -> 10%

    - Allience With Siam focus now requires NAP with Soviets focus instead of Sign Tripartite Pact
    - Added Nationalize the Zaibatus focus that allows the Challenge the Zaibatsus spirit to be improved
    - Added Large Artillery Studies focus: Railway Gun technology and 3 Railway Guns

    - Strike South spirits now have been merged into a single Nanshin Ron spirit
    - Strike South Branch expanded with new Military and Industry branches

- Soviet Union
    - Infrastructure effort: Focus duration 70 -> 35
    - Heavy Industry: Focus duration 70 -> 35
    - Expand the Aircraft industry: Focus duration 70 -> 35
    - Foster Flying Club: Focus duration 70 -> 35
    - Modernize Aircraft facilities: Focus duration 70 -> 35
    - Women in Aviation: Focus duration: 70 -> 35
    - Third five year plan: Modifi consumer goods 0.05 -> 0

 - Italy 
    - Demand Ticino and Request Control of French Territories focuses re-added to allow Italy to gain the states required to form Greater Italy

 - USA 
    - Selective Training Act: Set base war support 10% -> 0%
### High command

 - All air mission type high command advisors buffed

 - Gino Verchiella (Canada): Air superiority expert -> Close air support expert
 - Sándor Magyarossy (Hungary): Air combat training specialist -> Air superiority expert
 - Vasily Yanchenko (USSR): Removed exile and civil war requiremets 
 - Nishizo Tsukahara (Japan): Naval strike specialist -> Naval strike expert 

 - Maneuver Warfare: Org loss when moving -0.4 -> -0.3
                     Army Fuel consumtion 0.1 -> 0
                     Supply consumtion 0.15 -> 0.1
                     Supply truck attrition 0.3 -> 0.15
### Airplane designer

 - All Airframes significantly reduced production cost
 - All cas modules significantly increased production cost

 - Medium bomb bay: ground attack 3 -> 4
 - Rocket rails: gound attack 4 -> 6
 - Guided anti-ship misssile: naval strike attack 8 -> 11
                              weight 15 -> 12
                              producion cost 15 -> 11
 - Non strategic material: production cost modifier -0.075 -> 0.1
                           air defence -6 -> -4
 - Rocket engine 1: range modifier -0.9 -> 0.65
                    reliability 0 -> -0.125
                    tungsten cost 3 -> 2
 - Rocket engine 2: range modifier -0.85 -> 0.50
                    reliability 0 -> -0.075
                    tungsten cost 3 -> 2
 - Rocket engine 1: range modifier -0.8 -> 0.35
                    tungsten cost 3 -> 2
 - Air-air radar 1: No longer limited to interception
                    Night time penalty -0.2 -> 0.15
                    Air attack modifier 0.1
 - Air-air radar 2: No longer limited to interception
                    Night time penalty -0.4 -> 0.3
                    Air attack modifier 0.15
 - Radio navigation 1 when on naval missions: Surface detection 0 -> 6
                                              Sub detection 0 -> 4
 - Radio navigation 2 when on naval missions: Surface detection 0 -> 10
                                              Sub detection 0 -> 6
                                              Production cost 1 -> 2
 - Air-Ground radar 1: Removed all naval bonuses
                       When on close air support mission: Ground attack 0 -> +10%
                       When on close recon

 - Air-Ground radar 2: Removed all naval bonuses
                       When on close air support mission: Ground attack 0 -> +15%
### Tank designer

 - All light tank chassis: production cost -0.3
 - Small cannon: soft attack 25 -> 24
                 steel cost 0 -> 1
                 build cost 1.5 -> 2
### Technologies 

 - Moved radio navigation 1: Radio -> Decimetric radar
 - Moved radio navigation 2: Decimetric radar -> Centimetric Radar
 - Moved Air-Ground Radar 1: Improved Centimetric Radar -> Centimetric Radar
 - Rocket engines: year of technology 1944 -> 1943
 - Improved rocket engines: year of technology 1945 -> 1944
 - Advanced rocket engines: year of technology 1946 -> 1945
 - Centimetric Radar: fighter detection 0 -> 0.05
 - Advanced Centimetric Radar: fighter detection 0 -> 0.05
### 3.5.2
 - Added new quotes
### Rules
 - Updated rules on paratroopers

### Focus Trees
 - UK
     - Hold the imperial conference now requrires "Development in Australia" instead of "Develop New Zealand"


### 3.5.1
### Rules
 - Clarified win conditions
 - Only minors nations may ask for tradebacks 
 - Japan must attack allies before 1942.01.01
 - USA may now have troops in Raj before the dacca line falls
 - USA may now join WW2 if Raj looses port to European Axis

### Focus Trees
- Usa
   - Updated tooltip in bureau of ships [Now shows correct numbers]

 - Germany
     - Align Romania: Focus duration 70 -> 35
     - Align Hungary: Focus duration 70 -> 35


### Tank designer
 - Main armaments
    - Close support gun: breakthrough 9.5 -> 6

    - Small Cannon 1: soft attack 12.5 -> 17
                      hard attack 10 -> 11.5
                      breakthrough 7 -> 4
                      piercing 30 -> 29

    - Small Cannon 2: soft attack 19 -> 25
                      hard attack 10 -> 14
                      breakthrough 9.5 -> 6.5
                      piercing 30 -> 34
    
    - Meduim cannon 1: soft attack 22.5 -> 23.5
                       hard attack 15 -> 16
                       piercing 40 -> 44

    - Meduim cannon 2: soft attack 27.5 - > 28.5
                       hard attack 18 -> 19
                       piercing 61 -> 67

    - Rocket Artillery 1: soft attack 51 -> 48

    - Rocket Artillery 2 socft attack 64 -> 59.5

    - Basic High-velocity gun: soft attack 12.5 -> 10
                               hard attack 20 -> 22.5
    
    - Improved High-velocity gun: soft attack 15 -> 12
                                  hard attack 22 -> 25.5

 - Turrets
    - Heavy two man turret: production cost 4 -> 4.5

    - Heavy three man turret: production cost 5.5 -> 6.5

- Engine
    - Diesel engine: Fule consumtion 1.5 -> 2.5

### Artillery tech
 - Moved Small Cannon: Inter-war artillery -> Improved artillery

 - Moved Improved High-velocity gun: Improved Anti-tank upgrade II -> Improved Anti-tank upgrade 
 
### 3.5.0
### Focus Trees
- Added NEW reworked Japanese focus tree

- Rearanged some focuses for USA
    - Added evet "investigation of Mark 14 Torpede" from Bureau of ships [Allow for removal of bureau of ships spirit]
    - Fund the navy 0 -> 2 dockyards from focus

- Further developed the "learn from the germans" path for Finland

- Fixed issue with Manchukuo factories spawning randomly across the world

### Tank designer
- locked slots based on tech level
    - interwar and basic tank chassis will now have two slots locked
    - improved chassis will now have one slot locked
    - no slots locked for advanced, modern and super-heavy chassis

- Main armaments
    - heavy cannon 1: soft attack 31 -> 30
                      hard attack 25 -> 24
                      piercing 60 -> 55

    - heavy cannon 2: soft attack `37.5`->`36`
`                      hard attack 27.5 -> 27
                      piercing 90 -> 80

    - heavy cannon 3: soft attack 42.5 -> 41
                      hard attack 37.5 -> 35
                      piercing 125 -> 108

    - High-velocity gun 1: piercing 90 -> 80

    - High-velocity gun 2: piercing 135 -> 120

    - High-velocity gun 3: piercing 188 -> 162
   
    - Medium gun 1: piercing 45 -> 40
    
    - Medium gun 2: piercing 68 -> 61
                   
- Armour 
    - Rivided armour: 0 -> -5% reliability

    - Welded armour: 0 -> +5% reliability
                     +10% -> 7.5% production cost

    - Cast armour: 0 -> +10% reliability 
                   +20% -> 15% production cost 

- Module balances changes
    - Diesel engine production cost: 1 -> 1.5 [To bring it in line with gasoline engine]

    - Radio 1 production cost: 0.5 -> 0,75

    - Radio 3 production cost: 2.5 -> 2.25 [To make it scale equaly between modules]

    - Squeeze-bore adaptor: production cost 0 -> 1
                            hard attack +5% -> +10%
                            soft attack -0.05% -> -0.1%

    - Armour skirts: breakthrough 2 -> 3
                     defense 3 -> 4
                     production cost 2 -> 1.5

### Artillery 
- Reduced rescource cost for AT
    - All AT tungsten cost: 2 -> 1 

- Reduced piercing of AA
    -  Anti Air 2 piercing: 60 -> 50
    -  Anti-Air 3 piercing: 88 -> 75

### Army spirits
- Tip of the Spear 
    - Naval invasion planning 25% -> 15%
    - Special forces capacity -10% -> 0%

- Proper heritage
    - cavalry attack 0.3 -> 0.25
	- cavalry defence 0.3 -> 0.25

- Operational Reserves 
    - Defence 15% -> 10%
    - Division HP 25% - 15%

- Aggressive Reconnaisance
    - initative +25% -> 0%
    - reinforce rate 0% -> 3%
    - Supply Consumtion 10% -> 5%

### Navy spirits
- Bureau of ordnance
    - Torpedo hit chance -10% -> -25%
    - Convoy raiding effeiciency 0 -> -25%

### Air spirits
- Dive Bombing
    - Naval aircraft reseach speed +25% -> 0 [Used to stack with dive bomber reseach speed]    

- Industry Liasos
    - Naval aircraft reseach speed +15% -> 0 [Used to stack with light aircraft reseach speed]

### Land doctrine

- Mass - Human wave offensice 
    - Recritable population 5% -> 2.5
    - reinforce rate 15% -> 8%
### 3.4.1

- Reduced the land modifier bonus for each experience level `+25%` -> `20%`
- Added two new quotes
- Added two console commands called "SPT_No_Resource_Penalty" and "SPT_Remove_No_Resource_Penalty" that remove resource penalty [So you dont have to trade in playtests so its like you are getting tradebacks]

#### AOI
- Gave cores on all their own states with the decision to form them

#### Spain
- Increased time for "Impending Carlist Uprising" mission `316` -> `386`

#### Rules
- Changed Diplomacy rule 2 to "Military access and docking rights are banned except between Finland and Germany."

#### Finland
- Added a new post Winter War focus branch

### 3.4.0

-Updated to version 1.12.10

#### Manchuko
- Added new focus tree!

#### Japan
- Reduced manchuko focuses length `70` -> `35`

#### Finland
- Clarified Winter War tooltip 

#### Rule Changes
- Change Soviet rule 9 to "No naval invading or paradropping Finland during the Winter War."

#### Tank Designer
- Chasis:
    - Heavies can only use heavy turrets [no more sneaking on light turret on heavy tds]


### 3.3.1

#### Rule Changes
- Added rule "No naval invading Finland during the Winter War"

#### Finland
- Made Finland unable to join factions
- Nerfed some army buffs [ Finlands infantry stats were too strong atm]
- Increased mobilisation speed for Finland

#### Soviet Union
- Readded the change to "Turkey Seizes Control Over the Bosporus" event so war support gained is now `5% -> 10%` [ Buff soviets as they have a new front/ extra enemy. More might be necesary ]

#### Tank Designer
- Chasis:
    - Heavy 1:
        - Decreased ic cost `+14 -> +8` [Make heavies more viable]
    - Heavy 2:
        - Decreased ic cost `+14 -> +10` 
- Secondary Turrets:
    - Heavy MG:
        - Decreased hard attack `2` -> `1`
    - Small Cannon:
        - Reduced soft attack `7.5` -> `3` [nerf module which nerfs mediums as a whole]
- Main Armaments:
    - Decreased chromium cost for heavy cannons `2` -> `1`

### 3.3 - Winter War Update

#### Finland
- Added Finland to list of playable countries
- Added a new Finland focus tree and starting conditions
- Added a new winter war mechanic

#### Soviet Union
- Added a new winter war mechanic
- Removed "Baltic Security" focus
- Made "Secure Leningrad" only available after 1.11.1939

#### Rule Changes
- Changed rule 4 to "Must start the winter war before 01.03.1940"
- Added a new page and rules for Finland

### 3.2.5.1

- Changed some gfx icons for Hungary, Japan and Romania

#### Hunary
- Removed "Boost Hungarian Aviation Industry" as a prerequisite for "Indigenous designs" [Allows Hungary to rush fighters now italy can't]
- Merged "Synthetic Industry" into "Autarky" focus
- Increased number of mils received from "Boost Hungarian Aviation Industry" `2` -> `4`

#### Japan
- Replaced getting a variant with researching fighter 2 for "The Zero" focus


### 3.2.5

- Removed quick access to the countries that arent playable on the 1936 start date

#### Lend Lease Rules
- Added rule No lend leasing planes to Spain during or before the Spanish civil war"

#### USA
- Removed the ahistorical options from the panay incident event chain

#### France
- Removed the requirement for Charles De Gaulle to be leader to complete for "Appeal to the French Nation" in the Free France focus tree

#### Soviet Union
- Reduce length of "Desperate Measures" idea from "Desperate Measures" focus `365`-> `180`

#### Japan
- Addd `+20%` factory output to "State Shintoism" idea [(Hopefully) Temporary buff to japan]


### 3.2.4

- Made the province underneath Alamein passable [Try and spice up africa front little bit more]
- Reduce the cooldown on using a railway after capturing it `10` -> `5` [Speed up combat slightly]
- Gave each minor `100` convoys at the start of the game [Prevent lend lease issues]
- Incorperated "Spy Agency Reminders" into the mod
- Made England automatically guarantee Poland at the start of the game

#### Ethiopia
- Removed focus path where ethiopia rebel from Italy and declare independence

#### England
- Added decision to annex Malaya:
    - Takes `90` days
    - Gives `15%` consumer goods while annexing
    - Costs `50` pp
    - Can't be taken if at war and cancels if UK joins a war.
    - Also gives `100` compliance in the states

#### Germany
- Shortened some focus lengths `70` -> `56` days
    - "Anschluss"
    - "Demand Sudetenland"
    - "Fate of Czechoslovakia"
    - "Alliance with Spain"
    - "Reassert Eastern Claims"
- Shortened all the navy branch focus lengths to `35` days
- Shortened some focus lengths `70` -> `35` days
    - "First Vienna Award"
    - "Second Vienna Award"
    - "Anti-Comintern Pact"
- Shortened "Danzig or War" focus length `70` -> `7` days
- Moved "Improve National Spirit" to below "War With France"
- Moved "Form the Reichskommissariats" to below "Anschluss"
- Created a new focus branch that all take `70` days and will give `+50%` compliance when Germany caps their respective countries
    - Poland
    - Benelux (Netherlands and Belgium)
    - France
    - Scandanavia (Denmark and Norway)
- Change the icons on many focuses

#### Japan
- Added decision to annex Manchuko and gain 100% Compliance if there's not a player on it


### 3.2.3 - Update to 1.12.7 and small changes
 
- Updated to 1.12.7 hoi4 version 
- Removed 1939 start 

#### Hungary
- Fixed "Claim overlordship over slovakia" to require the correct states
#### Italy
- Remove decision to form greater italy [Getting all cores is too op and the med war already buffs italian success]
#### Romania
- Removed "His majesty's loyal government" branch and the "King michaels coup" focus [Ahistorical focuses and requires hungary to not exist or be a puppet]
#### Raj
- Fixed focuses overlapping
#### Army Spirits
- Proper Heritage:
    - Decreased cavalry attack `+50% -> +30%` [too op atm]
    - Decreased cavalry defense `+50% -> +30%`


### 3.2.2 - Balancing Update

#### Axis Rules
- Removed rule number 2 for Italy, allowing them to join the war whenever they wish

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
