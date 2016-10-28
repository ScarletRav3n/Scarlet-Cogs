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
        self.pepe = "data/pepe/pepe.json"
        self.system = dataIO.load_json(self.pepe)
        # self.pepe = `data/pepe`

    def save_emotes(self):
        dataIO.save_json(self.pepe, self.system)
        dataIO.is_valid_json("data/pepe/pepe.json")

    @commands.group(aliases=["pepe"], invoke_without_command=True)
    async def _pepe(self, n: int=None):
        l = len(self.system["pepes"])
        print("step 1")
        if n is None:
            print("step 2a")
            await self.bot.say(rnd(self.system["pepes"]))
            print("step 2b")
        else:
            print("step 3")
            if n > l:
                print("step 4a")
                await self.bot.say("The highest pepe count is " + str(l) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                print("step 4b")
                await self.bot.say(self.system["pepes"][n])

    @_pepe.command()
    async def count(self):
        """Displays total count"""
        l = len(self.system["pepes"])
        await self.bot.say("There are " + str(l) + " pepes")


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
