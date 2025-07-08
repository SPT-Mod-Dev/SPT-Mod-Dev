NDefines = {
    NGame = {
        LAG_DAYS_FOR_LOWER_SPEED = 30
        LAG_DAYS_FOR_PAUSE = 18
        GAME_SPEED_SECONDS = { 0.6, 0.3, 0.2, 0.08, 0.0 }
    }
    NCountry = {
        NAVAL_EQUIPMENT_BASE_COST = 0,
        NAVAL_EQUIPMENT_RAMP_COST = 0,
        SPECIAL_FORCES_CAP_MIN = 64,
        AIR_SUPPLY_CONVERSION_SCALE = 0.03,
        EVENT_PROCESS_OFFSET = 30,
    },

    NProduction = {
        EQUIPMENT_MODULE_ADD_XP_COST = 0,
        EQUIPMENT_MODULE_REPLACE_XP_COST = 0,
        EQUIPMENT_MODULE_CONVERT_XP_COST = 0,
        EQUIPMENT_MODULE_REMOVE_XP_COST = 0,
        MIN_POSSIBLE_TRAINING_MANPOWER = 1000000,
    },

    NMilitary = {
        BASE_DIVISION_BRIGADE_GROUP_COST = 0,
        BASE_DIVISION_BRIGADE_CHANGE_COST = 0,
        BASE_DIVISION_SUPPORT_SLOT_COST = 0,
        MAX_ARMY_EXPERIENCE = 999,
        MAX_NAVY_EXPERIENCE = 999,
        MAX_AIR_EXPERIENCE = 999,
        NAVAL_EQUIPMENT_BASE_COST = 0,
        NAVAL_EQUIPMENT_RAMP_COST = 0,
        EXPERIENCE_COMBAT_FACTOR = 0.2,
        ARMOR_VS_AVERAGE = 0.25,
        PEN_VS_AVERAGE = 0.3,
        ENEMY_AIR_SUPERIORITY_IMPACT = 0.25,
        ENEMY_AIR_SUPERIORITY_DEFENSE = 0.5,
        ENEMY_AIR_SUPERIORITY_DEFENSE_STEEPNESS = 80,
        AIR_SUPPORT_BASE = 0.2,
    },

    NSupply = {
        RAILWAY_CONVERSION_COOLDOWN = 5,
    },

    NBuildings = {
        ANTI_AIR_SUPERIORITY_MULT = 25,
    },

    NAir= {
        ANTI_AIR_MAXIMUM_DAMAGE_REDUCTION_FACTOR = 0.9,
        ANTI_AIR_ATTACK_TO_DAMAGE_REDUCTION_FACTOR = 0.4,
    },

    NNavy = {
        CARRIER_STACK_PENALTY 									        = 6,         --The most efficient is 4 carriers in combat. 5+ brings the penalty to the amount of wings in battle.
        CARRIER_STACK_PENALTY_EFFECT 									= 0.5,       --Each carrier above the optimal amount decreases the amount of airplanes being able to takeoff by such %.
        MIN_GUN_COOLDOWN                                                = 1,
        DEPTH_CHARGES_HIT_CHANCE_MULT 									= 1.1,       --"multiplies hit chance of small guns" says the comment, tf does i actually do
        DEPTH_CHARGES_DAMAGE_MULT 										= 0.7,       --multiplies damage of depth charges
        DEPTH_CHARGES_HIT_PROFILE 										= 100.0,     --hit profile for depth charges
        SUBMARINE_BASE_TORPEDO_REVEAL_CHANCE 							= 0.1,       --Chance of a submarine being revealed when it fires. 1.0 is 100%. this chance is then multiplied with modifier ~~created by comparing firer's visibiility and target's detection~~ depending on the subs sub visibility
        SUBMARINE_REVEAL_BASE_CHANCE 									= 11,        --Base factor for submarine detection in Battles. It's modified by the difference of a spotter's submarines detection vs submarine visibility. Use this variable for game balancing. setting this too low will cause bad spotting issues.
        SUBMARINE_REVEAL_POW 											= 3.0,		 --A scaling factor that is applied to the reveal chance in order to make large differences in detection vs visibility more pronounced
        CONVOY_HIT_PROFILE                                               = 105,
        CONVOY_RAID_MAX_REGION_TO_TASKFORCE_RATIO                        = 1,
        MISSION_SUPREMACY_RATIOS = { -- supremacy multipliers for different mission types
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
        },
        NAVY_PIERCING_THRESHOLDS = {					-- Our piercing / their armor must be at least this value to deal damage fraction equal to the index in the array below [higher number = higher penetration]. If armor is 0, 1.00 will be returned.
            2.00,
            1.00,
            0.75,
            0.50,
            0.33,
            0.20,
            0.10,
            0.00 --there isn't much point setting this lower than 0
        },

        NAVY_PIERCING_THRESHOLD_CRITICAL_VALUES = {	-- 0 armor will always receive maximum damage (so add overmatching at your own peril). the system expects at least 2 values, with no upper limit.
            2.00,
            1.00,
            0.75,
            0.50,
            0.33,
            0.20,
            0.10,
            0.00 -- For criticals, you could reduce crit chance unlike damage in army combat, but we do not for now.
        },

        NAVY_PIERCING_THRESHOLD_DAMAGE_VALUES = {	-- 0 armor will always receive maximum damage (so add overmatching at your own peril). the system expects at least 2 values, with no upper limit.
            1.00,
            1.00,
            0.70,
            0.40,
            0.30,
            0.20,
            0.10,
            0.05 --
        },

        -- all of these NEED to be the same size!!!!
    },

    NDiplomacy = {
        EMBARGO_THREAT_THRESHOLD = 50,
        PEACE_SCORE_DISTRIBUTION = { 1, 1, 1, 1, 1 },
    },

    NProject = {
        BREAKTHROUGH_DAILY_TECHNOLOGY_GAIN = 9,
    },
},