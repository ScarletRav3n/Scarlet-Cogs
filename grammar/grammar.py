# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from cogs.utils import checks
from .utils.dataIO import dataIO
import re
import os

__author__ = "ScarletRav3n"


# TODO: Find a better way to trigger a/an's
# TODO: Allow self added fixes?


class Grammar:
    """Fix those mistakes"""

    def __init__(self, bot):
        self.bot = bot
        self.toggle = False
        self.grammar = "data/grammar/grammar.json"
        self.system = dataIO.load_json(self.grammar)

    def save_grammar(self):
        dataIO.save_json(self.grammar, self.system)
        dataIO.is_valid_json("data/grammar/grammar.json")

    @commands.command()
    @checks.admin_or_permissions(administrator=True)
    async def grammar(self, on_off: str):
        """Toggle ^ caret deletion"""
        if on_off.lower() == "on":
            await self.bot.say("Deleting carets is now ON." +
                               "\n`Make sure I have the 'manage_messages' " +
                               "permission`")
            self.toggle = True
        elif on_off.lower() == "off":
            await self.bot.say("Deleting carets is now OFF.")
            self.toggle = False
        else:
            await self.bot.say("I need an ON or OFF state.")

    async def on_message(self, m):
        for x in self.bot.settings.get_prefixes(m.server):
            if m.author.bot is False:
                if m.content.startswith(x):
                    return
                for k, v in self.system.items():
                    if re.findall(r'\b' + k + r'\b', m.content.lower()):
                        await self.bot.send_message(m.channel, v)
                    elif "^" in m.content:  # caret
                        if self.toggle is True:
                            try:
                                await self.bot.delete_message(m)
                            except discord.errors.Forbidden:
                                await self.bot.say("Wanted to delete mid {} but no permissions".format(m.id))


def check_folders():
    if not os.path.exists("data/grammar"):
        print("Creating data/grammar folder...")
        os.makedirs("data/grammar")


def check_files():
    f = "data/grammar/grammar.json"
    if not dataIO.is_valid_json(f):
        print("No such thing as grammar.json...")


def setup(bot):
    n = Grammar(bot)
    bot.add_cog(n)
