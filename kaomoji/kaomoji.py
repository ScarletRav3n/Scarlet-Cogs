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
        self.feelings = "data/kaomoji/feelings.json"
        self.system = dataIO.load_json(self.feelings)
        # self.kaomoji = `data/kaomoji`

    def save_emotes(self):
        dataIO.save_json(self.feelings, self.service)
        dataIO.is_valid_json("data/kaomoji/feelings.json")

    @commands.group(aliases=["kao"], invoke_without_command=True)
    async def kaomoji(self, category: str, number: int=None):
        c = category.lower()
        l = len(self.system[c])
        n = number
        # global b
        if c in self.system:
            if n is None:
                await self.bot.say(rnd(self.system[c]))
                # print(b)
            else:
                if n > l:
                    await self.bot.say("The highest kaomoji count for " + c + " is " + str(l) + ". \n(╯°□°）╯︵ ┻━┻")
                else:
                    await self.bot.say(self.system[c][n])
            print(c + " kaomoji called")
        else:
            await self.bot.say(c + "category not found. \n¯\_(ツ)_/¯")

    @kaomoji.command(name="list")
    async def _list(self):
        """Shows all categories"""
        k = [i for i in self.system]
        await self.bot.say("```" + ', '.join(k) + "```")
        print("Kaomoji list called")

    @kaomoji.command()
    async def count(self, category: str):
        """Displays count per category"""
        c = category.lower()
        l = len(self.system[c])
        await self.bot.say("There are " + str(l) + " kaomojis for " + c)

    # ----- cleanup function ------
    # @kaomoji.command()
    # async def cleaner(self, on_off: str):
    #     """Cleans up your commands"""
    #     global b
    #     _b = on_off.lower()
    #     if _b == "on":
    #         await self.bot.say("Cleaner is now ON ")
    #         b = True
    #     elif _b == "off":
    #         await self.bot.say("Cleaner is now OFF ")
    #         b = False
    #     else:
    #         await self.bot.say("It needs an ON or OFF state")


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
