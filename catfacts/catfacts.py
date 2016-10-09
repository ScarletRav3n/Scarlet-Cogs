# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from random import choice as rnd
from .utils.dataIO import dataIO
import os

__author__ = "ScarletRav3n"


class CatFacts:
    """Cat Facts"""

    def __init__(self, bot):
        self.bot = bot
        self.cat = "data/catfacts/catfacts.json"
        self.system = dataIO.load_json(self.cat)
        # self.kaomoji = `data/kaomoji`

    def save_emotes(self):
        dataIO.save_json(self.cat, self.service)
        dataIO.is_valid_json("data/catfacts/catfacts.json")

    @commands.group(aliases=["cat"], invoke_without_command=True)
    async def catfacts(self):
        await self.bot.say(rnd(self.system))

    @catfacts.command()
    async def count(self):
        l = len(self.system)
        await self.bot.say("I have " + str(l) + " cat facts loaded.")

    @catfacts.command()
    async def number(self, number: int):
        l = len(self.system)
        n = number
        if n > l:
            await self.bot.say("I only have " + str(l) + " cat facts!")
        else:
            await self.bot.say(self.system[n])


def check_folders():
    if not os.path.exists("data/kaomoji"):
        print("Creating data/catfacts folder...")
        os.makedirs("data/catfacts")


def check_files():
    f = "data/catfacts/catfacts.json"
    if not dataIO.is_valid_json(f):
        print("No such thing as catfacts.json...")


def setup(bot):
    check_folders()
    check_files()
    n = CatFacts(bot)
    bot.add_cog(n)