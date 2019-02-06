import discord
from redbot.core import commands, checks
from redbot.core.data_manager import cog_data_path
import json
import os

__author__ = "ScarletRaven"


BaseCog = getattr(commands, "Cog", object)

class Count(BaseCog):
    """Count all commands used"""

    def __init__(self, bot):
        self.bot = bot
        self.toggle = False
        self.path = cog_data_path(self) / 'count.json'
        try:
            f = open(self.path, 'r')
        except IOError:
            json.dump({}, open(self.path, 'w'))
        self.load_data = json.load(f)

    @commands.group(invoke_without_command=True)
    async def count(self, ctx, *, command: str):
        """Call count for command"""
        str_command = command.lower()
        if str_command in self.load_data:
            await self.counter(ctx, command = str_command, count = self.load_data[str_command])
        else:
            await ctx.send(f"**{str_command}** command hasn't been used.")

    async def counter(self, ctx, command, count):
        await ctx.send(f"**{command}** has been used {count} times.")

    @count.command()
    @checks.admin_or_permissions(administrator=True)
    async def all(self, ctx):
        """List all command counts"""
        all_data = json.dumps(self.load_data, sort_keys=True, indent=0)
        for ch in ['"', ',', "{", "}"]:
            if ch in all_data:
                all_data = all_data.replace(ch, '')
        await ctx.send(f"List of all commands counted: \
                        \n```json\n{all_data}```")

    async def on_command(self, ctx):
        k = str(ctx.command)
        if ctx.message.author.bot is False:
            if not k in self.load_data:
                self.load_data[k] = 0
            self.load_data[k] += 1
        with open(self.path, 'w') as f:
            json.dump(self.load_data, f, sort_keys=True, indent=4)