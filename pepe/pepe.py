# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from random import choice as rnd
from .utils.dataIO import dataIO
import os

__author__ = "ScarletRav3n"


class Pepe:
    """Pepes (Some NSFW)"""

    def __init__(self, bot):
        self.bot = bot
        self.toggle = False
        self.pepe = "data/pepe/pepe.json"
        self.system = dataIO.load_json(self.pepe)
        # self.pepe = `data/pepe`

    def save_emotes(self):
        dataIO.save_json(self.pepe, self.system)
        dataIO.is_valid_json("data/pepe/pepe.json")

    @commands.group(aliases=["pepe"], invoke_without_command=True, pass_context=True)
    async def _pepe(self, ctx, *, n: int=None):
        amount = len(self.system["pepes"])
        m = ctx.message
        if n is None:
            await self.bot.say(rnd(self.system["pepes"]))
        else:
            if n > amount:
                await self.bot.say("The highest pepe count is " + str(amount) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system["pepes"][n])
        if self.toggle is True:
            try:
                await self.bot.delete_message(m)
                await self.bot.say("Deleted command msg {}".format(m.id))
            except discord.errors.Forbidden:
                await self.bot.say("Wanted to delete mid {} but no permissions".format(m.id))

    @_pepe.command()
    async def count(self):
        """Displays total count"""
        amount = len(self.system["pepes"])
        await self.bot.say("There are " + str(amount) + " pepes")

    @_pepe.command()
    async def cleaner(self, on_off: str):
        """Cleans up your commands"""
        if on_off is True:
            await self.bot.say('Deleting commands is now ON.')
            self.toggle = True
        else:
            await self.bot.say('Deleting commands is now OFF.')
            self.toggle = False


def check_folders():
    if not os.path.exists("data/pepe"):
        print("Creating data/pepe folder...")
        os.makedirs("data/pepe")


def check_files():
    f = "data/pepe/pepe.json"
    if not dataIO.is_valid_json(f):
        print("No such thing as pepe.json...")


def setup(bot):
    check_folders()
    check_files()
    n = Pepe(bot)
    bot.add_cog(n)
