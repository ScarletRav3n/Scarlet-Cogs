# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from cogs.utils import checks
from random import randint
from random import choice

__author__ = "ScarletRav3n"


# TODO: make random change to trigger
# TODO: add lists for randoms
# TODO: json or sometingnggn and add/delete

class CommandSpice:
    """spice up everyday commands"""

    def __init__(self, bot):
        self.bot = bot

    async def on_command(self, command, ctx):
        m = ctx.message
        com = str(command)
        if m.author.bot is not True:
            if "ping" == com:
                re = "You're too slow"
            elif "version" == com:
                re = "Do I need the latest tech?"
            elif "unmute" == com:
                re = "Permission to speak: Granted"
            elif "unignore" == com:
                re = "Can you hear me now?"
            elif "urban" == com:
                re = "Don't think I'm happy about this"
            elif "userinfo" == com:
                re = "Quite the looker"
            elif "serverinfo" == com:
                re = "This is my home"
            elif "lmgtfy" == com:
                re = "This helps...right?"
            elif "leaderboard" == com:
                re = "Am I in here?"
            else:
                return
            await self.bot.send_message(m.channel, re)


def setup(bot):
    n = CommandSpice(bot)
    bot.add_cog(n)
