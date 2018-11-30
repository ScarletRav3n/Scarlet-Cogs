import discord
from redbot.core import commands, checks
from random import randint, choice

__author__ = "ScarletRav3n"


class Fun(commands.Cog):
    """fun random commands"""

    def __init__(self):
        self.toggle = False
        self.nsword = self.nlove = self.nsquat = self.npizza = self.nbribe = self.ndad = self.ncalc \
            = self.nbutt = self.ncom = self.nflirt = self.nup = 0

    @commands.command()
    @checks.admin_or_permissions(administrator=True)
    async def fun(self, ctx, on_off: bool):
        """Toggle counting for fun-based commands"""
        if on_off is True:
            await ctx.send('Counting counter is now ON.')
            self.toggle = True
        else:
            await ctx.send('Counting counter is now OFF.')
            self.toggle = False

    @commands.command()
    async def sword(self, ctx, *, user: discord.Member):
        """Sword Duel!"""
        self.nsword += 1
        n = self.nsword
        if user.id == ctx.bot.user.id:
            await ctx.send("I'm not the fighting kind")
        else:
            await ctx.send("{0} and {1} dueled for {2} gruesome hours! It was a long, heated battle, \
                            but {3} came out victorious!".format(ctx.author.mention, user.mention, \
                            str(randint(2,120)), choice([ctx.author.mention, user.mention])))
        await self.counter(ctx, n)

    @commands.command()
    async def love(self, ctx, user: discord.Member):
        """Found your one true love?"""
        self.nlove += 1
        n = self.nlove
        if user.id == ctx.bot.user.id:
            await ctx.send("I am not capable of loving like you can. I'm sorry.")
        else:
            await ctx.send("{0} is capable of loving {1} a whopping {2}%!".format(ctx.author.mention, \
                            user.mention, str(randint(0, 100))))
        await self.counter(ctx, n)

    @commands.command()
    async def squat(self, ctx):
        """How is your workout going?"""
        self.nsquat += 1
        n = self.nsquat
        await ctx.send("{0} puts on their game face and does {1} squats in {2} minutes. Wurt it!".format\
                        (ctx.author.mention, str(randint(2, 1000)), str(randint(4, 90))))
        await self.counter(ctx, n)

    @commands.command()
    async def pizza(self, ctx):
        """How many slices of pizza have you eaten today?"""
        self.npizza += 1
        n = self.npizza
        await ctx.send("{0} has eaten {1} slices of pizza today.".format(ctx.author.mention, randint(2, 120)))
        await self.counter(ctx, n)

    @commands.command()
    async def bribe(self, ctx):
        """Find out who is paying under the table"""
        self.nbribe += 1
        n = self.nbribe
        await ctx.send("{0} has bribed {1} with {2} dollars!".format(ctx.author.mention, ctx.user.user.mention, \
                        str(randint(10, 10000))))
        await self.counter(ctx, n)

    @commands.command()
    async def daddy(self, ctx):
        """Pass the salt"""
        self.ndad += 1
        n = self.ndad
        await ctx.send("I'm kink shaming you, {0}".format(ctx.author.mention))
        await self.counter(ctx, n)
    
    @commands.command()
    async def calculated(self, ctx):
        """That was 100% calculated!"""
        self.ncalc += 1
        n = self.ncalc
        await ctx.send("That was {0}% calculated!".format(str(randint(0, 100))))
        await self.counter(ctx, n)

    @commands.command()
    async def butts(self, ctx):
        """Butts"""
        self.nbutt += 1
        n = self.nbutt
        await ctx.send("ლ(́◉◞౪◟◉‵ლ)")
        await self.counter(ctx, n)
    
    @commands.command(name="commands")
    async def _commands(self, ctx):
        """Command the bot"""
        self.ncom += 1
        n = self.ncom
        await ctx.send("Don't tell me what to do.")
        await self.counter(ctx, n)

    @commands.command()
    async def flirt(self, ctx):
        """Slide into DMs"""
        self.nflirt += 1
        n = self.nflirt
        await ctx.send("xoxoxoxoxo ;)) ))) hey b a b e ; ; ;))) ) ;)")
        await self.counter(ctx, n)
    
    @commands.command()
    async def updog(self):
        """This is updog"""
        self.nup += 1
        n = self.nup
        await self.bot.say("What's updog?")
        await self.counter(ctx, n)

    async def counter(self, ctx, n):
        if self.toggle:
            await ctx.send("*This command has been used {0} times.*".format(n))