# noinspection PyUnresolvedReferences
import discord
import re

__author__ = "ScarletRav3n"


class TitleCase:
    """Stop people from writing in CamelCase"""

    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, m):
        pattern = re.compile(r'''(?x)(\b
            [A-Z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)
            \b)''')

        def c(s): return [u[0] for u in re.findall(pattern, s)]
        trigger = str(c(m.content))
        for x in self.bot.settings.get_prefixes(m.server):
            if m.content.startswith(x) or m.content.startswith('"') or m.content.startswith('\\'):
                return
            if m.author.bot is False and trigger != "[]":
                trigger = str(m.author.name) + ' wrote *"' + trigger[2:-2] + '..."*'
                await self.bot.send_message(m.channel, trigger + "\nPlease refrain from using titlecase")
                try:
                    await self.bot.delete_message(m)
                except discord.errors.Forbidden:
                    await self.bot.send_message(m.channel, "(Wanted to delete mid {} but no permissions)".format(m.id))


def setup(bot):
    n = TitleCase(bot)
    bot.add_cog(n)
