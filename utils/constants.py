# Constants file

# The path is where the chromedriver.exe is, but without the .exe at the end.

# That's is not the location of the chromedriver folder, it's the executable file itself, \\chromedriver.exe but without the .exe
# Example for Windows users: chrome_driver_path = "C:\\Program Files (x86)\\chromedriver folder\\chromedriver"

chrome_driver_path = "/Users/leonardoluiz/.wdm/drivers/chromedriver/mac64/120.0.6099.71/chromedriver-mac-arm64/chromedriver"

gameDataURL = "https://www.streamraiders.com/api/game/"

# "https://d1vngzyege2qd5.cloudfront.net/prod1/od/${captainId}-${battleGroundId}.txt"
mapPlacements = "https://d1vngzyege2qd5.cloudfront.net/prod1/"
mapPlacements2 = "https://d2k2g0zg1te1mr.cloudfront.net/maps/"

regular_chests = ["chestbronze", "chestsilver", "chestgold"]
map_nodes_path = "assets/map_nodes.json"
map_units_path = "assets/map_units.json"
quest_nodes_path = "assets/quest_nodes.json"
obstacles_path = "assets/obstacles.json"

retry_states = ["OVER_UNIT", "OUTSIDE_PLACEMENT", "OVER_OBSTACLE"]

bad_raid = ["INVALID_RAID_STATE:",
             "PERIOD_ENDED", 
             "MAX_RAIDS",
             "REQUIRES_VERSUS_CODE",
             "REQUIRES_DUNGEON_CODE",
             "NOT_IN_RAID",
             "UNIT_NOT_OWNED"]

default_entry = [
    {
        "name": "",
        "token": "",
        "scapmpid": "",
        "scsession": "",
        "powered_on": True,
        "preserve_loyalty": 0,
        "switch_if_preserve_loyalty": False,
        "switch_on_idle": True,
        "minimum_idle_time": 15,
        "unlimited_campaign": False,
        "unlimited_clash": False,
        "unlimited_duels": False,
        "unlimited_dungeons": False,
        "any_captain": True,
        "only_masterlist": False,
        "masterlist": ["", "", ""],
        "ignore_blocklist": False,
        "blocklist": ["", "", ""],
        "temporary_ignore": [{"capNm": "", "time": ""}],
        "user_agent": "",
        "proxy": "",
        "proxy_user": "",
        "proxy_password": "",
        "use_potions": False,
        "has_pass": False,
        "userId": "",
        "otherUserId": "",
        "favorites_only": False,
        "favoriteCaptainIds": "",
        "slots": 3,
        "use_skins": True,
        "units": "",
    }
]

units_dict = [
    {"type": "melee", "name": "amazon", "alt": ""},
    {"type": "ranged", "name": "archer", "alt": ""},
    {"type": "ranged", "name": "artillery", "alt": ""},
    {"type": "assassin", "name": "alliesballoonbuster", "alt": "balloonbuster"},
    {"type": "melee", "name": "barbarian", "alt": ""},
    {"type": "melee", "name": "berserker", "alt": ""},
    {"type": "armored", "name": "blob", "alt": ""},
    {"type": "ranged", "name": "bomber", "alt": ""},
    {"type": "assassin", "name": "buster", "alt": ""},
    {"type": "armored", "name": "centurion", "alt": ""},
    {"type": "support", "name": "fairy", "alt": ""},
    {"type": "support", "name": "flagbearer", "alt": ""},
    {"type": "assassin", "name": "flyingarcher", "alt": "flyingrogue"},
    {"type": "melee", "name": "gladiator", "alt": ""},
    {"type": "support", "name": "healer", "alt": ""},
    {"type": "melee", "name": "lancer", "alt": ""},
    {"type": "ranged", "name": "mage", "alt": ""},
    {"type": "support", "name": "monk", "alt": ""},
    {"type": "ranged", "name": "musketeer", "alt": ""},
    {"type": "support", "name": "necromancer", "alt": ""},
    {"type": "armored", "name": "orcslayer", "alt": ""},
    {"type": "armored", "name": "alliespaladin", "alt": "paladin"},
    {"type": "assassin", "name": "rogue", "alt": ""},
    {"type": "support", "name": "saint", "alt": ""},
    {"type": "assassin", "name": "shinobi", "alt": ""},
    {"type": "assassin", "name": "spy", "alt": ""},
    {"type": "armored", "name": "tank", "alt": ""},
    {"type": "support", "name": "templar", "alt": ""},
    {"type": "armored", "name": "vampire", "alt": ""},
    {"type": "melee", "name": "warbeast", "alt": ""},
    {"type": "melee", "name": "warrior", "alt": ""},
]

