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
            [A-Z](\S*?)[ ]
            [A-Z](\S*?)[ ]
            [A-Z](\S*?)[ ]
            [A-Z](\S*?)
            \b)''')
        c = lambda s: [u[0] for u in re.findall(pattern, s)]
        p = str(c(m.content))
        if m.author != self.bot.user:
            if p != "[]":
                p = str(m.author.name) + ' wrote *"' + p[2:-2] + '"*'
                try:
                    await self.bot.delete_message(m)
                except:
                    pass
                await self.bot.send_message(m.channel, p + "\nPlease refrain from using TitleCase")


def setup(bot):
    n = TitleCase(bot)
    bot.add_cog(n)
