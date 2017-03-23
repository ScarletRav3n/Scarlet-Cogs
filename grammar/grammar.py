# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from cogs.utils import checks
from .utils.dataIO import dataIO
import re
import os

__author__ = "ScarletRav3n"


# TODO: Find a better way to trigger a/an's


class Grammar:
    """Fix those mistakes"""

    def __init__(self, bot):
        self.bot = bot
        self.toggle = False
        self.grammar = dataIO.load_json("data/grammar/grammar.json")
        self.ignore = dataIO.load_json("data/grammar/ignorelist.json")

    def save_grammar(self):
        dataIO.save_json(self.grammar, self.ignore)
        dataIO.is_valid_json("data/grammar/grammar.json")
        dataIO.is_valid_json("data/grammar/ignorelist.json")

    @commands.group(name="grammar", pass_context=True)
    @checks.admin_or_permissions(administrator=True)
    async def _grammar(self, ctx):
        """Grammar commands"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    @commands.group(name="grammarignore", aliases=["gignore"], pass_context=True)
    @checks.admin_or_permissions(administrator=True)
    async def grammar_ignore(self, ctx):
        """Edit the ignores of a server"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)
            await self.bot.say(self.count_ignored())

    @grammar_ignore.command(name="grammar")
    async def ignore_grammar(self, trigger: str):
        """Ignore certain grammar triggers"""
        if trigger not in self.ignore['GRAMMAR']:
            self.ignore['GRAMMAR'].append(trigger)
            dataIO.save_json("data/grammar/ignorelist.json", self.ignore)
            await self.bot.say('"' + trigger + '" is now in the ignore list.')
        else:
            await self.bot.say('"' + trigger + '" is already being ignored.')

    @grammar_ignore.command(name="channel", pass_context=True)
    async def ignore_channel(self, ctx, channel: discord.Channel=None):
        """Ignores channel

        Defaults to current one"""
        current_ch = ctx.message.channel
        if not channel:
            if current_ch.id not in self.ignore["CHANNELS"]:
                self.ignore["CHANNELS"].append(current_ch.id)
                dataIO.save_json("data/grammar/ignorelist.json", self.ignore)
                await self.bot.say("Channel added to ignore list.")
            else:
                await self.bot.say("Channel already in ignore list.")
        else:
            if channel.id not in self.ignore["CHANNELS"]:
                self.ignore["CHANNELS"].append(channel.id)
                dataIO.save_json("data/grammar/ignorelist.json", self.ignore)
                await self.bot.say("Channel added to ignore list.")
            else:
                await self.bot.say("Channel already in ignore list.")

    @grammar_ignore.command(name="server", pass_context=True)
    async def ignore_server(self, ctx):
        """Ignores current server"""
        server = ctx.message.server
        if server.id not in self.ignore["SERVERS"]:
            self.ignore["SERVERS"].append(server.id)
            dataIO.save_json("data/grammar/ignorelist.json", self.ignore)
            await self.bot.say("This server has been added to the ignore list.")
        else:
            await self.bot.say("This server is already being ignored.")

    @commands.group(name="grammarunignore", aliases=["gunignore"], pass_context=True, no_pm=True)
    @checks.admin_or_permissions(administrator=True)
    async def grammar_unignore(self, ctx):
        """Removes servers/channels from ignorelist"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)
            await self.bot.say(self.count_ignored())

    @grammar_unignore.command(name="grammar")
    async def unignore_grammar(self, trigger: str):
        """Unignore certain grammar triggers"""
        if trigger in self.ignore['GRAMMAR']:
            self.ignore['GRAMMAR'].remove(trigger)
            dataIO.save_json("data/grammar/ignorelist.json", self.ignore)
            await self.bot.say('"' + trigger + '" has been removed from the ignore list.')
        else:
            await self.bot.say('"' + trigger + '" is not in the ignore list.')

    @grammar_unignore.command(name="channel", pass_context=True)
    async def unignore_channel(self, ctx, channel: discord.Channel=None):
        """Removes channel from ignore list

        Defaults to current one"""
        current_ch = ctx.message.channel
        if not channel:
            if current_ch.id in self.ignore["CHANNELS"]:
                self.ignore["CHANNELS"].remove(current_ch.id)
                dataIO.save_json("data/grammar/ignorelist.json", self.ignore)
                await self.bot.say("This channel has been removed from the ignore list.")
            else:
                await self.bot.say("This channel is not in the ignore list.")
        else:
            if channel.id in self.ignore["CHANNELS"]:
                self.ignore["CHANNELS"].remove(channel.id)
                dataIO.save_json("data/grammar/ignorelist.json", self.ignore)
                await self.bot.say("Channel removed from ignore list.")
            else:
                await self.bot.say("That channel is not in the ignore list.")

    @grammar_unignore.command(name="server", pass_context=True)
    async def unignore_server(self, ctx):
        """Removes current server from ignore list"""
        server = ctx.message.server
        if server.id in self.ignore["SERVERS"]:
            self.ignore["SERVERS"].remove(server.id)
            dataIO.save_json("data/grammar/ignorelist.json", self.ignore)
            await self.bot.say("This server has been removed from the ignore list.")
        else:
            await self.bot.say("This server is not in the ignore list.")

    def count_ignored(self):
        msg = "```Currently ignoring:\n"
        msg += str(len(self.ignore["CHANNELS"])) + " channels\n"
        msg += str(len(self.ignore["SERVERS"])) + " servers\n```\n"
        return msg

    @_grammar.command(name="list")
    async def _list(self):
        """Pull up grammar being ignored"""
        if self.ignore['GRAMMAR']:
            await self.bot.say(str(self.ignore['GRAMMAR']).strip('[]') + '\nare all being ignored.')
        else:
            await self.bot.say("There's nothing in the ignore list.")

    @_grammar.command()
    async def caret(self, on_off: bool):
        """Toggle ^ caret deletion"""
        if on_off is True:
            await self.bot.say('Deleting carets is now ON.')
            self.toggle = True
        else:
            await self.bot.say('Deleting carets is now OFF.')
            self.toggle = False

    async def on_message(self, message):
        m = message
        for x in self.bot.settings.get_prefixes(m.server):
            if m.author.bot is True or m.content.startswith(x) \
                    or m.server.id in self.ignore["SERVERS"] or m.channel.id in self.ignore["CHANNELS"]:
                return
            for k, v in self.grammar.items():
                if re.findall(r'\b' + k + r'\b', m.content.lower()):
                    if k not in self.ignore['GRAMMAR']:
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
    g = "data/grammar/ignorelist.json"
    if not dataIO.is_valid_json(f):
        print("No such thing as grammar.json...")
    if not dataIO.is_valid_json(g):
        print("No such thing as ignorelist.json...")


def setup(bot):
    n = Grammar(bot)
    bot.add_cog(n)
