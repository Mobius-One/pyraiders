import asyncio, requests
import random
from datetime import datetime, timedelta
from utils.logger import log_to_file
from utils.response_handler import handle_error_response
from utils.time_generator import get_five_min
from utils.settings import open_file, write_file
from utils.game_requests import (
    get_live_captains,
    get_request_strings,
    get_game_data,
    get_proxy_auth,
    leave_captain,
)
from utils import constants


async def fill_slots():
    while True:
        await asyncio.sleep(get_five_min())
        # Fill empty slots.
        accounts = open_file(constants.py_accounts)
        for account in accounts:
            # Check if account is running
            if account["powered_on"] == False:
                continue
            # Required data
            user_id = account["userId"]
            user_name = account["name"]
            token = account["token"]
            user_agent = account["user_agent"]
            proxy = account["proxy"]
            proxy_user = account["proxy_user"]
            proxy_password = account["proxy_password"]

            # Data for the conditional checks
            preserve_loyalty = account["preserve_loyalty"]
            switch_if_preserve_loyalty = account["switch_if_preserve_loyalty"]
            switch_on_idle = account["switch_on_idle"]
            minimum_idle_time = account["minimum_idle_time"]
            only_masterlist = account["only_masterlist"]
            masterlist = []
            if only_masterlist:
                masterlist = account["masterlist"]
            ignore_blocklist = account["ignore_blocklist"]
            blocklist = []
            if ignore_blocklist:
                blocklist = account["blocklist"]
            favorites_only = account["favorites_only"]
            favoriteCaptainIds = []
            if favorites_only:
                favoriteCaptainIds = account["favoriteCaptainIds"]
            any_captain = account["any_captain"]
            temporary_ignore = account["temporary_ignore"]
            has_pass = account["has_pass"]
            slots_quantity = account["slots"]

            activeRaids = getActiveraids(
                user_id, token, user_agent, proxy, proxy_user, proxy_password
            )

            if activeRaids == None:
                continue
            # There are empty slots
            if (
                (has_pass and len(activeRaids) != 4)
                or (not has_pass and len(activeRaids) != 3)
                or activeRaids == None
                or activeRaids == []
            ):
                fill_empty_slots(
                    activeRaids,
                    user_id,
                    user_name,
                    token,
                    user_agent,
                    proxy,
                    proxy_user,
                    proxy_password,
                    temporary_ignore,
                    masterlist,
                    favoriteCaptainIds,
                    blocklist,
                    any_captain,
                    has_pass,
                    slots_quantity,
                    preserve_loyalty,
                    switch_if_preserve_loyalty,
                    switch_on_idle,
                    minimum_idle_time,
                    favorites_only,
                    only_masterlist,
                )
                continue
            else:
                # All slots are full, checks slots, place units
                clean_slots(
                    user_id,
                    token,
                    user_agent,
                    proxy,
                    proxy_user,
                    proxy_password,
                    preserve_loyalty,
                    switch_if_preserve_loyalty,
                    switch_on_idle,
                    minimum_idle_time,
                )
                log_to_file("clean_slot 1")
                continue
                place_units(user_id)
                return


def getActiveraids(user_id, token, user_agent, proxy, proxy_user, proxy_password):
    headers, proxies = get_request_strings(token, user_agent, proxy)
    _, data_version = get_game_data(
        token, user_agent, proxy, proxy_user, proxy_password
    )
    url = (
        constants.gameDataURL
        + "?cn=getActiveRaidsByUser&userId="
        + user_id
        + "&isCaptain=0&gameDataVersion="
        + data_version
        + "&clientPlatform:WebGL&command=getActiveRaidsByUser"
    )
    has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)
    if has_proxy:
        response = requests.get(url, proxies=proxies, headers=headers, auth=proxy_auth)
    else:
        response = requests.get(url, proxies=proxies, headers=headers)

    has_error = handle_error_response(response)
    if has_error:
        log_to_file(url)
        return

    if response.status_code == 200:
        parsedResponse = response.json()
        raid_data = parsedResponse["data"]
        activeRaids = []
        if raid_data == None:
            return activeRaids.append("all slots are empty")

        for raid in raid_data:
            raidId = raid["raidId"]
            if raidId == None:
                continue
            captainId = raid["captainId"]
            userSortIndex = raid["userSortIndex"]
            twitchUserName = raid["twitchUserName"]
            lastUnitPlacedTime = raid["lastUnitPlacedTime"]
            creationDate = raid["creationDate"]
            pveLoyaltyLevel = raid["pveLoyaltyLevel"]
            startTime = raid["startTime"]
            isCodeLocked = raid["isCodeLocked"]
            nodeId = raid["nodeId"]
            type = raid["type"]
            battleground = raid["battleground"]
            hasViewedResults = raid["hasViewedResults"]
            chestAwarded = raid["chestAwarded"]
            battleResult = raid["battleResult"]
            rewards = raid["rewards"]
            postBattleComplete = raid["postBattleComplete"]
            hasRecievedRewards = raid["hasRecievedRewards"]

            activeRaids.append(
                {
                    "raidId": raidId,
                    "captainId": captainId,
                    "userSortIndex": userSortIndex,
                    "twitchUserName": twitchUserName,
                    "lastUnitPlacedTime": lastUnitPlacedTime,
                    "creationDate": creationDate,
                    "pveLoyaltyLevel": pveLoyaltyLevel,
                    "startTime": startTime,
                    "isCodeLocked": isCodeLocked,
                    "nodeId": nodeId,
                    "type": type,
                    "battleground": battleground,
                    "hasViewedResults": hasViewedResults,
                    "chestAwarded": chestAwarded,
                    "battleResult": battleResult,
                    "rewards": rewards,
                    "postBattleComplete": postBattleComplete,
                    "hasRecievedRewards": hasRecievedRewards,
                }
            )
        return activeRaids


