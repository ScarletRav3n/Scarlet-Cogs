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

    @commands.group(pass_context=True)
    async def kaomoji(self, ctx):
        if ctx.invoked_subcommand is None:
            print("This is a 4.0 GPA")
            await self.bot.say("This is a 4.0 GPA")
            return

    @kaomoji.command(name="list")
    async def _list(self):
        k = [i for i in self.feelings]
        await self.bot.say("```" + ', '.join(k) + "```")
        print("Kaomoji list called")

    @kaomoji.command(invoke_without_command=True)
    async def excited(self):
        await self.bot.say(rnd(self.feelings["excited"]))

    @kaomoji.command(invoke_without_command=True)
    async def happy(self):
        await self.bot.say(rnd(self.feelings["happy"]))

    @kaomoji.command(invoke_without_command=True)
    async def love(self):
        await self.bot.say(rnd(self.feelings["love"]))

    @kaomoji.command(invoke_without_command=True)
    async def success(self):
        await self.bot.say(rnd(self.feelings["success"]))

    @kaomoji.command(invoke_without_command=True)
    async def confused(self):
        await self.bot.say(rnd(self.feelings["confused"]))

    @kaomoji.command(invoke_without_command=True)
    async def crazy(self):
        await self.bot.say(rnd(self.feelings["crazy"]))

    @kaomoji.command(invoke_without_command=True)
    async def hungry(self):
        await self.bot.say(rnd(self.feelings["hungry"]))

    @kaomoji.command(invoke_without_command=True)
    async def meh(self):
        await self.bot.say(rnd(self.feelings["meh"]))

    @kaomoji.command(invoke_without_command=True)
    async def shy(self):
        await self.bot.say(rnd(self.feelings["shy"]))

    @kaomoji.command(invoke_without_command=True)
    async def smug(self):
        await self.bot.say(rnd(self.feelings["smug"]))

    @kaomoji.command(invoke_without_command=True)
    async def surprised(self):
        await self.bot.say(rnd(self.feelings["surprised"]))

    @kaomoji.command(invoke_without_command=True)
    async def angry(self):
        await self.bot.say(rnd(self.feelings["angry"]))

    @kaomoji.command(invoke_without_command=True)
    async def hurt(self):
        await self.bot.say(rnd(self.feelings["hurt"]))

    @kaomoji.command(invoke_without_command=True)
    async def sad(self):
        await self.bot.say(rnd(self.feelings["sad"]))

    @kaomoji.command(invoke_without_command=True)
    async def scared(self):
        await self.bot.say(rnd(self.feelings["scared"]))

    @kaomoji.command(invoke_without_command=True)
    async def worried(self):
        await self.bot.say(rnd(self.feelings["worried"]))


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
