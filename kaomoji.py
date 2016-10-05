# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from random import choice as rnd
from .utils.dataIO import dataIO
from .utils import checks
import os

__author__ = "ScarletRav3n"


class Kaomoji:
    """Japanese Emoticons"""

    def __init__(self, bot):
        self.bot = bot
        self.feelings = "data/kaomoji/feelings.json"
        self.system = dataIO.load_json(self.feelings)
        # self.kaomoji = `data/kaomoji`

    def save_emotes(self):
        dataIO.save_json(self.feelings, self.service)
        dataIO.is_valid_json("data/kaomoji/feelings.json")

    @commands.group(pass_context=True)
    async def kaomoji(self, ctx):
        if ctx.invoked_subcommand is None:
            print("This is a 4.0 GPA")
            await self.bot.say("This is a 4.0 GPA")
            return

    @kaomoji.command()
    async def list(self):
        k = [i for i in self.emotes]
        await self.bot.say("```" + ', '.join(k) + "```")
        print("Kaomoji list called")

    @kaomoji.command(name="excited", invoke_without_command=True)
    async def _excited(self):
        await self.bot.say(rnd(self.feelings["excited"]))

    @kaomoji.command(name="happy", invoke_without_command=True)
    async def _happy(self):
        await self.bot.say(rnd(self.feelings["happy"]))


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