def fill_empty_slots(
    activeRaids,
    user_id,
    user_name,
    token,
    user_agent,
    proxy,
    proxy_user,
    proxy_password,
    temporary_ignore,
    masterlist,
    favoriteCaptainIds,
    blocklist,
    any_captain,
    has_pass,
    slots_quantity,
    preserve_loyalty,
    switch_if_preserve_loyalty,
    switch_on_idle,
    minimum_idle_time,
    favorites_only,
    only_masterlist,
):
    has_active_dungeon = False
    has_active_pvp2 = False
    has_active_pvp5 = False
    for raid in activeRaids:
        if raid["type"] == "3":
            has_active_dungeon = True
        elif raid["type"] == "2":
            has_active_pvp2 = True
        elif raid["type"] == "5":
            has_active_pvp5 = True

    # Get list of active captains, filter it with the masterlist, favoriteCaptainsIds, blocklist

    headers, proxies = get_request_strings(token, user_agent, proxy)
    version, data_version = get_game_data(
        token, user_agent, proxy, proxy_user, proxy_password
    )
    has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)

    merged_data = get_live_captains(
        user_name, headers, proxies, version, data_version, has_proxy, proxy_auth
    )
    if merged_data == []:
        return

    unique_user_ids = set()
    temp_unique_data = []
    # Clean up list to remove duplicate captains
    for entry in merged_data:
        if entry == None:
            continue
        try:
            id = entry["userId"]
        except:
            log_to_file(f"id = entry[userId] {entry}")
            continue
        if id not in unique_user_ids:
            unique_user_ids.add(id)
            temp_unique_data.append(entry)
            
    # Removing captains running special mode conditions and captains running codes.
    unique_data = []
    for captain in temp_unique_data:
        if (
            (captain["type"] == "3" and has_active_dungeon) or
            (captain["type"] == "5" and has_active_pvp5) or
            (captain["type"] == "2" and has_active_pvp2)):
            pass
        else:
            unique_data.append(captain)
            
    acceptable_captains = []
    global_ignore = open_file("variables.json")
    gb_list = global_ignore["global_ignore"]
    if len(gb_list) != 0:
        acceptable_captains = sorted(
            (
                entry
                for entry in unique_data
                if entry["twitchUserName"].upper() in map(str.upper, global_ignore)
            ),
            key=lambda x: global_ignore.index(x["twitchUserName"].upper())
            if x["twitchUserName"].upper() in global_ignore
            else float("inf"),
        )

    # User wants to use masterlist
    if len(masterlist) != 0:
        acceptable_captains = sorted(
            (
                entry
                for entry in unique_data
                if entry["twitchUserName"].upper() in map(str.upper, masterlist)
            ),
            key=lambda x: masterlist.index(x["twitchUserName"].upper())
            if x["twitchUserName"].upper() in masterlist
            else float("inf"),
        )

    # User wants favorite list
    if len(acceptable_captains) == 0 and favoriteCaptainIds != "":
        for entry in unique_data:
            captain = entry["userId"]
            if captain in favoriteCaptainIds:
                acceptable_captains.append(entry)

    if len(acceptable_captains) == 0 and len(blocklist) != 0 and any_captain:
        for entry in unique_data:
            captain = entry["twitchUserName"].upper()
            if captain in map(str.upper, blocklist):
                pass
            else:
                acceptable_captains.append(entry)

    if len(acceptable_captains) == 0 and any_captain:
        acceptable_captains = unique_data

    # Now that the list of usable live captains has been made, filter out active captains and avoid a duplicate pvp/dungeon captain

    # Remove active captains from the live captains list
    active_captain_ids = set(entry["captainId"] for entry in activeRaids)
    acceptable_captains = [
        entry
        for entry in acceptable_captains
        if entry["userId"] not in active_captain_ids
    ]

    # Remove live captains that are running special modes that active captains are also running to avoid conflict
    active_types = {entry["type"] for entry in activeRaids if "type" in entry}
    acceptable_captains = [
        entry
        for entry in acceptable_captains
        if entry.get("type") == "1"
        or (
            entry.get("type")
            and set(entry["type"]) != {"1"}
            and set(entry["type"]) != active_types
        )
    ]

    # Remove captains that are on the temporary idle list for the last 30 minutes
    # Convert the time strings to datetime variables
    try:
        temporary_ignore_times = [
            datetime.strptime(entry["time"], "%Y-%m-%d %H:%M:%S")
            for entry in temporary_ignore
        ]
        current_time = datetime.utcnow()
        # Define the threshold for acceptable captains (30 minutes)
        threshold_time = timedelta(minutes=30)
        # Filter out captains younger than 30 minutes in temporary_ignore
        captains_to_remove = [
            entry["capNm"].upper()
            for entry, time_entry in zip(temporary_ignore, temporary_ignore_times)
            if current_time - time_entry < threshold_time
        ]
        # Remove corresponding entries from acceptable_captains
        acceptable_captains = [
            entry
            for entry in acceptable_captains
            if entry["twitchUserName"].upper() not in captains_to_remove
        ]
    except:
        log_to_file("An error happened while trying to fill empty slots")
        pass

    # The list left is ready to be used for placement, now figure out what slots are available
    # Initialize slots list
    slots = []
    for raid in activeRaids:
        slots.append(raid["userSortIndex"])
    possible_slots = []

    if has_pass and len(slots) != 4:
        possible_slots = list(set(["0", "1", "2", "3"]) - set(slots))

    elif not has_pass and len(slots) != 3:
        possible_slots = list(set(["0", "1", "2"]) - set(slots))

    # If possible_slots is not empty it means there are slots that can be filled up, fill them up the acceptable_captains list.
    if len(possible_slots) != 0:
        select_captain(
            user_id,
            user_name,
            headers,
            proxies,
            version,
            data_version,
            has_proxy,
            proxy_auth,
            possible_slots,
            acceptable_captains,
            token,
            user_agent,
            proxy,
            proxy_user,
            proxy_password,
            slots_quantity,
            preserve_loyalty,
            switch_if_preserve_loyalty,
            switch_on_idle,
            minimum_idle_time,
            favorites_only,
            only_masterlist,
        )
    else:
        clean_slots(
            user_id,
            token,
            user_agent,
            proxy,
            proxy_user,
            proxy_password,
            preserve_loyalty,
            switch_if_preserve_loyalty,
            switch_on_idle,
            minimum_idle_time,
        )

        log_to_file("clean_slot 2")
        return