py_accounts = "pyraiders_accounts.json"
py_unauthorized_accounts = "py_unauthorized_accounts.json"
logger = "logger.txt"
keys_to_remove = [
    "NodeDifficulty",
    "MapTags",
    "OnLoseDialog",
    "OnStartDialog",
    "OnWinDialog",
]
quest_keys_rm = [
    "AssetPathOverride",
    "AssetScaleOverride",
    "AutoCompleteCost",
    "CompletionCooldown",
    "CurrencyIdRequirement",
    "CurrencyMaxRequirement",
    "CurrencyMinRequirement",
    "Description",
    "Mode",
    "Objective",
    "RewardAmount",
    "RewardItemId",
    "Title",
    "Type",
    "UnitAsset",
    "UnitLevelRequirement",
    "UnitTypeRequirement",
]

units_keys_rm = [
    "raidPlacementsId",
    "userId",
    "skin",
    "unitId",
    "specializationUid",
    "onPlanIcon",
    "isSpell",
    "stackRaidPlacementsId",
]
unit_values_rm = [
    "AttackRate",
    "AttackType",
    "BaseAction",
    "BaseActionSelfVfxUid",
    "Damage",
    "DamageDelay",
    "Description",
    "DisplayName",
    "EffectiveCircleDataUid",
    "ExtraHitSize",
    "HP",
    "Heal",
    "IsFlying",
    "Level",
    "OnDeathAction",
    "OnDeathActionSelfVfxUid",
    "OnDefeatAction",
    "OnKillAction",
    "PassThroughList",
    "PlacementVFX",
    "Level",
    "OnDeathAction",
    "OnDeathActionSelfVfxUid",
    "OnDefeatAction",
    "OnKillAction",
    "PassThroughList",
    "PlacementVFX",
    "Power",
    "ProjectileUid",
    "Range",
    "Rarity",
    "RemainsAsset",
    "Role",
    "ShowTeamIndicator",
    "SpecialAbilityActionUid",
    "SpecialAbilityDescription",
    "SpecialAbilityRate",
    "SpecialAbilitySelfVfxUid",
    "Speed",
    "StartBuffsList",
    "StrongAgainstTagsList",
    "TagsList",
    "TargetPriorityTagsList",
    "TargetTeam",
    "TargetingPriorityRange",
    "Triggers",
    "Uid",
    "UnitTargetingType",
    "UnitType",
    "UpgradeCurrencyType",
    "WeakAgainstTagsList",
]


type_dict = {
    "1": "unlimited_campaign",
    "2": "unlimited_clash",
    "5": "unlimited_duels",
    "3": "unlimited_dungeons",
}

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.37",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.4",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.76",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.6",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:109.0) Gecko/20100101 Firefox/115.",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.4",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko DNT: 1",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.98",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.88",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.31",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.10",
    "Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.931 YaBrowser/23.9.3.931 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 OPR/95.0.0.",
    "Mozilla/5.0 (X11; CrOS x86_64 14541.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.3",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.81",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.57",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 OPR/103.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.69",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0",
    "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.837 YaBrowser/23.9.4.837 Yowser/2.5 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (X11; Linux aarch64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "Mozilla/5.0 (X11; Linux i686 (x86_64)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; Tablet PC 2.0; Zoom 3.6.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.43",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.200",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.55",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Whale/3.23.214.10 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.70",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.68",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36,gzip(gfe)",
    "Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S901U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-S908U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-G991U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; SM-A515U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; SM-G973U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; moto g 5G (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; moto g power (2022)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; moto g power (2021)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Redmi Note 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 10; MAR-LX1A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 13; M2101K6G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 12; DE2118) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36",
    "Mozilla/5.0 (iPhone14,6; U; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19E241 Safari/602.1",
    "Mozilla/5.0 (iPhone14,3; U; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/19A346 Safari/602.1",
    "Mozilla/5.0 (iPhone13,2; U; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1",
    "Mozilla/5.0 (iPhone12,1; U; CPU iPhone OS 13_0 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/15E148 Safari/602.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/69.0.3497.105 Mobile/15E148 Safari/605.1",
    "Mozilla/5.0 (Linux; Android 12; SM-X906C Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 11; Lenovo YT-J706X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; Pixel C Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SGP771 Build/32.2.A.0.253; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/52.0.2743.98 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0.1; SHIELD Tablet K1 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.0; SM-T827R4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Safari/537.36",
    "Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-T550 Build/LRX22G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/3.3 Chrome/38.0.2125.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
    "Mozilla/5.0 (Nintendo Switch; WifiWebAuthApplet) AppleWebKit/601.6 (KHTML, like Gecko) NF/4.0.0.5.10 NintendoBrowser/5.1.0.13343",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
]

