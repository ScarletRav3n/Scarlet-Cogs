# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from cogs.utils import checks
from .utils.dataIO import dataIO
import os
import re

__author__ = "ScarletRav3n"


class TitleCase:
    """Stop people from writing in CamelCase"""

    def __init__(self, bot):
        self.bot = bot
        self.ignore = dataIO.load_json("data/titlecase/ignorelist.json")

    def save_ignore(self):
        dataIO.save_json(self.ignore)
        dataIO.is_valid_json("data/titlecase/ignorelist.json")

    @commands.group(pass_context=True)
    @checks.admin_or_permissions(administrator=True)
    async def titlecase(self, ctx):
        """TitleCase settings"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    @titlecase.group(pass_context=True, no_pm=True)
    async def ignore(self, ctx):
        """Adds servers/channels to ignorelist"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)
            await self.bot.say(self.count_ignored())

    @ignore.command(name="channel", pass_context=True)
    async def ignore_channel(self, ctx, channel: discord.Channel=None):
        """Ignores channel

        Defaults to current one"""
        current_ch = ctx.message.channel
        if not channel:
            if current_ch.id not in self.ignore["CHANNELS"]:
                self.ignore["CHANNELS"].append(current_ch.id)
                dataIO.save_json("data/titlecase/ignorelist.json", self.ignore)
                await self.bot.say("Channel added to ignore list.")
            else:
                await self.bot.say("Channel already in ignore list.")
        else:
            if channel.id not in self.ignore["CHANNELS"]:
                self.ignore["CHANNELS"].append(channel.id)
                dataIO.save_json("data/titlecase/ignorelist.json", self.ignore)
                await self.bot.say("Channel added to ignore list.")
            else:
                await self.bot.say("Channel already in ignore list.")

    @ignore.command(name="server", pass_context=True)
    async def ignore_server(self, ctx):
        """Ignores current server"""
        server = ctx.message.server
        if server.id not in self.ignore["SERVERS"]:
            self.ignore["SERVERS"].append(server.id)
            dataIO.save_json("data/titlecase/ignorelist.json", self.ignore)
            await self.bot.say("This server has been added to the ignore list.")
        else:
            await self.bot.say("This server is already being ignored.")

    @titlecase.group(pass_context=True, no_pm=True)
    async def unignore(self, ctx):
        """Removes servers/channels from ignorelist"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)
            await self.bot.say(self.count_ignored())

    @unignore.command(name="channel", pass_context=True)
    async def unignore_channel(self, ctx, channel: discord.Channel=None):
        """Removes channel from ignore list

        Defaults to current one"""
        current_ch = ctx.message.channel
        if not channel:
            if current_ch.id in self.ignore["CHANNELS"]:
                self.ignore["CHANNELS"].remove(current_ch.id)
                dataIO.save_json("data/titlecase/ignorelist.json", self.ignore)
                await self.bot.say("This channel has been removed from the ignore list.")
            else:
                await self.bot.say("This channel is not in the ignore list.")
        else:
            if channel.id in self.ignore["CHANNELS"]:
                self.ignore["CHANNELS"].remove(channel.id)
                dataIO.save_json("data/titlecase/ignorelist.json", self.ignore)
                await self.bot.say("Channel removed from ignore list.")
            else:
                await self.bot.say("That channel is not in the ignore list.")

    @unignore.command(name="server", pass_context=True)
    async def unignore_server(self, ctx):
        """Removes current server from ignore list"""
        server = ctx.message.server
        if server.id in self.ignore["SERVERS"]:
            self.ignore["SERVERS"].remove(server.id)
            dataIO.save_json("data/titlecase/ignorelist.json", self.ignore)
            await self.bot.say("This server has been removed from the ignore list.")
        else:
            await self.bot.say("This server is not in the ignore list.")

    def count_ignored(self):
        msg = "```Currently ignoring:\n"
        msg += str(len(self.ignore["CHANNELS"])) + " channels\n"
        msg += str(len(self.ignore["SERVERS"])) + " servers\n```\n"
        return msg

    async def on_message(self, m):
        pattern = re.compile(r'''(?x)(\b
            [A-Z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)[ ]
            [A-Z][a-z](\S*?)
            \b)''')

        def c(s): return [u[0] for u in re.findall(pattern, s)]
        trigger = str(c(m.content))
        for x in self.bot.settings.get_prefixes(m.server):
            if m.content.startswith(x) or m.content.startswith('"') or m.content.startswith('\\'):
                return
            if m.author.bot is False and trigger != "[]":
                trigger = str(m.author.name) + ' wrote *"' + trigger[2:-2] + '..."*'
                await self.bot.send_message(m.channel, trigger + "\nPlease refrain from using titlecase")
                try:
                    await self.bot.delete_message(m)
                except discord.errors.Forbidden:
                    await self.bot.send_message(m.channel, "(Wanted to delete mid {} but no permissions)".format(m.id))


def check_folders():
    if not os.path.exists("data/titlecase"):
        print("Creating data/titlecase folder...")
        os.makedirs("data/titlecase")


def check_files():
    f = "data/titlecase/ignorelist.json"
    if not dataIO.is_valid_json(f):
        print("No such thing as ignorelist.json...")


def setup(bot):
    n = TitleCase(bot)
    bot.add_cog(n)
