import discord
from redbot.core import commands, checks
import os
import re

__author__ = "ScarletRaven"


class TitleCase(commands.Cog):
    """Stop people from writing in CamelCase"""

    def __init__(self, bot):
        self.bot = bot

    async def titlecase(self, ctx):
        """TitleCase settings"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)


    async def on_message(self, m: discord.Message):
        pattern = re.compile(r'''(?x)(\b
            [A-Z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)
            \b)''')

        def c(s): return [u[0] for u in re.findall(pattern, s)]
        user = m.author.display_name
        trigger = str(c(m.content))
        quote = trigger[2:-2]
        if await self.bot.is_automod_immune(m):
            return
        if (await self.bot.get_context(m)).valid or m.content.startswith('"') or m.content.startswith('\\'):
            return
        if m.author.bot is False and trigger != "[]":
            await self.bot.send_filtered(m.channel, content=f"{user} wrote *\"{quote}...\"* \
                                    \nPlease refrain from using weird capitals.", delete_after=30)
            try:
                await m.delete()
            except discord.errors.Forbidden:
                await m.channel.send(f"*(Wanted to delete mid {m.id} but no permissions)*")