proxies = [
    "185.217.143.96:80",
    "162.248.225.125:80",
    "162.248.225.17:80",
    "222.138.76.6:9002",
    "220.248.70.237:9002",
    "113.143.37.82:9002",
    "20.157.194.61:80",
    "138.197.20.244:10007",
    "162.248.225.2:80",
    "51.68.220.201:8080",
    "162.248.225.30:80",
    "58.246.58.150:9002",
    "162.248.225.122:80",
    "162.248.225.98:80",
    "106.14.255.124:80",
    "120.234.203.171:9002",
    "51.91.109.83:80",
    "64.225.4.81:10004",
    "43.133.136.208:8800",
    "213.184.153.66:8080",
    "115.96.208.124:8080",
    "203.95.198.52:8080",
    "162.248.225.11:80",
    "183.234.85.26:9002",
    "51.15.242.202:8888",
    "185.217.143.125:80",
    "162.248.225.16:80",
    "190.60.82.22:80",
    "117.160.250.138:8899",
    "67.43.236.20:5729",
    "103.213.97.74:80",
    "39.104.79.145:1111",
    "58.20.248.139:9002",
    "162.248.225.8:80",
    "162.248.225.22:80",
    "136.144.155.182:3128",
    "120.197.40.219:9002",
    "47.74.152.29:8888",
    "162.248.225.131:80",
    "60.12.168.114:9002",
    "45.124.184.13:80",
    "162.248.225.135:80",
    "162.248.225.9:80",
    "117.50.186.65:80",
    "47.107.61.215:8000",
    "203.19.38.114:1080",
    "72.10.160.90:20005",
    "162.248.225.133:80",
    "133.232.90.155:80",
    "42.248.122.147:1080",
    "72.10.160.90:24447",
    "113.223.213.118:8089",
    "217.199.130.242:8080",
    "162.248.225.141:80",
    "64.225.4.17:10000",
    "159.65.186.46:10003",
    "162.248.225.34:80",
    "88.99.249.96:8284",
    "59.26.254.243:8193",
    "162.248.225.3:80",
    "8.209.68.1:81",
    "138.68.60.8:3128",
    "121.199.14.181:7890",
    "120.197.160.2:9002",
    "134.19.254.2:21231",
    "39.104.79.145:5000",
    "101.231.64.89:8443",
    "8.209.68.1:8192",
    "58.20.88.24:2323",
    "190.61.84.166:9812",
    "162.248.225.28:80",
    "94.130.177.190:9999",
    "47.97.21.151:1024",
    "8.209.68.1:8001",
    "47.88.3.19:8080",
    "221.153.92.39:80",
    "44.211.43.222:3128",
    "182.106.220.252:9091",
    "64.146.227.230:8080",
    "84.39.112.144:3128",
    "114.55.84.12:30001",
    "152.32.132.220:443",
    "185.101.159.130:80",
    "64.225.8.132:10007",
    "34.77.56.122:8080",
    "162.248.225.156:80",
    "162.246.248.214:80",
    "123.56.129.203:19",
    "213.212.220.210:8080",
    "113.208.119.142:9002",
    "47.243.242.70:8118",
    "39.107.33.254:8090",
    "47.243.242.70:45",
    "111.16.50.12:9002",
    "47.245.34.161:443",
    "162.248.225.182:80",
    "20.219.137.240:3000",
    "121.37.205.253:1000",
    "123.56.129.203:6666",
    "61.129.2.212:8080",
    "47.91.46.88:3128",
    "91.225.48.111:8888",
    "47.245.34.161:1080",
    "46.47.197.210:3128",
    "117.69.232.177:8089",
    "91.241.217.58:9090",
    "162.248.225.162:80",
    "162.248.225.23:80",
    "123.56.129.203:8085",
    "123.138.214.150:9002",
    "149.102.130.120:80",
    "162.248.225.18:80",
    "222.175.59.6:9002",
    "123.56.129.203:41890",
    "162.248.225.127:80",
    "135.181.36.242:80",
    "1.117.178.112:8080",
    "218.252.244.126:80",
    "121.37.205.253:8001",
    "198.49.68.80:80",
    "112.120.7.51:80",
    "68.183.143.134:80",
    "106.105.120.14:80",
    "176.99.2.43:1081",
    "162.248.225.14:80",
    "103.118.46.177:8080",
    "43.198.105.38:80",
    "139.224.190.222:8083",
    "119.28.117.127:31280",
    "113.195.207.249:9091",
    "47.91.65.23:3128",
    "217.12.20.250:80",
    "146.59.202.70:80",
    "129.150.39.9:80",
    "162.248.225.171:80",
    "159.223.183.111:80",
    "45.133.168.17:8080",
    "122.9.4.213:80",
    "120.46.197.14:41890",
    "67.43.227.227:4335",
    "80.99.87.3:80",
    "49.7.11.187:80",
    "162.248.225.39:80",
    "162.248.225.102:80",
    "162.248.225.215:80",
    "47.100.91.57:8080",
    "182.92.73.106:80",
    "162.248.225.224:80",
    "120.24.173.186:9999",
    "162.248.225.97:80",
    "162.248.225.128:80",
    "162.248.225.203:80",
    "82.223.102.92:9443",
    "37.120.173.115:80",
    "162.248.225.19:80",
    "47.56.110.204:8989",
    "162.248.225.47:80",
    "8.213.151.128:3128",
    "120.46.197.14:8989",
    "162.248.225.99:80",
    "101.132.25.152:199",
    "112.51.96.118:9091",
    "162.248.225.7:80",
    "117.71.155.25:8089",
    "162.248.225.201:80",
    "120.26.0.11:8880",
    "162.248.225.168:80",
    "101.132.25.152:873",
    "72.10.160.90:25277",
    "117.160.250.130:8899",
    "64.225.8.132:10009",
    "85.10.133.96:3128",
    "162.248.225.143:80",
    "61.72.254.69:8061",
    "183.230.162.122:9091",
    "38.180.86.43:80",
    "45.117.179.209:80",
    "178.54.21.203:8081",
    "60.188.102.225:18080",
    "111.20.217.178:9091",
    "51.75.206.209:80",
    "67.43.227.227:6961",
    "42.96.13.196:1914",
    "89.168.90.85:1080",
    "162.248.225.40:80",
    "188.166.56.246:80",
    "72.10.160.171:10879",
    "64.225.4.81:10008",
    "162.248.225.25:80",
    "47.113.219.226:8084",
    "61.158.175.38:9002",
    "47.114.101.57:8888",
    "162.248.225.214:80",
    "49.235.127.178:8000",
    "60.214.128.150:9091",
    "162.248.225.130:80",
    "36.64.162.194:8080",
    "60.210.40.190:9091",
    "139.59.55.213:80",
    "74.48.220.109:80",
    "5.2.180.169:8080",
    "222.127.136.229:32000",
    "162.248.225.120:80",
    "106.56.20.37:80",
    "103.153.154.6:80",
    "162.248.225.136:80",
    "162.248.225.32:80",
    "103.7.52.60:8118",
    "62.33.207.202:80",
    "43.156.0.125:8888",
    "93.177.229.164:9812",
    "72.10.160.171:22837",
    "67.43.227.227:29395",
    "47.113.221.120:80",
    "67.43.228.250:28891",
    "162.248.225.227:80",
    "162.248.225.36:80",
    "47.113.203.122:4153",
    "162.248.225.146:80",
    "162.248.225.115:80",
    "47.113.203.122:9090",
    "123.126.158.50:80",
    "43.251.132.133:8080",
    "117.160.250.138:80",
    "47.252.27.174:8009",
    "72.10.160.90:17205",
    "162.248.225.107:80",
    "196.1.95.124:80",
    "139.198.171.113:8081",
    "162.248.225.165:80",
    "162.248.225.202:80",
    "165.227.0.192:80",
    "8.209.255.13:3128",
    "49.156.47.162:8080",
    "196.223.129.21:80",
    "162.248.225.109:80",
    "64.225.8.132:10008",
    "47.89.184.18:3128",
    "103.216.49.233:8080",
    "162.248.225.38:80",
    "212.108.155.205:9090",
    "117.158.146.215:9091",
    "162.248.225.159:80",
    "42.96.5.251:6737",
    "47.88.29.108:8989",
    "39.107.89.178:80",
    "47.88.29.108:5000",
    "117.160.250.133:8899",
    "188.166.17.18:8881",
    "62.33.207.202:3128",
    "120.77.148.138:8080",
    "123.30.154.171:7777",
    "64.225.4.81:10002",
    "162.248.225.37:80",
    "5.161.103.41:88",
    "149.249.32.86:80",
    "103.153.62.221:3125",
    "47.91.104.88:3128",
    "47.106.107.212:3128",
    "202.61.204.51:80",
    "162.248.225.175:80",
    "218.57.210.186:9002",
    "117.160.250.132:8899",
    "162.248.225.140:80",
    "162.248.225.137:80",
    "162.248.225.157:80",
    "117.160.250.134:8899",
    "153.101.67.170:9002",
    "140.238.10.229:21000",
    "27.109.135.144:80",
    "85.172.0.30:8080",
    "64.225.4.17:10005",
    "162.248.225.222:80",
    "64.225.8.132:10005",
    "80.78.64.70:8080",
    "223.16.92.17:80",
    "221.194.149.8:80",
    "197.243.20.186:80",
    "111.224.213.196:8089",
    "159.65.77.168:8585",
    "2.138.254.0:3128",
    "162.248.225.239:80",
    "162.248.225.144:80",
    "181.212.58.68:80",
    "47.243.92.199:3128",
    "194.182.178.90:3128",
    "39.165.0.137:9002",
    "182.93.85.225:8080",
    "35.209.198.222:80",
    "47.93.114.68:88",
    "183.221.221.149:9091",
    "203.95.198.112:8080",
    "154.85.58.149:80",
    "139.59.1.14:3128",
    "72.10.160.94:20629",
    "191.96.251.53:80",
    "136.144.155.176:3128",
    "177.12.118.160:80",
    "136.144.155.173:3128",
    "162.248.225.237:80",
    "198.37.57.112:80",
    "162.248.225.108:80",
    "172.173.132.85:80",
    "61.133.66.69:9002",
    "79.137.203.245:3128",
    "162.248.225.172:80",
    "93.20.25.100:80",
    "196.20.125.145:8083",
    "162.248.225.111:80",
    "68.183.144.115:10003",
    "162.248.225.167:80",
    "193.239.56.84:8081",
    "181.41.142.252:443",
    "67.43.227.227:20755",
    "66.29.154.105:3128",
    "102.132.201.202:80",
    "198.199.86.11:3128",
    "122.9.131.161:8888",
    "221.231.24.94:9002",
    "46.101.186.238:80",
    "203.89.8.107:80",
    "113.214.27.99:8118",
    "135.125.39.69:12000",
    "152.32.132.220:80",
    "190.122.185.170:999",
    "185.249.107.84:3128",
    "114.231.82.60:8089",
    "217.12.21.249:80",
    "189.240.60.168:9090",
    "114.231.46.20:8089",
    "114.231.82.17:8888",
    "102.132.56.218:8080",
    "27.79.199.186:3128",
    "45.133.168.120:8080",
    "91.235.220.122:80",
    "1.224.3.122:3889",
    "132.145.162.109:3128",
    "103.23.37.138:80",
    "92.114.19.131:3128",
    "92.114.19.138:3128",
    "92.114.19.133:3128",
    "5.180.254.9:80",
    "196.11.183.216:8080",
    "193.150.21.138:8088",
    "103.231.78.36:80",
    "116.254.115.130:8080",
    "185.221.237.219:80",
    "103.178.94.107:80",
    "143.47.121.145:3128",
    "103.216.49.57:8080",
    "109.254.81.159:9090",
    "91.67.234.73:80",
    "196.251.135.157:8080",
    "102.132.40.222:8080",
    "102.132.41.31:8080",
    "216.238.99.171:80",
    "103.133.221.251:80",
    "122.116.150.2:9000",
    "95.216.164.36:80",
    "94.130.54.171:7385",
    "94.130.54.171:7449",
    "94.130.54.171:7455",
    "94.130.54.171:7166",
    "94.130.54.171:7396",
    "94.130.54.171:7021",
    "194.182.187.78:3128",
    "190.104.168.19:80",
    "103.141.70.18:8080",
    "188.215.245.235:80",
    "94.130.54.171:7293",
    "94.130.54.171:7125",
    "94.130.54.171:7095",
    "103.118.175.87:1645",
    "58.250.250.115:8888",
    "121.230.210.254:8089",
    "114.106.135.0:8089",
    "65.21.232.59:8786",
    "223.247.46.96:8089",
    "45.71.169.145:80",
    "103.83.232.122:80",
    "222.190.173.154:8089",
    "103.218.188.2:80",
    "114.231.46.185:8089",
    "88.99.249.96:8283",
    "204.157.240.53:999",
    "114.106.135.177:8089",
    "88.99.249.96:8177",
    "129.213.118.148:3128",
    "194.31.53.250:80",
    "180.119.92.64:8089",
    "117.94.122.150:9000",
    "5.165.6.188:1513",
    "114.233.70.184:9000",
    "202.0.103.115:80",
    "221.230.216.50:7788",
    "123.245.248.135:8089",
    "190.104.173.62:80",
    "223.215.176.221:8089",
    "128.199.202.122:8080",
    "185.49.170.20:43626",
    "114.103.81.34:8089",
    "5.2.228.168:8888",
    "101.34.30.200:8081",
    "114.233.70.213:9000",
    "41.65.236.43:1981",
    "2.83.198.171:80",
    "103.150.18.218:80",
    "222.190.208.125:8089",
    "221.230.216.54:7788",
    "222.190.208.44:8089",
    "118.70.12.171:53281",
    "41.74.91.190:7777",
    "103.49.202.252:80",
    "85.50.139.97:55443",
    "200.7.10.158:8080",
    "43.133.180.107:7890",
    "103.127.1.130:80",
    "223.215.177.196:8089",
    "63.42.112.155:8001",
    "114.233.71.0:9000",
    "114.231.8.204:8089",
    "183.165.246.108:8089",
    "223.247.46.169:8089",
    "66.29.154.103:3128",
    "49.70.89.246:8089",
    "46.160.209.155:8088",
    "201.238.248.134:443",
    "87.123.56.163:80",
    "103.146.17.241:80",
    "222.190.208.233:8089",
    "114.103.88.53:8089",
    "117.70.48.40:8089",
    "114.99.8.124:8089",
    "178.216.249.130:8080",
    "198.44.191.202:45787",
    "177.66.101.223:8024",
    "103.15.140.121:44759",
    "123.245.248.97:8089",
    "182.204.183.221:8089",
    "123.245.250.179:8089",
    "123.245.249.5:8089",
    "43.251.118.153:45787",
    "121.230.210.106:8089",
    "123.245.250.190:8089",
    "182.204.176.86:8089",
    "114.106.134.117:8089",
    "114.103.88.87:8089",
    "158.101.113.18:80",
    "221.230.216.200:7788",
    "114.106.173.101:8089",
    "188.127.249.9:20255",
    "103.68.194.85:45787",
    "222.190.173.102:8089",
    "223.215.177.115:8089",
    "103.80.54.132:32650",
    "183.165.248.179:8089",
    "114.233.70.173:9000",
    "123.245.250.6:8089",
    "165.225.206.248:10007",
    "182.204.178.100:8089",
    "182.204.181.134:8089",
    "102.69.236.152:80",
    "117.94.121.29:9000",
    "114.231.41.171:8089",
    "183.165.244.37:8089",
    "95.71.125.50:49882",
    "120.35.200.44:8089",
    "117.94.122.175:9000",
    "180.175.124.102:8118",
    "114.106.173.122:8089",
    "103.118.78.194:80",
    "223.215.176.37:8089",
    "123.245.249.185:8089",
]

welcome_message = """
*Accounts file created successfully.
*To add multiple accounts simply copy and paste the default account.
*Add unique names and unique tokens.
*The name can be anything you want, they don't have to be the Twitch account. Tokens must match your account.
*Customize the other settings as you need.
*Accounts with duplicate names and tokens will be wiped from the file.
*If you have any issues with the user agent or the proxy, replace them.
*Duplicate user agents and proxies will be automatically replaced, you can manually edit if you have issues with faulty ones, but make sure they are not duplicates.
*Once the file is set up, run main.py again.
"""

heartbreak = [
    r"  ♥",
    r"   ♥",
    r"    ♥",
    r"     ♥",
    r"      ♥",
    r"       ♥",
    r"        ♥",
    r"         ♥",
    r"          ♥",
    r"           ♥",
    r"            ♥",
    r"             ♥",
    r"              ♥",
    r"               ♥",
    r"                ♥",
    r"                 ♥",
    r"  ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥",
]