# Place captain on slot
def select_captain(
    user_id,
    user_name,
    headers,
    proxies,
    version,
    data_version,
    has_proxy,
    proxy_auth,
    possible_slots,
    acceptable_captains,
    token,
    user_agent,
    proxy,
    proxy_user,
    proxy_password,
    slots_quantity,
    preserve_loyalty,
    switch_if_preserve_loyalty,
    switch_on_idle,
    minimum_idle_time,
    favorites_only,
    only_masterlist,
):
    for i, slot in enumerate(possible_slots):
        slot_integer = int(slot)
        if i < len(acceptable_captains) and slot_integer < slots_quantity:
            # RANDOMIZE THE INDEX SO DEFAULT ACCOUNTS ARE SPREAD THROUGHOUT THE CAPTAINS
            if favorites_only or only_masterlist:
                captain_id = acceptable_captains[i]["userId"]
                captain_name = acceptable_captains[i]["twitchUserName"]
            else:
                random_captain = random.choice(acceptable_captains)
                captain_id = random_captain["userId"]
                captain_name = random_captain["twitchUserName"]
        else:
            clean_slots(
                user_id,
                token,
                user_agent,
                proxy,
                proxy_user,
                proxy_password,
                preserve_loyalty,
                switch_if_preserve_loyalty,
                switch_on_idle,
                minimum_idle_time,
            )
            log_to_file("clean_slot 3")
            return

        url = (
            constants.gameDataURL
            + "?cn=addPlayerToRaid&userId="
            + user_id
            + "&isCaptain=0&gameDataVersion="
            + data_version
            + "&command=addPlayerToRaid&userSortIndex="
            + slot
            + "&captainId="
            + captain_id
            + "&clientVersion="
            + version
            + "&clientPlatform=WebGL"
        )

        if has_proxy:
            response = requests.get(
                url, proxies=proxies, headers=headers, auth=proxy_auth
            )
            pr_str = f"Account: {user_name}. Added {captain_name} to slot number {str(int(slot) + 1)}"
            log_to_file(pr_str)
            print(pr_str)
        else:
            response = requests.get(url, proxies=proxies, headers=headers)
            pr_str = f"Account: {user_name}. Added {captain_name} to slot number {str(int(slot) + 1)}"
            log_to_file(pr_str)
            print(pr_str)
        has_error = handle_error_response(response)
        if has_error:
            log_to_file(f"Account: {user_name}. Captain: {captain_name}. URL: {url}")
            return

    # get active raids again and count the occupied slots, that is the real amount of slots
    activeRaids = getActiveraids(
        user_id, token, user_agent, proxy, proxy_user, proxy_password
    )
    real_slot_quantity = len(activeRaids)
    accounts = open_file(constants.py_accounts)
    for account in accounts:
        if account["userId"] == user_id or account["otherUserId"] == user_id:
            account["slots"] = real_slot_quantity

    write_file(constants.py_accounts, accounts)


