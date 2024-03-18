from datetime import datetime
import random
import time
import requests
from utils import constants, current_event
from requests.auth import HTTPProxyAuth
from utils.logger import log_to_file
from utils.response_handler import handle_error_response
from utils.settings import add_temporary_ignore, open_file, write_file


# Pass the headers and proxy formatted strings so requests can be performed.
def get_request_strings(token, user_agent, proxy):
    headers = {"Cookie": "ACCESS_INFO=" + token, "User-Agent": user_agent}
    proxies = {"http": "http://" + proxy}
    return headers, proxies


def get_proxy_auth(proxy_user, proxy_pass):
    if proxy_user and proxy_pass:
        proxy_auth = HTTPProxyAuth(proxy_user, proxy_pass)
        return True, proxy_auth
    else:
        return False, ""


# Check if current event is a new one, if it is load map.
def check_for_new_event():
    # Load and replace event Id if needed
    accounts = open_file(constants.py_accounts)
    userId = accounts[0]["userId"]
    token = accounts[0]["token"]
    user_agent = accounts[0]["user_agent"]
    proxy = accounts[0]["proxy"]
    proxy_user = accounts[0]["proxy_user"]
    proxy_password = accounts[0]["proxy_password"]

    version, data_version = get_game_data(
        token, user_agent, proxy, proxy_user, proxy_password
    )
    url = (
        constants.gameDataURL
        + "?cn=getEventProgressionLite&userId="
        + userId
        + "&isCaptain=0&gameDataVersion="
        + data_version
        + "&command=getEventProgressionLite&clientVersion="
        + version
        + "&clientPlatform=MobileLite"
    )

    headers, proxies = get_request_strings(token, user_agent, proxy)
    has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)
    if has_proxy:
        response = requests.get(url, proxies=proxies, headers=headers, auth=proxy_auth)
    else:
        response = requests.get(url, proxies=proxies, headers=headers)

    has_error = handle_error_response(response)
    if has_error:
        log_to_file(f"Account: {userId}. URL: {url}")
        return

    if response.status_code == 200:
        parsedResponse = response.json()
        data = parsedResponse["data"]
        if data == None:
            return

        eventUid = data["eventUid"]
        current_url = parsedResponse["info"]["dataPath"]
        if eventUid != current_event.current_event:
            with open("utils/current_event.py", "w") as file:
                file.write('current_event = "' + eventUid + '"')
            print(
                "New event has started. Checking map nodes, this may take a few seconds..."
            )
            get_new_event_map(current_url)
        else:
            get_new_event_map(current_url)

    else:
        print(f"Error: {response.status_code}")


def get_new_event_map(current_url):
    # Update mapIds

    config_json = open_file("variables.json")
    old_url = config_json["map_node_url"]
    if old_url == current_url:
        print("Map nodes are up to date")
        return
    else:
        config_json["map_node_url"] = current_url
        write_file("variables.json", config_json)
        print("Map nodes have changed, fetching new map nodes...")

    response = requests.get(current_url)

    if response.status_code == 200:
        data_json = response.json()["sheets"]["MapNodes"]
        for entry in data_json.values():
            for key in constants.keys_to_remove:
                entry.pop(key, None)
        write_file(constants.map_nodes_path, data_json)

        # Grab units in here
        units_json = response.json()["sheets"]["Units"]
        for unit_data in units_json.values():
            for key_to_remove in constants.unit_values_rm:
                unit_data.pop(key_to_remove, None)
        write_file(constants.map_units_path, units_json)

        quests_json = response.json()["sheets"]["Quests"]
        for quests in quests_json.values():
            for key_to_remove in constants.quest_keys_rm:
                quests.pop(key_to_remove, None)
        write_file(constants.quest_nodes_path, quests_json)

        print("\nMap nodes updated successfully.\n")
    else:
        print(f"\nError updating game data: {response.status_code}")


