from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.smex.DARK_Config import Config
from userbot import *
from userbot.utils import load_module
from userbot import LOAD_PLUG, Darkversion
from pathlib import Path
import asyncio
import telethon.utils

os.system("pip install -U telethon")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.BOT_TOKEN)
        print("Initialisation finished with no errors")
        print("🔰ՏTᗩᖇT ᖇᗴᗷᗴᒪᗷOT🔰")
        bot.loop.run_until_complete(add_bot(Var.BOT_USERNAME))
        print("⚡ᖇᗴᗷᗴᒪᗷOT ՏTᗩᖇTᑌᑭ ᑕOᗰᑭᒪᗴTᗴᗪ⚡")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print(f"""Hello sir i am REBELBOT!! REBELBOT VERSION :- {REBELversion} YOUR REBELBOT IS READY! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @REBELBOT_SUPPORT .""")

if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
