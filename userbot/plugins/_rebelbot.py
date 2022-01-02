"""REBELBOT Help Command"""

from REBELBOT.utils import *

from userbot import *
from userbot import CMD_HELP


@bot.on(admin_cmd(pattern="helps(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="helps(?: |$)(.*)", allow_sudo=True))
async def REBELBOT(event):
    if event.fwd_from:
        return
    """ .plinfo cmd """
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(str(CMD_HELP[args]))
        else:
            await event.edit(["NEED_PLUGIN"])
    else:
        string = ""
        sayfa = [
            sorted(list(CMD_HELP))[i : i + 5]
            for i in range(0, len(sorted(list(CMD_HELP))), 5)
        ]

        for i in sayfa:
            string += "`▶️ `"
            for sira, a in enumerate(i):
                string += "`" + str(a)
                string += "`" if sira == i.index(i[-1]) else "`, "
            string += "\n"
        await event.edit(["NEED_MODULE"] + "\n\n" + string)
