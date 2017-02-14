# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from cogs.utils import checks
from random import randint
from random import choice

__author__ = "ScarletRav3n"

b = False
nsword = nlove = nsquat = npizza = nbribe = ndad = ncalc = nbutt = ncom = nflirt = nup = 0


class Fun:
    """fun random commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.admin_or_permissions(administrator=True)
    async def fun(self, on_off: str):
        """Toggle counting for fun-based commands"""
        f = on_off.lower()
        global b
        if f == "on":
            await self.bot.say("Counting counter is now ON." +
                               "\n`Make sure I have the 'manage_messages' " +
                               "permission`")
            b = True
        elif f == "off":
            await self.bot.say("Counting counter is now OFF.")
            b = False
        else:
            await self.bot.say("I need an ON or OFF state.")

    @commands.command(pass_context=True)
    async def sword(self, ctx, *, user: discord.Member):
        """Sword Duel!"""
        global nsword
        author = ctx.message.author
        nsword += 1
        if b is True:
            k = "\n*This command has been used " + str(nsword) + " times.*"
        else:
            k = ""
        if user.id == self.bot.user.id:
            await self.bot.say("I'm not the fighting kind" + k)
        else:
            await self.bot.say(author.mention + " and " + user.mention + " dueled for " + str(randint(2, 120)) +
                               " gruesome hours! It was a long, heated battle, but " +
                               choice([author.mention, user.mention]) + " came out victorious!" + k)

    @commands.command(pass_context=True)
    async def love(self, ctx, user: discord.Member):
        """Found your one true love?"""
        global nlove
        author = ctx.message.author
        nlove += 1
        if b is True:
            k = "\n*This command has been used " + str(nlove) + " times.*"
        else:
            k = ""
        if user.id == self.bot.user.id:
            await self.bot.say("I am not capable of loving like you can. I'm sorry." + k)
        else:
            await self.bot.say(author.mention + " is capable of loving " + user.mention + " a whopping " +
                               str(randint(0, 100)) + "%!" + k)

    @commands.command(pass_context=True)
    async def squat(self, ctx):
        """How is your workout going?"""
        global nsquat
        author = ctx.message.author
        nsquat += 1
        if b is True:
            k = "\n*This command has been used " + str(nsquat) + " times.*"
        else:
            k = ""
        await self.bot.say(author.mention + " puts on their game face and does " + str(randint(2, 1000)) +
                           " squats in " + str(randint(4, 90)) + " minutes. Wurk it!" + k)

    @commands.command(pass_context=True)
    async def pizza(self, ctx):
        """How many slices of pizza have you eaten today?"""
        global npizza
        author = ctx.message.author
        npizza += 1
        if b is True:
            k = "\n*This command has been used " + str(npizza) + " times.*"
        else:
            k = ""
        await self.bot.say(author.mention + " has eaten " + str(randint(2, 120)) + " slices of pizza today." + k)

    @commands.command(pass_context=True)
    async def bribe(self, ctx):
        """Find out who is paying under the table"""
        global nbribe
        author = ctx.message.author
        nbribe += 1
        if b is True:
            k = "\n*This command has been used " + str(nbribe) + " times.*"
        else:
            k = ""
        await self.bot.say(author.mention + " has bribed " + self.bot.user.mention + " with " +
                           str(randint(10, 10000)) + " dollars!" + k)

    @commands.command(pass_context=True)
    async def daddy(self, ctx):
        global ndad
        author = ctx.message.author
        ndad += 1
        if b is True:
            k = "\n*This command has been used " + str(ndad) + " times.*"
        else:
            k = ""
        await self.bot.say("I'm kink shaming you, " + author.mention + k)

    @commands.command()
    async def calculated(self):
        global ndad
        ndad += ndad
        if b is True:
            k = "\n*This command has been used " + str(ndad) + " times.*"
        else:
            k = ""
        await self.bot.say("That was " + str(randint(0, 100)) + "% calculated!" + k)

    @commands.command()
    async def butts(self):
        global nbutt
        nbutt += 1
        if b is True:
            k = "\n*This command has been used " + str(nbutt) + " times.*"
        else:
            k = ""
        await self.bot.say("ლ(́◉◞౪◟◉‵ლ)" + k)

    @commands.command(name="commands")
    async def _commands(self):
        global ncom
        ncom += 1
        if b is True:
            k = "\n*This command has been used " + str(ncom) + " times.*"
        else:
            k = ""
        await self.bot.say("Don't tell me what to do." + k)

    @commands.command()
    async def flirt(self):
        global nflirt
        nflirt += 1
        if b is True:
            k = "\n*This command has been used " + str(nflirt) + " times.*"
        else:
            k = ""
        await self.bot.say("xoxoxoxoxo ;)) ))) hey b a b e ; ; ;))) ) ;)" + k)

    @commands.command()
    async def updog(self):
        global nup
        nup += 1
        if b is True:
            k = "\n*This command has been used " + str(nup) + " times.*"
        else:
            k = ""
        await self.bot.say("What's updog?" + k)


def setup(bot):
    n = Fun(bot)
    bot.add_cog(n)
