# Prod file with error handling


import time
from datetime import datetime, timedelta
from utils import constants
from utils.game_requests import (
    collect_raid_rewards,
    get_game_data,
    get_user_dungeon,
    leave_captain,
    update_unit_cooldown,
)
from utils.logger import log_to_file
from utils.marker_handler import calculate_placement
from utils.placement_handler import place_the_unit
from utils.settings import check_raid_type, open_file, validate_raid
from utils.player import getActiveraids


async def place_unit_in_battlefield():
    is_running = False
    log_to_file("log-placement Starting point of placement system")
    while True:
        if is_running:
            print("We are running already")
            return
        is_running = True

        try:
            accounts = open_file(constants.py_accounts)
            if not accounts or len(accounts) == 0:
                return
            log_to_file("log-placement Groups have been processed")
            await process_accounts(accounts)
        except Exception as e:
            pr_str = f"log An error occurred: {e}"
            print(pr_str)
            log_to_file(pr_str)
        finally:
            pr_str = "PLACEMENT SYSTEM CYCLED"
            print(pr_str)
            log_to_file(pr_str)
            time.sleep(15)
            is_running = False

# Process every account
async def process_accounts(accounts):
    for account in accounts:
        log_to_file("Processing account")
        # Check if account is enabled
        if not account["powered_on"]:
            continue
        name = account["name"]
        user_id = account["userId"]
        token = account["token"]
        user_agent = account["user_agent"]
        proxy = account["proxy"]
        proxy_user = account["proxy_user"]
        proxy_password = account["proxy_password"]
        can_epic = account["use_potions"]
        # Get active raids to determine placements
        raids = getActiveraids(
            user_id, token, user_agent, proxy, proxy_user, proxy_password
        )
        version, data_version = get_game_data(
            token, user_agent, proxy, proxy_user, proxy_password
        )

        # Check if raid response was properly received
        if raids == None:
            continue

        for raid in raids:
            raid_id = raid["raidId"]
            cap_nm = raid["twitchUserName"]
            cap_id = raid["captainId"]
            log_to_file("log-placement Calculating marker for raid")
            # Calculate the markers
            usable_markers = calculate_placement(
                cap_id,
                raid,
                raid_id,
                name,
                cap_nm,
                user_id,
                token,
                user_agent,
                proxy,
                proxy_user,
                proxy_password,
                version,
                data_version,
            )
            log_to_file("log-placement Validating raid")
            if usable_markers == []:
                log_to_file("log-placement There are no usable markers.")
                return

            # Check if raid is over to collect rewards #also check rewards was not collected already
            if (
                raid["hasRecievedRewards"] == "0"
                and raid["postBattleComplete"] == "1"
                and raid["hasViewedResults"] == "0"
            ):
                # Raid is complete, collect rewards and return so the battle is checked on the next loop
                collect_raid_rewards(
                    name,
                    cap_nm,
                    user_id,
                    raid_id,
                    token,
                    user_agent,
                    proxy,
                    proxy_user,
                    proxy_password,
                    version,
                    data_version,
                )
                continue
            try:
                is_playing = raid["isPlaying"]
            except:
                is_playing = "1"
            if is_playing and is_playing is not None and is_playing != "1":
                pr_str = f"Account {name} captain {cap_nm} went offline, attempting to clean the slot (depends on raid state)"
                log_to_file(pr_str)
                print(pr_str)
                leave_captain(cap_id, cap_nm, user_id, token, user_agent, proxy, proxy_user, proxy_password)
            try:
                is_code_locked = raid["isCodeLocked"]
            except:
                is_code_locked = False
            if is_code_locked:
                pr_str = f"Account {name} captain {cap_nm} is using codes, removing"
                log_to_file(pr_str)
                print(pr_str)
                leave_captain(cap_id, cap_nm, user_id, token, user_agent, proxy, proxy_user, proxy_password)
            # Check if raid is in active placement as everything from this point on would be a waste of resources.
            now = datetime.utcnow()
            cr_time_string = raid["creationDate"]
            creation_time = datetime.strptime(cr_time_string, "%Y-%m-%d %H:%M:%S")
            time_difference = now - creation_time

            raid_type = raid["type"]

            if not check_raid_type(raid_type, time_difference):
                continue

            # Check if raid captain is on blocklist and skip (Redudancy check since the slot script is supposed to skip blocklisted captains)
            blocklist = account["blocklist"]
            if raid["twitchUserName"].upper() in map(str.upper, blocklist):
                continue

            log_to_file("log-placement Checking loyalty preservation")
            # Check if it's campaign and if user wants to preserver loyalty.
            if account["preserve_loyalty"] != 0 and raid_type == "1":
                mapLoyalty = raid["pveLoyaltyLevel"]
                loyal = account["preserve_loyalty"]
                # Check if map loyalty is bigger than the.
                if loyal < mapLoyalty:
                    current_map_node = raid["nodeId"]
                    map_nodes = open_file("assets/map_nodes")
                    # Check the loyalty on the current based on the map id.
                    if current_map_node in map_nodes:
                        chest_type = map_nodes[current_map_node]["ChestType"]
                        chests = constants.regular_chests
                        if chest_type not in chests:
                            if account["switch_if_preserve_loyalty"]:
                                print("log 4 ")
                                leave_captain(
                                    cap_id,
                                    cap_nm,
                                    user_id,
                                    token,
                                    user_agent,
                                    proxy,
                                    proxy_user,
                                    proxy_password,
                                )
                                continue
                            else:
                                pass

            # Check if it is time and if there is time to place an unit
            last = raid["lastUnitPlacedTime"]
            previous_placement = (
                datetime.strptime(last, "%Y-%m-%d %H:%M:%S")
                if raid["lastUnitPlacedTime"]
                else None
            )

            if not validate_raid(raid):
                continue
            # Fallback PVP
            if raid_type == "2" or raid_type == "5":
                continue

            log_to_file("log-placement Checking unlimited placements")
            # Check raid type, check if an unit was placed, check if the user wants more units.
            un_key = constants.type_dict.get(raid_type)
            if last is not None and un_key is not None and not account[un_key]:
                continue

            # update units cooldown
            log_to_file("log-placement Updating unit cooldown")
            update_unit_cooldown()
            time.sleep(2)
            # Check if there are units available in order to save resources
            log_to_file("log-placement Checking if there are available units")

            if raid_type == "1":
                units = check_unit_availability(name)
            elif raid_type == "3":
                units = check_dungeon_unit_avail(
                    name,
                    user_id,
                    raid_id,
                    token,
                    user_agent,
                    proxy,
                    proxy_user,
                    proxy_password,
                )

            if not units or units == []:
                continue

            # Place the unit
            log_to_file("log-placement Placing the unit")
            place_the_unit(
                can_epic,
                raid,
                units,
                usable_markers,
                cap_nm,
                raid_id,
                name,
                user_id,
                token,
                user_agent,
                proxy,
                proxy_user,
                proxy_password,
                version,
                data_version,
                previous_placement,
                raid_type,
                creation_time,
            )


