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
# TODO: Configure ignore list to be permanent
# TODO: Ignore channels/servers


class Grammar:
    """Fix those mistakes"""

    def __init__(self, bot):
        self.bot = bot
        self.toggle = False
        self.ignore = []
        self.grammar = "data/grammar/grammar.json"
        self.system = dataIO.load_json(self.grammar)

    def save_grammar(self):
        dataIO.save_json(self.grammar, self.system)
        dataIO.is_valid_json("data/grammar/grammar.json")

    @commands.group(name="grammar", pass_context=True)
    @checks.admin_or_permissions(administrator=True)
    async def _grammar(self, ctx):
        """Grammar commands"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    @_grammar.command(name="ignore")
    async def _ignore(self, trigger: str):
        """Ignores fixes that may be annoying"""
        self.ignore.append(trigger)
        await self.bot.say('"' + trigger + '" is now being ignored.')

    @_grammar.command(name="list")
    async def _list(self):
        """Pull up grammar being ignored"""
        await self.bot.say(str(self.ignore).strip('[]') + '\nare all being ignored.')

    @_grammar.command()
    async def caret(self, on_off: bool):
        """Toggle ^ caret deletion"""
        if on_off is True:
            await self.bot.say('Deleting carets is now ON.')
            self.toggle = True
        else:
            await self.bot.say('Deleting carets is now OFF.')
            self.toggle = False

    async def on_message(self, m):
        for x in self.bot.settings.get_prefixes(m.server):
            if m.author.bot is False and m.content.startswith(x):
                return
            for k, v in self.system.items():
                if re.findall(r'\b' + k + r'\b', m.content.lower()):
                    if k not in self.ignore:
                        await self.bot.send_message(m.channel, v)
                elif "^" in m.content:  # caret
                    if self.toggle is True:
                        try:
                            await self.bot.delete_message(m)
                        except discord.errors.Forbidden:
                            await self.bot.say('Wanted to delete mid {} but no permissions'.format(m.id))


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
