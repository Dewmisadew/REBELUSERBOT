# Thanks to @D3_krish
# Porting in DarkUSERBOT by Dark75

import asyncio
import random
from telethon import events, version
from DarkWeb import ALIVE_NAME, Darkversion
from Dark.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from DarkWeb.cmdhelp import CmdHelp

# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DarkWeb"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

Dark = bot.uid

edit_time = 4
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/76dd5605de7340568a904.mp4"
file2 = "https://telegra.ph/file/b765c0daec4a63c286e34.mp4"
file3 = "https://telegra.ph/file/956883ad3a92d3f816040.mp4"
file4 = "https://telegra.ph/file/b765c0daec4a63c286e34.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "  __**🔥🔥𝐑𝐄𝐁𝐄𝐋 𝐁𝐎𝐓  𝐈𝐒 𝐀𝐋𝐈𝐕𝐄🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                🔰ᗰᗩՏTᗴᖇ🔰\n      **『😈[{DEFAULTUSER}](tg://user?id={Dark})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `𝚅𝚎𝚛𝚜𝚒𝚘𝚗:` `{Darkversion}`\n"
pm_caption += f"┣•➳➠ `𝚂𝚞𝚍𝚘:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `𝙲𝚑𝚊𝚗𝚗𝚎𝚕:` [𝙹𝙾𝙸𝙽](https://t.me/DarkWeb_SUPPORT)\n"
pm_caption += f"┣•➳➠ `𝙲𝚛𝚎𝚊𝚝𝚘𝚛:` [𝚁𝙴𝙱𝙴𝙻](https://t.me/Dark_IS_OP)\n"
pm_caption += f"┣•➳➠ `𝚂𝚞𝚙𝚙𝚘𝚛𝚝𝚎𝚛:` [𝙽𝙸𝚂𝙷𝚄](https://t.me/nishuop)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥𝐑𝐄𝐏𝐎🔥](https://github.com/Dark75/DarkWebOP) 🔹 [📜𝐋𝐢𝐜𝐞𝐧𝐬𝐞📜](https://github.com/Dark75/DarkWebOP/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@Dark.on(admin_cmd(outgoing=True, pattern="alive$"))
@Dark.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
CmdHelp("alive").add_command(
  "alive", None, "To check am i alive"
).add_command(
  "Dark", None, "To check am i alive with your favorite alive pic"
).add()
