NDefines.NCountry.NAVAL_EQUIPMENT_BASE_COST = 0
NDefines.NCountry.NAVAL_EQUIPMENT_RAMP_COST = 0

NDefines.NProduction.EQUIPMENT_MODULE_ADD_XP_COST = 0
NDefines.NProduction.EQUIPMENT_MODULE_REPLACE_XP_COST = 0
NDefines.NProduction.EQUIPMENT_MODULE_CONVERT_XP_COST = 0
NDefines.NProduction.EQUIPMENT_MODULE_REMOVE_XP_COST = 0

NDefines.NMilitary.BASE_DIVISION_BRIGADE_GROUP_COST = 0
NDefines.NMilitary.BASE_DIVISION_BRIGADE_CHANGE_COST = 0
NDefines.NMilitary.BASE_DIVISION_SUPPORT_SLOT_COST = 0

NDefines.NMilitary.MAX_ARMY_EXPERIENCE = 999
NDefines.NMilitary.MAX_NAVY_EXPERIENCE = 999
NDefines.NMilitary.MAX_AIR_EXPERIENCE = 999

NDefines.NMilitary.NAVAL_EQUIPMENT_BASE_COST = 0
NDefines.NMilitary.NAVAL_EQUIPMENT_RAMP_COST = 0

NDefines.NCountry.SPECIAL_FORCES_CAP_MIN = 64

NDefines.NSupply.RAILWAY_CONVERSION_COOLDOWN = 5

NDefines.NMilitary.EXPERIENCE_COMBAT_FACTOR = 0.2

NDefines.NIndustrialOrganisation.DESIGN_TEAM_CHANGE_XP_COST = 1

NDefines.NMilitary.ARMOR_VS_AVERAGE = 0.25
NDefines.NMilitary.PEN_VS_AVERAGE = 0.3

NDefines.NNavy.MIN_GUN_COOLDOWN = 1
NDefines.NNavy.DEPTH_CHARGES_HIT_CHANCE_MULT 									= 1.1       #"multiplies hit chance of small guns" says the comment, tf does i actually do
NDefines.NNavy.DEPTH_CHARGES_DAMAGE_MULT 										= 1         #multiplies damage of depth charges
NDefines.NNavy.DEPTH_CHARGES_HIT_PROFILE 										= 90.0      #hit profile for depth charges
NDefines.NNavy.SUBMARINE_BASE_TORPEDO_REVEAL_CHANCE 							= 0.75       #Chance of a submarine being revealed when it fires. 1.0 is 100%. this chance is then multiplied with modifier ~~created by comparing firer's visibiility and target's detection~~ depending on the subs sub visibility
NDefines.NNavy.SUBMARINE_REVEAL_BASE_CHANCE 									= 88        #Base factor for submarine detection in Battles. It's modified by the difference of a spotter's submarines detection vs submarine visibility. Use this variable for game balancing. setting this too low will cause bad spotting issues.
NDefines.NNavy.SUBMARINE_REVEAL_POW 											= 3.0		#A scaling factor that is applied to the reveal chance in order to make large differences in detection vs visibility more pronounced
NDefines.NNavy.GUN_HIT_PROFILES = { -- hit profiles for guns, if target ih profile is lower the gun will have lower accuracy
    90.0,	-- big guns
    120.0,	-- torpedoes
    45.0,	-- small guns
},