# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from .utils.dataIO import dataIO
import random
import os

__author__ = "ScarletRav3n"


class CommandSpice:
    """spice up everyday commands"""

    def __init__(self, bot):
        self.bot = bot
        self.spice = "data/commandspice/commandspice.json"
        self.system = dataIO.load_json(self.spice)

    def save_grammar(self):
        dataIO.save_json(self.spice, self.system)
        dataIO.is_valid_json("data/grammar/commandspice.json")

    async def on_command(self, command, ctx):
        m = ctx.message
        if m.author.bot is False:
            for k, v in self.system.items():
                if k in str(command):
                    await self.bot.send_message(m.channel, random.choice(v))


def check_folders():
    if not os.path.exists("data/commandspice"):
        print("Creating data/commandspice folder...")
        os.makedirs("data/commandspice")


def check_files():
    f = "data/commandspice/commandspice.json"
    if not dataIO.is_valid_json(f):
        print("No such thing as grammar.json...")


def setup(bot):
    n = CommandSpice(bot)
    bot.add_cog(n)