# Get the game version and data_version for the api calls
def get_game_data(token, user_agent, proxy, proxy_user, proxy_password):
    _, proxies = get_request_strings(token, user_agent, proxy)
    has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)
    headers = {"User-Agent": user_agent}

    if has_proxy:
        gameDataResponse = requests.get(
            constants.gameDataURL, proxies=proxies, headers=headers, auth=proxy_auth
        )
    else:
        gameDataResponse = requests.get(
            constants.gameDataURL, proxies=proxies, headers=headers
        )

    has_error = handle_error_response(gameDataResponse)
    if has_error:
        log_to_file(constants.gameDataURL)
        return

    # Check if the request was successful (status code 200)
    if gameDataResponse.status_code == 200:
        response_json = gameDataResponse.json()

        # Extract version from the JSON response
        # Version which goes in the clientVersion command. _shrug_
        version = response_json["info"]["version"]
        data_version = response_json["info"]["dataVersion"]
        return version, data_version
    else:
        return False, False


# Get userId and a list of favorite captains
def get_user_id(
    token, user_agent, proxy, version, data_version, proxy_user, proxy_password
):
    url = (
        constants.gameDataURL
        + "?cn=getUser&gameDataVersion="
        + data_version
        + "&command=getUser&skipDataCheck=true&isLogin=true&clientVersion="
        + version
        + "&clientPlatform=WebGL"
    )

    headers, proxies = get_request_strings(token, user_agent, proxy)

    has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)
    if has_proxy:
        response = requests.get(url, proxies=proxies, headers=headers, auth=proxy_auth)
    else:
        response = requests.get(url, proxies=proxies, headers=headers)

    has_error = handle_error_response(response)
    if has_error:
        parsedResponse = response.json()["errorMessage"]
        pr_str = f'Error for account token: {token}. Error is {parsedResponse}'
        if parsedResponse == "User is not authorized.":
            accounts = open_file(constants.py_accounts)
            py_unauthorized_accounts = open_file(constants.py_unauthorized_accounts)
            for account in accounts:
                if account["token"] == token:
                    pr_str = f"Removing unathorized account from the accounts file. Please check {constants.py_unauthorized_accounts}"
                    print(pr_str)
                    log_to_file(pr_str)
                    write_file(constants.py_accounts, accounts)
                    if py_unauthorized_accounts is None:
                        py_unauthorized_accounts = []
                    py_unauthorized_accounts.append(account)
                    write_file(constants.py_unauthorized_accounts, py_unauthorized_accounts)
                    account = None
                    token = None
                    break
        log_to_file(pr_str)
        log_to_file(url)
        return "", "", ""

    if response.status_code == 200:
        parsedResponse = response.json()
        userId = parsedResponse["data"]["userId"]
        try:
            favoriteCaptains = parsedResponse["data"]["favoriteCaptainIds"]
        except KeyError:
            favoriteCaptains = ""
        try:
            other_user_id = parsedResponse["data"]["otherUserId"]
        except KeyError:
            other_user_id = ""

    return userId, other_user_id, favoriteCaptains


# Get userId, favorite captains and call to get the user units
def set_user_data(account_data):
    for account in account_data:
        if account["powered_on"] == False:
            continue

        token = account["token"]
        user_agent = account["user_agent"]
        proxy = account["proxy"]
        proxy_user = account["proxy_user"]
        proxy_password = account["proxy_password"]

        version, data_version = get_game_data(
            token, user_agent, proxy, proxy_user, proxy_password
        )

        userId, other_user_id, favoriteCaptainIds = get_user_id(
            token, user_agent, proxy, version, data_version, proxy_user, proxy_password
        )
        if userId == "":
            account_data.remove(account)
            continue
        account["userId"] = userId
        account["otherUserId"] = other_user_id
        account["favoriteCaptainIds"] = favoriteCaptainIds

        account["has_pass"] = get_battlepass(
            userId,
            token,
            user_agent,
            proxy,
            version,
            data_version,
            proxy_user,
            proxy_password,
        )
        if account["units"] == "":
            units = get_units_data(
                userId,
                token,
                user_agent,
                proxy,
                version,
                data_version,
                proxy_user,
                proxy_password,
            )
            account["units"] = units
        else:
            # TODO Update unit level as the data already exists
            pass

    return account_data


