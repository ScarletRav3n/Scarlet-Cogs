# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from cogs.utils import checks
from random import randint
from random import choice

__author__ = "ScarletRav3n"


class Fun:
    """fun random commands"""

    def __init__(self, bot):
        self.bot = bot
        self.toggle = False
        self.nsword = self.nlove = self.nsquat = self.npizza = self.nbribe = self.ndad = self.ncalc \
            = self.nbutt = self.ncom = self.nflirt = self.nup = 0

    @commands.command()
    @checks.admin_or_permissions(administrator=True)
    async def fun(self, on_off: str):
        """Toggle counting for fun-based commands"""
        if on_off.lower() == "on":
            await self.bot.say("Counting counter is now ON.")
            self.toggle = True
        elif on_off.lower() == "off":
            await self.bot.say("Counting counter is now OFF.")
            self.toggle = False
        else:
            await self.bot.say("I need an ON or OFF state.")

    @commands.command(pass_context=True)
    async def sword(self, ctx, *, user: discord.Member):
        """Sword Duel!"""
        author = ctx.message.author
        self.nsword += 1
        if self.toggle is True:
            count = "\n*This command has been used " + str(self.nsword) + " times.*"
        else:
            count = ""
        if user.id == self.bot.user.id:
            await self.bot.say("I'm not the fighting kind" + count)
        else:
            await self.bot.say(author.mention + " and " + user.mention + " dueled for " + str(randint(2, 120)) +
                               " gruesome hours! It was a long, heated battle, but " +
                               choice([author.mention, user.mention]) + " came out victorious!" + count)

    @commands.command(pass_context=True)
    async def love(self, ctx, user: discord.Member):
        """Found your one true love?"""
        author = ctx.message.author
        self.nlove += 1
        if self.toggle is True:
            count = "\n*This command has been used " + str(self.nlove) + " times.*"
        else:
            count = ""
        if user.id == self.bot.user.id:
            await self.bot.say("I am not capable of loving like you can. I'm sorry." + count)
        else:
            await self.bot.say(author.mention + " is capable of loving " + user.mention + " a whopping " +
                               str(randint(0, 100)) + "%!" + count)

    @commands.command(pass_context=True)
    async def squat(self, ctx):
        """How is your workout going?"""
        author = ctx.message.author
        self.nsquat += 1
        if self.toggle is True:
            count = "\n*This command has been used " + str(self.nsquat) + " times.*"
        else:
            count = ""
        await self.bot.say(author.mention + " puts on their game face and does " + str(randint(2, 1000)) +
                           " squats in " + str(randint(4, 90)) + " minutes. Wurk it!" + count)

    @commands.command(pass_context=True)
    async def pizza(self, ctx):
        """How many slices of pizza have you eaten today?"""
        author = ctx.message.author
        self.npizza += 1
        if self.toggle is True:
            count = "\n*This command has been used " + str(self.npizza) + " times.*"
        else:
            count = ""
        await self.bot.say(author.mention + " has eaten " + str(randint(2, 120)) + " slices of pizza today." + count)

    @commands.command(pass_context=True)
    async def bribe(self, ctx):
        """Find out who is paying under the table"""
        author = ctx.message.author
        self.nbribe += 1
        if self.toggle is True:
            count = "\n*This command has been used " + str(self.nbribe) + " times.*"
        else:
            count = ""
        await self.bot.say(author.mention + " has bribed " + self.bot.user.mention + " with " +
                           str(randint(10, 10000)) + " dollars!" + count)

    @commands.command(pass_context=True)
    async def daddy(self, ctx):
        author = ctx.message.author
        self.ndad += 1
        if self.toggle is True:
            count = "\n*This command has been used " + str(self.ndad) + " times.*"
        else:
            count = ""
        await self.bot.say("I'm kink shaming you, " + author.mention + count)

    @commands.command()
    async def calculated(self):
        self.ndad += ndad
        if self.toggle is True:
            count = "\n*This command has been used " + str(self.ndad) + " times.*"
        else:
            count = ""
        await self.bot.say("That was " + str(randint(0, 100)) + "% calculated!" + count)

    @commands.command()
    async def butts(self):
        self.nbutt += 1
        if self.toggle is True:
            count = "\n*This command has been used " + str(self.nbutt) + " times.*"
        else:
            count = ""
        await self.bot.say("ლ(́◉◞౪◟◉‵ლ)" + count)

    @commands.command(name="commands")
    async def _commands(self):
        self.ncom += 1
        if self.toggle is True:
            count = "\n*This command has been used " + str(self.ncom) + " times.*"
        else:
            count = ""
        await self.bot.say("Don't tell me what to do." + count)

    @commands.command()
    async def flirt(self):
        self.nflirt += 1
        if self.toggle is True:
            count = "\n*This command has been used " + str(self.nflirt) + " times.*"
        else:
            count = ""
        await self.bot.say("xoxoxoxoxo ;)) ))) hey b a b e ; ; ;))) ) ;)" + count)

    @commands.command()
    async def updog(self):
        self.nup += 1
        if self.toggle is True:
            count = "\n*This command has been used " + str(self.nup) + " times.*"
        else:
            count = ""
        await self.bot.say("What's updog?" + count)


def setup(bot):
    n = Fun(bot)
    bot.add_cog(n)
