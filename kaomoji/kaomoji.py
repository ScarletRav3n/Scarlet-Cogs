import discord
from redbot.core import commands
from redbot.core.data_manager import bundled_data_path
from random import choice as rnd
import json
import os

__author__ = "ScarletRaven"

BaseCog = getattr(commands, "Cog", object)

class Kaomoji(BaseCog):
    """Fun Emoticons"""

    def __init__(self, bot):
        self.bot = bot
        self.data = json.load(open(bundled_data_path(self) / "emoticons.json", encoding="utf8"))

    @commands.group(aliases=["kao"], invoke_without_command=True)
    async def kaomoji(self, ctx, category: str, n: int=None):
        """Call an emoticon"""
        str_category = category.lower()
        amount = len(self.data.get(str_category, []))
        if str_category in self.data:
            if n is None:
                await ctx.send(rnd(self.data[str_category]))
            else:
                if n > amount:
                    await ctx.send(f"The highest kaomoji count for {str_category} is \
                                    {str(amount)}. \n(╯°□°）╯︵ ┻━┻")
                else:
                    await ctx.send(self.data[str_category][n])
        else:
            await ctx.send(f"{str_category} category couldn't be found. \n¯\_(ツ)_/¯")

    @kaomoji.command(name="list")
    async def _list(self, ctx):
        """Shows all categories"""
        category = [i for i in self.data]
        await ctx.send(f"List of kaomoji categories: \
                        \n```{', '.join(category)}```")

    @kaomoji.command()
    async def count(self, ctx, category: str):
        """Displays count per category"""
        str_category = category.lower()
        amount = (len(self.data[str_category])-1)
        await ctx.send(f"There are **{str(amount)}** kaomojis for {str_category}")