def get_battlepass(
    userId, token, user_agent, proxy, version, data_version, proxy_user, proxy_password
):
    url = (
        constants.gameDataURL
        + "?cn=getEventProgressionLite&userId="
        + userId
        + "&isCaptain=0&gameDataVersion="
        + data_version
        + "&command=getEventProgressionLite&clientVersion="
        + version
        + "&clientPlatform=MobileLite"
    )

    headers, proxies = get_request_strings(token, user_agent, proxy)
    has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)
    if has_proxy:
        response = requests.get(url, proxies=proxies, headers=headers, auth=proxy_auth)
    else:
        response = requests.get(url, proxies=proxies, headers=headers)

    has_error = handle_error_response(response)
    if has_error:
        log_to_file(f"Account: {userId}. URL: {url}")
        return

    if response.status_code == 200:
        parsedResponse = response.json()
        data = parsedResponse["data"]
        if data == None:
            return False

        has_pass = data["hasBattlePass"]
        if has_pass == "1":
            return True
        else:
            return False


def leave_captain(
    captain_id,
    captain_name,
    user_id,
    token,
    user_agent,
    proxy,
    proxy_user,
    proxy_password,
):
    version, data_version = get_game_data(
        token, user_agent, proxy, proxy_user, proxy_password
    )
    headers, proxies = get_request_strings(token, user_agent, proxy)
    has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)
    url = (
        constants.gameDataURL
        + "?cn=leaveCaptain&userId="
        + user_id
        + "&isCaptain=0&gameDataVersion="
        + data_version
        + "&command=leaveCaptain&captainId="
        + captain_id
        + "&clientVersion="
        + version
        + "&clientPlatform=WebGL"
    )

    if has_proxy:
        response = requests.get(url, proxies=proxies, headers=headers, auth=proxy_auth)
    else:
        response = requests.get(url, proxies=proxies, headers=headers)

    add_temporary_ignore(user_id, captain_name)

    has_error = handle_error_response(response)
    if has_error:
        log_to_file(f"Account: {user_id}. Captain: {captain_name}. URL: {url}")
        return


# Get each user's units, append priority and levelup permissions to each unit
def get_units_data(
    userId, token, user_agent, proxy, version, data_version, proxy_user, proxy_password
):
    url = (
        constants.gameDataURL
        + "?cn=getUserUnits&userId="
        + userId
        + "&isCaptain=0&gameDataVersion="
        + data_version
        + "&command=getUserUnits&clientVersion="
        + version
        + "&clientPlatform=WebGL"
    )

    headers, proxies = get_request_strings(token, user_agent, proxy)
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
        units = response.json().get("data", [])
        for each_unit in units:
            if each_unit["unitType"] == "alliesballoonbuster":
                each_unit["priority"] = 0
            else:
                each_unit["priority"] = 10
            each_unit["level_up"] = False
            each_unit["spec_option"]: None
            # add an integer key called priority to each item before saving
    return units


# Update unit cooldown timer.
def update_unit_cooldown():
    accounts = open_file(constants.py_accounts)

    for account in accounts:
        name = account["name"]
        user_id = account["userId"]
        token = account["token"]
        user_agent = account["user_agent"]
        proxy = account["proxy"]
        proxy_user = account["proxy_user"]
        proxy_password = account["proxy_password"]
        local_units = account["units"]
        version, data_version = get_game_data(
            token, user_agent, proxy, proxy_user, proxy_password
        )
        fetched_units = get_units_data(
            user_id,
            token,
            user_agent,
            proxy,
            version,
            data_version,
            proxy_user,
            proxy_password,
        )
        if fetched_units is None:
            pr_str = f"Couldn't fetch units for {name}. Is user authorized?"
            print(pr_str)
            log_to_file(pr_str)
            continue
        
        for fetched_unit in fetched_units:
            found = False
            for local_unit in local_units:
                if local_unit["unitId"] == fetched_unit["unitId"]:
                    local_unit.update(
                        {
                            "userId": fetched_unit["userId"],
                            "unitType": fetched_unit["unitType"],
                            "level": fetched_unit["level"],
                            "skin": fetched_unit["skin"],
                            "cooldownTime": fetched_unit["cooldownTime"],
                            "specializationUid": fetched_unit["specializationUid"],
                            "soulType": fetched_unit["soulType"],
                            "soulId": fetched_unit["soulId"],
                        }
                    )
                    found = True
                    break
            if not found:
                local_units.append(
                    {
                        "userId": fetched_unit["userId"],
                        "unitType": fetched_unit["unitType"],
                        "level": fetched_unit["level"],
                        "skin": fetched_unit["skin"],
                        "cooldownTime": fetched_unit["cooldownTime"],
                        "unitId": fetched_unit["unitId"],
                        "specializationUid": fetched_unit["specializationUid"],
                        "soulType": fetched_unit["soulType"],
                        "soulId": fetched_unit["soulId"],
                        "priority": 0 if fetched_unit["unitType"] == "alliesballoonbuster" else 10,
                        "level_up": False,
                        "spec_option": None
                    }
                )

    write_file(constants.py_accounts, accounts)


