# PyRaiders - SR assistant written in Python.

### For bugs and issues please check the logger.txt file.
### Do not share your logger.txt publicly, it contains information that identifies your SR account.

## Want to help me with testing?
Join the server: [![Static Badge](https://img.shields.io/badge/Discord-Discord?style=for-the-badge&logo=discord&color=%23C5CAE9)](https://discord.gg/Egu7v8V8Dz)<br>
If you can, run PyRaiders using Visual Studio Code to better track issues.

### This is still in Alpha:
It can autonomously rotate slots, place units and collect quests.<br>
For every option available please check the bottom of this page<br>
You can set captain priority and block lists.<br>
You can set which units you want to use.<br>
It can place epic units, but it is still unprecise and is causing placement loops due to marker offsetting.<br>

### Can I get banned from using this tool?
Since this is an automation tool there is the possibility of having your account shadowbanned or banned completely, so use it with caution.<br>
So far, neither the accounts that I am using nor the person assisting me in testing have been banned. I believe that as long as the tool does not do anything noticeably sketchy it should not be banned. However it is not foolproof and does not prevent individual captains from being suspicious about placements.<br>
I am trying to emulate the human behaviour as much as possible while avoiding unhuman behaviour such as rapid firing tasks.

### Multi account placements:
Unless you are using the priority list the tool will randomly select the captains so each account will be placing with its own set of captains preventing a bot swarm from happening. However, randomness allows that multiple accounts select the same captain <br>
It will always place near the captain (or any random unit if the captain does not place one) whilst following the markers.

### Requirements:
Python3.

### Non-mandatory requirements:
PyQt, QtWebEngine, selenium, chromedriver and a chromium based browser

### Quickly open the terminal on windows
On PyRaiders folder, click the address bar, type ```cmd``` and press ENTER. Use the shortcut CTRL+L to quickly focus the address bar.
Another quick way to open the terminal is to press CTRL+R, type cmd and press ENTER. However this requires navigating to the PyRaiders folder.

Double click or execute ```python3 setup.py``` to install the Python dependencies.
Chromedriver and the browser must be installed manually. Ensure that they are compatible. Example: Chromedriver 120.0 == Chromium browser 120.0

## There are 3 ways to set up your account
Your account name is not necessarily the Twitch name, it is just a random unique name used to identify your account within PyRaiders.

To obtain the token, scapmpid and scsession open a browser, login to SR, right-click, Inspect elements, open dev tool -> Application -> Cookies -> SR website and get the values.
You can also use a browser extension such as Cookie Quick Manager or alternatives to help you quickly find your cookies.

### Manual: 
Run ```python3 run.py``` once for the first time. It will create a py_accounts.json file with a template, use the template at the end of the page to add other new accounts.

### Guided:
Run ```python3 helper_tools add_account``` or ```python3 helper_tools a```
Follow the instructions, you will need the token, scapmpid and the scsession.

### Simplified (Requires PyQt and QtWebEngine)
Run ```python3 helpre_tools simple_login``` or ```python3 helpre_tools s```
Add your account name, a browser will load, login to your Twitch account.

You can add as many accounts as you want with any method you prefer, you do not have to use the same method everytime.

# Once you added at least one account double click or execute ```python3 run.py``` to start the assistant

## Determine which units should be used 
Run ```python3 helper_tools change_priority``` or ```python3 helper_tools c```
Type the name of the account, a list of units will load, copy and paste the id of the unit you want to edit and set a priority number.<br>
0 -> Will be completely ignored.<br>
1 -> Highest priority.<br>
The higher the number, the lowest the priority. They all have a default of 1 meaning their priority is all the same.

## Quick access to your account (Requires selenium, chromedriver and a chromium browser)
After installing the chromedriver, go to the assistant folder /utils/ and edit the ```chrome_driver_path``` (8th line) at file ```constants.py``` with the path to your chromedriver.exe. Keep in mind that it is not the chromedriver folder, it is the chromedriver executable itself without the ".exe". There are path examples there to help you.

Run ```python3 helper_tools load_browser``` or ```python3 helper_tools l```
Add the name of the account you want to access then press ENTER.

## Use the following template when adding new accounts, you only need to add the unique account name, token, scapmpid and scsession, the rest is generated by the application.
## The assistant works perfectly fine with the default settings so you do not have to change if you do not want to.
Potions not yet implemented.
```
    {
        "name": "",
        "token": "",
        "scapmpid": "",
        "scsession": "",
        "powered_on": true,
        "preserve_loyalty": 0,
        "switch_if_preserve_loyalty": false,
        "switch_on_idle": true,
        "minimum_idle_time": 15,
        "unlimited_campaign": false,
        "unlimited_clash": false,
        "unlimited_duels": false,
        "unlimited_dungeons": false,
        "any_captain": true,
        "only_masterlist": false,
        "masterlist": ["", "", ""],
        "ignore_blocklist": false,
        "blocklist": ["", "", ""],
        "temporary_ignore": [{"capNm": "", "time": ""}],
        "user_agent": "",
        "proxy": "",
        "proxy_user": "",
        "proxy_password": "",
        "use_potions": false,
        "has_pass": false,
        "userId": "",
        "otherUserId": "",
        "favorites_only": false,
        "favoriteCaptainIds": "",
        "slots": 3,
        "units": ""
    }
```