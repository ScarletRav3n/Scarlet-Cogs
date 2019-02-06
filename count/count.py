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
        self.cjson = cog_data_path(self) / 'count.json'
        try:
            open(self.cjson, 'r')
        except IOError:
            json.dump({}, open(self.cjson, 'w'))

    @commands.command()
    @checks.admin_or_permissions(administrator=True)
    async def count(self, ctx, on_off: bool):
        """Toggle counting for commands"""
        if on_off is True:
            await ctx.send('Counting counter is now ON.')
            self.toggle = True
        else:
            await ctx.send('Counting counter is now OFF.')
            self.toggle = False
    
    async def counter(self, ctx, count):
        if self.toggle:
            await ctx.send(f"*This command has been used {count} times.*")

    async def on_command(self, ctx):
        k = str(ctx.command)
        m = ctx.message
        if m.author.bot is False:
            with open(self.cjson, 'r') as f:
                data = json.load(f)
                if not k in data:
                    data[k] = 0
                data[k] += 1
                await self.counter(ctx, count = data[k])
            with open(self.cjson, 'w') as f:
                json.dump(data, f, sort_keys=True, indent=4)