def collect_raid_rewards(
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
):
    url = (
        constants.gameDataURL
        + "?cn=getRaidStatsByUser&userId="
        + user_id
        + "&isCaptain=0&gameDataVersion="
        + data_version
        + "&command=getRaidStatsByUser&raidId="
        + raid_id
        + "&clientVersion="
        + version
        + "&clientPlatform=WebGL"
    )

    headers, proxies = get_request_strings(token, user_agent, proxy)
    has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)
    if has_proxy:
        response = requests.get(url, proxies=proxies, headers=headers, auth=proxy_auth)
    else:
        response = requests.get(url, proxies=proxies, headers=headers)

    has_error = handle_error_response(response)
    if not has_error:
        now = datetime.now().strftime("%H:%M:%S")
        pr_str = f"Account: {name}: Chest/savage collected at {cap_nm} at {now}"
        print(pr_str)
        log_to_file(pr_str)
        time.sleep(5)
        collect_quests(
            token,
            name,
            user_agent,
            proxy,
            proxy_user,
            proxy_password,
            version,
            data_version,
        )
    else:
        log_to_file(
            f"Account: {name}: Chest/savage FAILED TO COLLECT at {cap_nm}. URL: {url}"
        )


def check_potions(
    user_id, data_version, version, token, user_agent, proxy, proxy_user, proxy_password
):
    url = (
        constants.gameDataURL
        + "?cn=getUser&userId="
        + user_id
        + "&isCaptain=0&gameDataVersion="
        + data_version
        + "&command=getUser"
        + "&clientVersion="
        + version
        + "&clientPlatform=WebGL"
    )

    headers, proxies = get_request_strings(token, user_agent, proxy)
    has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)
    if has_proxy:
        response = requests.get(url, proxies=proxies, headers=headers, auth=proxy_auth)
    else:
        response = requests.get(url, proxies=proxies, headers=headers)

    has_error = handle_error_response(response)
    if not has_error:
        response = response.json()
        epicP = response["data"]["epicProgression"]
        try:
            epic_qt = int(epicP)
            if epic_qt >= 45:
                return True
            else:
                return False
        except:
            log_to_file(response)
            return False
    else:
        log_to_file(url)
        return False


