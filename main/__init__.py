#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "28876320" #config("API_ID", default=None, cast=int)
API_HASH = "5e073859e6dfccb4d8e83545761a2260" #config("API_HASH", default=None)
BOT_TOKEN = "7239072318:AAFMusQWks7MvvsoAm7fFg2e4_Z1ws4XzZY" #config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
FORCESUB = "ludblux" #config("FORCESUB", default=None)
AUTH = "6332636383" #config("AUTH", default=None)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
