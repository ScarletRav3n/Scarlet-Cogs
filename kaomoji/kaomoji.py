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

    @commands.group(pass_context=True, aliases=["kao"])
    async def kaomoji(self, ctx):
        if ctx.invoked_subcommand is None:
            print("This is a 4.0 GPA")
            await self.bot.say("This is a 4.0 GPA")  # placeholder
            return

    @kaomoji.command(name="list")
    async def _list(self):
        k = [i for i in self.system]
        await self.bot.say("```" + ', '.join(k) + "```")
        print("Kaomoji list called")

    @kaomoji.command()
    async def excited(self, n: int=None):
        c = "excited"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def happy(self, n: int=None):
        c = "happy"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def love(self, n: int=None):
        c = "love"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def success(self, n: int=None):
        c = "success"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def confused(self, n: int=None):
        c = "confused"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def crazy(self, n: int=None):
        c = "crazy"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def hungry(self, n: int=None):
        c = "hungry"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def meh(self, n: int=None):
        c = "meh"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def shy(self, n: int=None):
        c = "shy"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def smug(self, n: int=None):
        c = "smug"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def surprised(self, n: int=None):
        c = "surprised"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def angry(self, n: int=None):
        c = "angry"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def hurt(self, n: int=None):
        c = "hurt"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def sad(self, n: int=None):
        c = "sad"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def scared(self, n: int=None):
        c = "scared"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")

    @kaomoji.command()
    async def worried(self, n: int=None):
        c = "worried"
        b = len(self.system[c])
        if n is None:
            await self.bot.say(rnd(self.system[c]))
        else:
            if n > b:
                await self.bot.say("The highest kaomoji count for " + c + " is " + str(b) + ". \n(╯°□°）╯︵ ┻━┻")
            else:
                await self.bot.say(self.system[c][n])
        print(c + " kaomoji called")


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
