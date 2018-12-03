import discord
from redbot.core import commands, checks
import os
import re

__author__ = "ScarletRav3n"


class TitleCase:
    """Stop people from writing in CamelCase"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    @checks.admin_or_permissions(administrator=True)
    async def titlecase(self, ctx):
        """TitleCase settings"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)


    async def on_message(self, ctx, m: discord.Message):
        pattern = re.compile(r'''(?x)(\b
            [A-Z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)
            \b)''')

        def c(s): return [u[0] for u in re.findall(pattern, s)]
        trigger = str(c(m.content))
        for x in await self.bot.get_prefix(m):
            if m.content.startswith(x) or m.content.startswith('"') or m.content.startswith('\\'):
                return
            if m.author.bot is False and trigger != "[]":
                await ctx.m.channel.send("{0} wrote *\"{1}...\"* \
                                        \nPlease refrain from using weird title setences.".format
                                        (str(m.author.name), trigger[2:-2]), delete_after=30)
                try:
                    await ctx.delete()
                except discord.errors.Forbidden:
                    await ctx.m.channel.send("*(Wanted to delete mid {0} but no permissions)*"
                                        .format(m.id))