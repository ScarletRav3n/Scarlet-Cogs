import discord
from redbot.core import commands
from redbot.core.data_manager import bundled_data_path
import random
import json
import os

__author__ = "ScarletRaven"


BaseCog = getattr(commands, "Cog", object)

class Spice(BaseCog):
    """spice up everyday commands"""

    def __init__(self, bot):
      self.bot = bot
      with open(bundled_data_path(self) / "commandspice.json") as f:
        self.data = json.load(f)

    async def on_command(self, ctx):

      m = ctx.message
      if m.author.bot is False:
        for k, v in self.data.items():
          vchoice = random.choice(v)
          if (k in str(ctx.command)) & (vchoice != ""):
            await ctx.send(vchoice)