# Check idle captains and loyalty switch.
def clean_slots(
    user_id,
    token,
    user_agent,
    proxy,
    proxy_user,
    proxy_password,
    preserve_loyalty,
    switch_if_preserve_loyalty,
    switch_on_idle,
    minimum_idle_time,
):
    # Once again, get active raids
    activeRaids = getActiveraids(
        user_id, token, user_agent, proxy, proxy_user, proxy_password
    )

    # Remove idle captains from the slots as well as captain running codes.
    if switch_on_idle:
        for raid in activeRaids:
            time_str = raid["creationDate"]
            is_code_locked = raid["isCodeLocked"]
            # This data object is not being stored so there's need to remove the milliseconds
            current_time = datetime.utcnow()
            idle_time = timedelta(minutes=30 + minimum_idle_time)
            creation_time = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            if current_time > creation_time + idle_time:
                # captain is idling, switch
                captain_id = raid["captainId"]
                captain_name = raid["twitchUserName"]
                pr_str = f"log 1 {captain_name} is idling. Switching..."
                log_to_file(pr_str)
                print(pr_str)
                
                leave_captain(
                    captain_id,
                    captain_name,
                    user_id,
                    token,
                    user_agent,
                    proxy,
                    proxy_user,
                    proxy_password,
                )
                
            elif is_code_locked:
                captain_id = raid["captainId"]
                captain_name = raid["twitchUserName"]
                pr_str = f"log 2 {captain_name} is using codes. Switching..."
                log_to_file(pr_str)
                print(pr_str)
                leave_captain(
                    captain_id,
                    captain_name,
                    user_id,
                    token,
                    user_agent,
                    proxy,
                    proxy_user,
                    proxy_password,
                )
                

    # Remove captains that are on loyalty switch
    if switch_if_preserve_loyalty and preserve_loyalty != 0:
        activeRaids = getActiveraids(
            user_id, token, user_agent, proxy, proxy_user, proxy_password
        )
        for raid in activeRaids:
            raid_loyalty = raid["pveLoyaltyLevel"]
            if raid_loyalty < preserve_loyalty and raid["type"] == "1":
                # Check map, if it's a loyalty map, replace captain.
                mapNode = raid["nodeId"]
                map_nodes = open_file(constants.map_nodes_path)
                if mapNode in map_nodes:
                    node_info = map_nodes[mapNode]

                    if (
                        "ChestType" in node_info
                        and node_info["ChestType"] not in constants.regular_chests
                    ):
                        captain_id = raid["captainId"]
                        captain_name = raid["twitchUserName"]
                        pr_str = f"log 3 Account: {user_id} {captain_name} is in a loyalty chest {node_info['ChestType']} without loyalty. Switching..."
                        log_to_file(pr_str)
                        print(pr_str)
                        leave_captain(
                            captain_id,
                            captain_name,
                            user_id,
                            token,
                            user_agent,
                            proxy,
                            proxy_user,
                            proxy_password,
                        )
                    elif (
                        "ChestType" in node_info
                        and node_info["ChestType"] in constants.regular_chests
                    ):
                        # not a loyalty chest
                        pass
                    else:
                        pr_str = f"log 4 {captain_name} Couldn't find chest info"
                        log_to_file(pr_str)
                        print(pr_str)
                else:
                    pr_str = f"log 5 {captain_name} Couldn't find chest info"
                    log_to_file(pr_str)
                    print(pr_str)

    return
    place_units(user_id)


# place units based on the loyalty skip and unlimited states
def place_units(user_id):
    # This task is being handled by /utils/place_units.place_unit_in_battlefield().
    # If needed this will be manually called and run synchronously.
    pass
