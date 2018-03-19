# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from random import choice as rnd
from .utils.dataIO import dataIO
import os

__author__ = "ScarletRav3n"


class Kaomoji:
    """Japanese Emoticons"""

    def __init__(self, bot):
        self.bot = bot
        self.toggle = False
        self.feelings = "data/kaomoji/feelings.json"
        self.system = dataIO.load_json(self.feelings)

    def save_emotes(self):
        dataIO.save_json(self.feelings, self.system)
        dataIO.is_valid_json("data/kaomoji/feelings.json")

    @commands.group(aliases=["kao"], invoke_without_command=True, pass_context=True)
    async def kaomoji(self, ctx, *, category: str, n: int=None):
        str_category = category.lower()
        m = ctx.message
        if self.toggle:
            try:
                await self.bot.delete_message(m)
            except discord.errors.Forbidden:
                pass
        amount = len(self.system.get(str_category, []))
        if str_category in self.system:
            if n is None:
                await self.bot.say(rnd(self.system[str_category]))
            else:
                if n > amount:
                    await self.bot.say("The highest kaomoji count for " + str_category + " is "
                                       + str(amount) + ". \n(╯°□°）╯︵ ┻━┻")
                else:
                    await self.bot.say(self.system[str_category][n])
            print(str_category + " kaomoji called")
        else:
            await self.bot.say(str_category + " category couldn't be found. \n¯\_(ツ)_/¯")

    @kaomoji.command(pass_context=True, name="list")
    async def _list(self, ctx):
        """Shows all categories"""
        if self.toggle:
            try:
                await self.bot.delete_message(ctx.message)
            except discord.errors.Forbidden:
                pass
        categories = [i for i in self.system]
        await self.bot.say("```" + ', '.join(categories) + "```")
        print("Kaomoji list called")

    @kaomoji.command(pass_context=True)
    async def count(self, ctx, category: str):
        """Displays count per category"""
        if self.toggle:
            try:
                await self.bot.delete_message(ctx.message)
            except discord.errors.Forbidden:
                pass
        str_category = category.lower()
        amount = len(self.system[str_category])
        await self.bot.say("There are " + str(amount) + " kaomojis for " + str_category)

    @kaomoji.command()
    async def cleaner(self, on_off: str):
        """Cleans up your commands"""
        if on_off in ('on', 'enabled'):
            await self.bot.say('Deleting commands is now ON.')
            self.toggle = True
        else:
            await self.bot.say('Deleting commands is now OFF.')
            self.toggle = False


def check_folders():
    if not os.path.exists("data/kaomoji"):
        print("Creating data/kaomoji folder...")
        os.makedirs("data/kaomoji")


def check_files():
    f = "data/kaomoji/feelings.json"
    if not dataIO.is_valid_json(f):
        print("No such thing as feelings.json...")


def setup(bot):
    check_folders()
    check_files()
    n = Kaomoji(bot)
    bot.add_cog(n)
