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

NDefines.NBuildings.ANTI_AIR_SUPERIORITY_MULT = 25

NDefines.NMilitary.ARMOR_VS_AVERAGE = 0.25
NDefines.NMilitary.PEN_VS_AVERAGE = 0.3
NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_IMPACT = -0.25
NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_DEFENSE = 0.5
NDefines.NMilitary.ENEMY_AIR_SUPERIORITY_DEFENSE_STEEPNESS = 80
NDefines.NMilitary.AIR_SUPPORT_BASE = 0.2
NDefines.NAir.ANTI_AIR_MAXIMUM_DAMAGE_REDUCTION_FACTOR = 0.9
NDefines.NAir.ANTI_AIR_ATTACK_TO_DAMAGE_REDUCTION_FACTOR = 0.4


NDefines.NNavy.CARRIER_STACK_PENALTY 									        = 6         --The most efficient is 4 carriers in combat. 5+ brings the penalty to the amount of wings in battle.
NDefines.NNavy.CARRIER_STACK_PENALTY_EFFECT 									= 0.5      --Each carrier above the optimal amount decreases the amount of airplanes being able to takeoff by such %.
NDefines.NNavy.MIN_GUN_COOLDOWN                                                 = 1
NDefines.NNavy.DEPTH_CHARGES_HIT_CHANCE_MULT 									= 1.1       --"multiplies hit chance of small guns" says the comment, tf does i actually do
NDefines.NNavy.DEPTH_CHARGES_DAMAGE_MULT 										= 0.7       --multiplies damage of depth charges
NDefines.NNavy.DEPTH_CHARGES_HIT_PROFILE 										= 100.0     --hit profile for depth charges
NDefines.NNavy.SUBMARINE_BASE_TORPEDO_REVEAL_CHANCE 							= 0.1       --Chance of a submarine being revealed when it fires. 1.0 is 100%. this chance is then multiplied with modifier ~~created by comparing firer's visibiility and target's detection~~ depending on the subs sub visibility
NDefines.NNavy.SUBMARINE_REVEAL_BASE_CHANCE 									= 11        --Base factor for submarine detection in Battles. It's modified by the difference of a spotter's submarines detection vs submarine visibility. Use this variable for game balancing. setting this too low will cause bad spotting issues.
NDefines.NNavy.SUBMARINE_REVEAL_POW 											= 3.0		--A scaling factor that is applied to the reveal chance in order to make large differences in detection vs visibility more pronounced
NDefines.NNavy.MISSION_SUPREMACY_RATIOS = { -- supremacy multipliers for different mission types
    0.0, -- HOLD
    1.0, -- PATROL
    0.5, -- STRIKE FORCE
    0.5, -- CONVOY RAIDING
    0.5, -- CONVOY ESCORT
    0.3, -- MINES PLANTING
    0.3, -- MINES SWEEPING
    0.0, -- TRAIN
    0.0, -- RESERVE_FLEET
    1.0, -- NAVAL_INVASION_SUPPORT
}
NDefines.NNavy.NAVY_PIERCING_THRESHOLDS = {					-- Our piercing / their armor must be at least this value to deal damage fraction equal to the index in the array below [higher number = higher penetration]. If armor is 0, 1.00 will be returned.
2.00,
1.00,
0.75,
0.50,
0.33,
0.20,
0.10,
0.00 --there isn't much point setting this lower than 0
}

NDefines.NNavy.NAVY_PIERCING_THRESHOLD_CRITICAL_VALUES = {	-- 0 armor will always receive maximum damage (so add overmatching at your own peril). the system expects at least 2 values, with no upper limit.
    2.00,
    1.00,
    0.75,
    0.50,
    0.33,
    0.20,
    0.10,
    0.00 -- For criticals, you could reduce crit chance unlike damage in army combat, but we do not for now.
}

NDefines.NNavy.NAVY_PIERCING_THRESHOLD_DAMAGE_VALUES = {	-- 0 armor will always receive maximum damage (so add overmatching at your own peril). the system expects at least 2 values, with no upper limit.
    1.00,
    1.00,
    0.70,
    0.40,
    0.30,
    0.20,
    0.10,
    0.05 --
} -- all of these NEED to be the same size!!!!

NDefines.NNavy.CONVOY_RAID_MAX_REGION_TO_TASKFORCE_RATIO                        = 1

NDefines.NDiplomacy.EMBARGO_THREAT_THRESHOLD = 50

NDefines.NDiplomacy.PEACE_SCORE_DISTRIBUTION = { 1, 1, 1, 1, 1 }

NDefines.NProject.BREAKTHROUGH_DAILY_TECHNOLOGY_GAIN = 9

-- SPTChange add manpower increase
NDefines.NProduction.MIN_POSSIBLE_TRAINING_MANPOWER = 1000000

NDefines.NAI.GIVE_STATE_CONTROL_MIN_CONTROLLED = 0
NDefines.NAI.GIVE_STATE_CONTROL_MIN_CONTROL_DIFF = 0
NDefines.NAir.AIR_DEPLOYMENT_DAYS = 0

NDefines.NGame.COMBAT_LOG_MAX_MONTHS = 6
NDefines_Graphics.NGraphics.UNITS_DISTANCE_CUTOFF = 100
NDefines_Graphics.NGraphics.SHIPS_DISTANCE_CUTOFF = 200
NDefines_Graphics.NGraphics.UNIT_ARROW_DISTANCE_CUTOFF = 500
NDefines_Graphics.NGraphics.UNITS_ICONS_DISTANCE_CUTOFF = 700
NDefines_Graphics.NGraphics.NAVAL_COMBAT_DISTANCE_CUTOFF = 1000
NDefines_Graphics.NGraphics.ADJACENCY_RULE_DISTANCE_CUTOFF = 1300
NDefines_Graphics.NGraphics.LAND_COMBAT_DISTANCE_CUTOFF = 800
NDefines_Graphics.NGraphics.SUPPLY_ICON_DISTANCE_CUTOFF = 1500
NDefines_Graphics.NGraphics.PROV_CONSTRUCTION_ICON_DISTANCE_CUTOFF = 300
NDefines_Graphics.NGraphics.STATE_CONSTRUCTION_ICON_DISTANCE_CUTOFF = 600
NDefines_Graphics.NGraphics.TREE_FADE_NEAR = 150.0
NDefines_Graphics.NGraphics.TREE_FADE_FAR = 250.0

NDefines.NAI.LENDLEASE_FRACTION_OF_PRODUCTION = 0
NDefines.NAI.LENDLEASE_FRACTION_OF_STOCKPILE = 0
NDefines.NAI.MINIMUM_EQUIPMENT_TO_ASK_LEND_LEASE = -100000
NDefines.NAI.MINIMUM_CONVOY_TO_ASK_LEND_LEASE = 0

NDefines.NProduction.LICENSE_IC_COST_YEAR_INCREASE = 0