# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
import json
import os


def get_user_list(config, key):
    with open(f"{os.getcwd()}/NekoRobot/{config}", "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 25924955  # integer value, dont use ""
    API_HASH = "140d8d0ad7c45e934d82dfcbba019e0d"
    TOKEN = "5805856990:AAHixt2Cm-elIJAjDSmAqcEVx22CQfePUl8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    STRING_SESSION = "1BVtsOHIBu2rl_TGeWeLMnP5D0L125IuHjh4jG8FMu7Ebn7NLtkMwGlHuJRPAa2rbOIMXKXWds83Elj4hSXqlxOsQq2NzNe4aF97Q-46msoOF1iOqFHHLC6PEDxJSrK2VZBnBJQK-RXS7cwxLU-Sk08zUdzduzSNWgxnyfGEurJ5y3-6f3O0HFWr1nSaakWe_l6wP5f27aE_9jir77QpFVHVA1UV_8CA1FHJbSati6Uyr8ERmcfpmjlpOqnkyptNXd9LgBcjDwGrCwJ3Rr3yjD5EbEap6h2Tx_-kfgeMZpyEEwmhHAQLDfiT1OVW0Sup6hfX7jsxMRT7kE1Wn2_PWzQq5bdcQA-0="
    OWNER_ID = 1784179805  # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "xtelr"
    SUPPORT_CHAT = "satpamajg"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001873253940
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001873253940
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://fsanpeav:ndB0XnZ4tbm887rtDk4DQuSl5lOBlcE_@hansken.db.elephantsql.com:5432/fsanpeav"  # needed for any database modules
    DB_URL = ""
    REDIS_URL = "redis-12905.c9.us-east-1-4.ec2.cloud.redislabs.com:12905"
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "P5_FWlwgUrpchwJceZDUSDxa41G396dn7J0vSEMWeBhHJ6C4q8VJLzjhfZPxNKUZ"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "MTUCS6JPUFR8XRPO"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "EYO2G96ONPI6"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "awoo"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True  # Create a new config.py or rename this to config.py file in same dir and import, then extend this class.


import json
import os


def get_user_list(config, key):
    with open(f"{os.getcwd()}/NekoRobot/{config}", "r") as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = 25924955  # integer value, dont use ""
    API_HASH = "140d8d0ad7c45e934d82dfcbba019e0d"
    TOKEN = "5805856990:AAHixt2Cm-elIJAjDSmAqcEVx22CQfePUl8"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = 1784179805 # If you dont know, run the bot and do /id in your private chat with it, also an integer
    OWNER_USERNAME = "xtelr"
    SUPPORT_CHAT = "satpamajg"  # Your own group for support, do not add the @
    JOIN_LOGGER = (
        -1001873253940
    )  # Prints any new group the bot is added to, prints just the name and ID.
    EVENT_LOGS = (
        -1001873253940
    )  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = "postgres://fsanpeav:ndB0XnZ4tbm887rtDk4DQuSl5lOBlcE_@hansken.db.elephantsql.com:5432/fsanpeav"  # needed for any database modules

   # needed for any database modules
    DB_URL = ""
    LOAD = []
    NO_LOAD = ["rss", "cleaner", "connection", "math"]
    WEBHOOK = False
    INFOPIC = True
    URL = None
    SPAMWATCH_API = "P5_FWlwgUrpchwJceZDUSDxa41G396dn7J0vSEMWeBhHJ6C4q8VJLzjhfZPxNKUZ"  # go to support.spamwat.ch to get key
    SPAMWATCH_SUPPORT_CHAT = "@SpamWatchSupport"

    # OPTIONAL
    ##List of id's -  (not usernames) for users which have sudo access to the bot.
    DRAGONS = get_user_list("elevated_users.json", "sudos")
    ##List of id's - (not usernames) for developers who will have the same perms as the owner
    DEV_USERS = get_user_list("elevated_users.json", "devs")
    ##List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    DEMONS = get_user_list("elevated_users.json", "supports")
    # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    TIGERS = get_user_list("elevated_users.json", "tigers")
    WOLVES = get_user_list("elevated_users.json", "whitelists")
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  # Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = (
        8  # Number of subthreads to use. Set as number of threads your processor uses
    )
    BAN_STICKER = ""  # banhammer marie sticker id, the bot will send this sticker before banning or kicking a user in chat.
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = (
        "MTUCS6JPUFR8XRPO"  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = "awoo"  # Get your API key from https://timezonedb.com/api
    WALL_API = (
        "EYO2G96ONPI6"  # For wallpapers, get one from https://wall.alphacoders.com/api.php
    )
    AI_API_KEY = "awoo"  # For chatbot, get one from https://coffeehouse.intellivoid.net/dashboard
    BL_CHATS = []  # List of groups that you want blacklisted.
    SPAMMERS = None


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