def get_live_captains(
    name, headers, proxies, version, data_version, has_proxy, proxy_auth
):
    live_captains_list = []

    for i in range(30):
        url = (
            constants.gameDataURL
            + "?cn=getCaptainsForSearch&isPlayingS=desc&isLiveS=desc&page="
            + str(i)
            + "&format=normalized&seed=0&resultsPerPage=30&filters=%7B%22favorite%22%3Afalse%2C%22isLive%22%3A1%2C%22ambassadors%22%3A%22false%22%7D&clientVersion="
            + version
            + "&clientPlatform=WebGL&gameDataVersion="
            + data_version
            + "&command=getCaptainsForSearch&isCaptain=0"
        )
        if has_proxy:
            response = requests.get(
                url, proxies=proxies, headers=headers, auth=proxy_auth
            )
        else:
            response = requests.get(url, proxies=proxies, headers=headers)

        has_error = handle_error_response(response)
        if has_error:
            log_to_file(f"Account: {name}. URL: {url}")
            return []
        # if captains_is_empty:
        # break
        live_captains_list.append(response.json())
        if response.json()["data"]["captains"] == []:
            break

        time.sleep(0.5)

    for i in range(30):
        url = (
            constants.gameDataURL
            + "?cn=getCaptainsForSearch&isPlayingS=desc&isLiveS=desc&page="
            + str(i)
            + "&format=normalized&seed=0&resultsPerPage=30&filters=%7B%22favorite%22%3Atrue%2C%22isLive%22%3A1%2C%22ambassadors%22%3A%22false%22%7D&clientVersion="
            + version
            + "&clientPlatform=WebGL&gameDataVersion="
            + data_version
            + "&command=getCaptainsForSearch&isCaptain=0"
        )
        if has_proxy:
            response = requests.get(
                url, proxies=proxies, headers=headers, auth=proxy_auth
            )
        else:
            response = requests.get(url, proxies=proxies, headers=headers)

        has_error = handle_error_response(response)
        if has_error:
            log_to_file(url)
            return []

        live_captains_list.append(response.json())
        if response.json()["data"]["captains"] == []:
            break

        time.sleep(0.5)

    captains_data_list = [entry["data"]["captains"] for entry in live_captains_list]
    merged_data = [
        captain for captains_data in captains_data_list for captain in captains_data
    ]
    return merged_data


# Equip skins. Captain skins have priority over a random skin.
def equip_skin(
    user_id,
    version,
    data_version,
    token,
    user_agent,
    proxy,
    proxy_user,
    proxy_password,
    unitName,
    cap_nm
):
    # Check if user wants to use skins
    accounts = open_file(constants.py_accounts)
    for account in accounts:
        if user_id == account["userId"]:
            # User doesn't want to user skins
            if not account["use_skins"]:
                return ""
            else:
                # User wants to use skins, find a matching one
                url = f"{constants.gameDataURL}?cn=getUserItems&userId={user_id}&isCaptain=0&gameDataVersion={data_version}&command=getUserItems&clientVersion={version}&clientPlatform=WebGL"
                headers, proxies = get_request_strings(token, user_agent, proxy)
                has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)
                if has_proxy:
                    response = requests.get(
                        url, proxies=proxies, headers=headers, auth=proxy_auth
                    )
                else:
                    response = requests.get(url, proxies=proxies, headers=headers)

                has_error = handle_error_response(response)
                if has_error:
                    log_to_file(
                        f"Account: {user_id}. Failed to get unit skins. URL: {url}"
                    )
                    return ""
                else:
                    a_skins = response.json()["data"]
                    random.shuffle(a_skins)

                    # Check for captain skins
                    skins = []
                    for sk in a_skins:
                        if "full" in sk["productId"]:
                            skins.insert(0, sk)
                        else:
                            skins.append(sk)
                            
                    for sk in skins:
                        skin_name = sk[
                            "productId"
                        ].lower()  # Using .lower() for lowercase conversion
                        if cap_nm.lower() in skin_name:
                            if (unitName == "flyingrogue" and "flyingrogue" in skin_name) or (unitName == "balloonbuster" and "balloonbuster" in skin_name):
                                return skin_name
                            elif (unitName == "rogue" and "rogue" in skin_name and "flyingrogue" not in skin_name) or (unitName == "buster" and "buster" in skin_name and "balloonbuster" not in skin_name):
                                return skin_name
                            elif unitName in skin_name:
                                return skin_name
                            

                    # Check for any skin
                    for sk in skins:
                        skin_name = sk["productId"].lower()
                        if unitName in skin_name:
                            return skin_name

    return ""


