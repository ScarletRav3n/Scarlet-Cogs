# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
import re

__author__ = "ScarletRav3n"


class TitleCase:
    """Stop people from writing in CamelCase"""

    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, m):
        pattern = re.compile(r'''(?x)(\b
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)
            \b)''')

        def c(s): return [u[0] for u in re.findall(pattern, s)]
        trigger = str(c(m.content))
        if m.author.bot is False:
            if trigger != "[]":
                trigger = str(m.author.name) + ' wrote *"' + trigger[2:-2] + '--"*'
                try:
                    await self.bot.delete_message(m)
                except discord.errors.Forbidden:
                    await self.bot.send_message(m.channel, "Wanted to delete mid {} but no permissions".format(m.id))
                await self.bot.send_message(m.channel, trigger + "\nPlease refrain from using TitleCase")


def setup(bot):
    n = TitleCase(bot)
    bot.add_cog(n)
