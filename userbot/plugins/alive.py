import asyncio
from telethon import version
from telethon.events import InlineQuery
from telethon.sync import custom
from telethon import events, Button
from userbot import ALIVE_NAME, REBELversion
from userbot.cmdhelp import CmdHelp
from userbot.smex.DARK_Config import Config
from userbot.utils import admin_cmd, sudo_cmd
from userbot import *

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK WEB"

ludosudo = Config.SUDO_USERS

sudou = "True" if ludosudo else "False"
REBEL = bot.uid
"""
 BUTTON = "[
                [
                    Button.url(
                        "SUPPORT CHAT", f"t.me/DARK_WEB_BOT_SUPPORT")
                ],
                [
                    Button.url(
                        "CHANNEL", f"t.me/DARK_WEB_UB")
                ],

            ],"
"""
edit_time = 1
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/76dd5605de7340568a904.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥𝐑𝐄𝐁𝐄𝐋 𝐁𝐎𝐓  𝐈𝐒 𝐀𝐋𝐈𝐕𝐄🔥🔥**__\n\n" + "**━━━━━━━━━━━━━━━━━━━━━━**\n\n"


pm_caption += (
    f"                🔰ᗰᗩՏTᗴᖇ🔰\n      **『[{DEFAULTUSER}](tg://user?id={REBEL})』**\n\n"
)
pm_caption += "┏━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠  `ᴛᴇʟᴇᴛʜᴏɴ:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `ᴠᴇʀsɪᴏɴ:` `{REBELversion}`\n"
pm_caption += f"┣•➳➠ `sᴜᴅᴏ:` `{sudou}`\n"
pm_caption += "┣•➳➠ `ᴄʜᴀɴɴᴇʟ:` [ᴊᴏɪɴ](https://t.me/REBELBOT_SUPPORT)\n"
pm_caption += "┣•➳➠ `ᴄʀᴇᴀᴛᴏʀ:` [ʀᴇʙᴇʟ](https://t.me/REBEL_IS_OP)\n"
pm_caption += "┣•➳➠ `sᴜᴘᴘᴏʀᴛᴇʀ:` [sᴜᴘᴘᴏʀᴛ](https://t.me/REBELSSUPPORT)\n"
pm_caption += "┗━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥𝚁𝙴𝙿𝙾🔥](https://github.com/TEAMREBELS/REBELBOT) 🔹 [📜𝙻𝚒𝚌𝚎𝚗𝚜𝚎📜](https://github.com/TEAMREBELS/REBELBOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1, caption=pm_caption, Button=BUTTON)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()


CmdHelp("alive").add_command("alive", None, "To check am i alive").add_command(
    "rebel", None, "To check am i alive with your favorite alive pic"
).add()