# After successfully collecting a chest/savage, check for quests.
def collect_quests(
    token, name, user_agent, proxy, proxy_user, proxy_password, version, data_version
):
    def collect_quest():
        # Get a list of current quests
        get_quests_url = (
            constants.gameDataURL
            + "?cn=getUserQuests&clientVersion="
            + version
            + "&clientPlatform=WebGL&gameDataVersion="
            + data_version
            + "&command=getUserQuests&isCaptain=0"
        )
        headers, proxies = get_request_strings(token, user_agent, proxy)
        has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)
        if has_proxy:
            response = requests.get(
                get_quests_url, proxies=proxies, headers=headers, auth=proxy_auth
            )
        else:
            response = requests.get(get_quests_url, proxies=proxies, headers=headers)
        has_error = handle_error_response(response)
        if has_error:
            log_to_file(
                f"Account: {name}. Failed to get quests. URL: {get_quests_url}. Response: {response.json()}"
            )
            return
        else:
            quest_nodes = open_file(constants.quest_nodes_path)
            qs_data = response.json()["data"]
            for q in qs_data:
                quest_id = q["currentQuestId"]
                quest_slot_id = q["questSlotId"]

                # There is no quest
                if quest_id is None:
                    continue
                # Check if current quest has been completed
                current_quest = q["currentQuestId"]

                if (
                    current_quest is not None
                    and q["completedQuestIds"] is not None
                    and current_quest in q["completedQuestIds"]
                ):
                    continue

                else:
                    current_progress = q["currentProgress"]
                    current_int = None
                    try:
                        current_int = int(current_progress)
                    except ValueError:
                        log_to_file(q)
                        return

                    for node in quest_nodes:
                        node_str = str(node)
                        if node_str == quest_id:
                            nd_key = quest_nodes[node_str]
                            node_amount = nd_key["GoalAmount"]
                            if current_int >= node_amount:
                                collect_the_quest(
                                    quest_slot_id,
                                    token,
                                    name,
                                    user_agent,
                                    proxy,
                                    proxy_user,
                                    proxy_password,
                                    version,
                                    data_version,
                                )
                                break
                    pass

    # Check if user wants to collect quests
    accounts = open_file(constants.py_accounts)
    for account in accounts:
        if account["name"] == name and not account["collect_quests"]:
            return
        if account["name"] == name and account["collect_quests"]:
            log_to_file(f"Account {name}: Checking quests")
            collect_quest()
            break


def collect_the_quest(
    node,
    token,
    name,
    user_agent,
    proxy,
    proxy_user,
    proxy_password,
    version,
    data_version,
):
    url = f"{constants.gameDataURL}?cn=collectQuestReward&slotId={node}&autoComplete=False&clientVersion={version}&clientPlatform=WebGL&gameDataVersion={data_version}&command=collectQuestReward&isCaptain=0"

    headers, proxies = get_request_strings(token, user_agent, proxy)
    has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)
    if has_proxy:
        response = requests.get(url, proxies=proxies, headers=headers, auth=proxy_auth)
    else:
        response = requests.get(url, proxies=proxies, headers=headers)
    has_error = handle_error_response(response)
    if has_error:
        log_to_file(
            f"Account: {name}. Failed to get quests. URL: {url}. Response: {response.json()}"
        )
        return
    else:
        pr_str = f"Account {name}: Collected {node} quest successfully."
        print(pr_str)
        log_to_file(pr_str)


def get_user_dungeon(
    user_id, raid_id, token, user_agent, proxy, proxy_user, proxy_password
):
    version, data_version = get_game_data(
        token, user_agent, proxy, proxy_user, proxy_password
    )
    headers, proxies = get_request_strings(token, user_agent, proxy)
    has_proxy, proxy_auth = get_proxy_auth(proxy_user, proxy_password)

    url = (
        constants.gameDataURL
        + "?cn=getUserDungeonInfoForRaid&userId="
        + user_id
        + "&isCaptain=0&gameDataVersion="
        + data_version
        + "&raidId="
        + raid_id
        + "&clientVersion="
        + version
        + "&clientPlatform=WebGL&command=getUserDungeonInfoForRaid"
    )

    if has_proxy:
        response = requests.get(url, proxies=proxies, headers=headers, auth=proxy_auth)
    else:
        response = requests.get(url, proxies=proxies, headers=headers)
    has_error = handle_error_response(response)
    if has_error:
        log_to_file(
            f"Account: {user_id}. Failed to get quests. URL: {url}. Response: {response.json()}"
        )
        return
    else:
        return response.json()