# Check if unit has priority and if it's out of cooldown.
def check_unit_availability(name):
    units = []
    now = datetime.utcnow()
    accounts = open_file(constants.py_accounts)
    for account in accounts:
        if account["name"] == name:
            user_units = account["units"]
            break
    for unit in user_units:
        if unit["priority"] == 0:
            continue
        cooldown_str = unit["cooldownTime"]
        if cooldown_str == None:
            cooldown = now - timedelta(minutes=5)
        else:
            cooldown = datetime.strptime(cooldown_str, "%Y-%m-%d %H:%M:%S")
        if cooldown > now:
            continue
        else:
            units.append(unit)

    # Sort units based on their "priority" value in ascending order
    units.sort(key=lambda x: x["priority"])

    return units

# Check if dungeon unit is dead, exhausted or knocked out
def check_dungeon_unit_avail(
    name, user_id, raid_id, token, user_agent, proxy, proxy_user, proxy_password
):
    pr_str = f"Account: {name} getting dungeon information."
    print(pr_str)
    log_to_file(pr_str)
    units = []
    accounts = open_file(constants.py_accounts)
    dungeon_data = get_user_dungeon(
        user_id, raid_id, token, user_agent, proxy, proxy_user, proxy_password
    )
    knocked_units  = ""
    dead_units  = ""
    exhausted_units = ""
    try:
        knocked_units = dungeon_data["data"]["knockedUnits"] or ""
    except:
        knocked_units = ""
    try:
        dead_units = dungeon_data["data"]["deadUnits"] or ""
    except:
        dead_units = ""
    try:
        exhausted_units = dungeon_data["data"]["exhaustedUnits"] or ""
    except:
        exhausted_units = ""
        
    unavailable_units = ' '.join(filter(None, [knocked_units.replace(',', ' '), dead_units.replace(',', ' '), exhausted_units.replace(',', ' ')]))
    for account in accounts:
        if account["name"] == name:
            user_units = account["units"]
            break
    for unit in user_units:
        if unit["priority"] == 0:
            continue
        unit_id = unit["unitId"]
        if unit_id in unavailable_units:
            continue
        else:
            units.append(unit)

    # Sort units based on their "priority" value in ascending order
    units.sort(key=lambda x: x["priority"])

    return units
