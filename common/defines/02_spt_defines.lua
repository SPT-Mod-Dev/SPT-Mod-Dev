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
NDefines.NCountry.AIR_SUPPLY_CONVERSION_SCALE = 0.03

NDefines.NSupply.RAILWAY_CONVERSION_COOLDOWN = 5

NDefines.NMilitary.EXPERIENCE_COMBAT_FACTOR = 0.2

NDefines.NIndustrialOrganisation.DESIGN_TEAM_CHANGE_XP_COST = 1

NDefines.NMilitary.ARMOR_VS_AVERAGE = 0.25
NDefines.NMilitary.PEN_VS_AVERAGE = 0.3

NDefines.NNavy.CARRIER_STACK_PENALTY 									        = 4         --The most efficient is 4 carriers in combat. 5+ brings the penalty to the amount of wings in battle.
NDefines.NNavy.CARRIER_STACK_PENALTY_EFFECT 									= 0.15      --Each carrier above the optimal amount decreases the amount of airplanes being able to takeoff by such %.
NDefines.NNavy.MIN_GUN_COOLDOWN = 1
NDefines.NNavy.DEPTH_CHARGES_HIT_CHANCE_MULT 									= 1.1       --"multiplies hit chance of small guns" says the comment, tf does i actually do
NDefines.NNavy.DEPTH_CHARGES_DAMAGE_MULT 										= 0.7       --multiplies damage of depth charges
NDefines.NNavy.DEPTH_CHARGES_HIT_PROFILE 										= 100.0     --hit profile for depth charges
NDefines.NNavy.SUBMARINE_BASE_TORPEDO_REVEAL_CHANCE 							= 0.1       --Chance of a submarine being revealed when it fires. 1.0 is 100%. this chance is then multiplied with modifier ~~created by comparing firer's visibiility and target's detection~~ depending on the subs sub visibility
NDefines.NNavy.SUBMARINE_REVEAL_BASE_CHANCE 									= 11        --Base factor for submarine detection in Battles. It's modified by the difference of a spotter's submarines detection vs submarine visibility. Use this variable for game balancing. setting this too low will cause bad spotting issues.
NDefines.NNavy.SUBMARINE_REVEAL_POW 											= 3.0		--A scaling factor that is applied to the reveal chance in order to make large differences in detection vs visibility more pronounced
NDefines.NNavy.GUN_HIT_PROFILES = { -- hit profiles for guns, if target ih profile is lower the gun will have lower accuracy
    90.0,	-- big guns
    110.0,	-- torpedoes
    45.0,	-- small guns
}
NDefines.NNavy.CONVOY_HIT_PROFILE                                               = 105
NDefines.NNavy.CONVOY_RAID_MAX_REGION_TO_TASKFORCE_RATIO                        = 1

NDefines.NDiplomacy.EMBARGO_THREAT_THRESHOLD = 50

NDefines.NDiplomacy.PEACE_SCORE_DISTRIBUTION = { 1, 1, 1, 1, 1 }

NDefines.NProject.BREAKTHROUGH_DAILY_TECHNOLOGY_GAIN = 9
