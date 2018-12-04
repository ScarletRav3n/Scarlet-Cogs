import discord
from redbot.core import commands, checks
from random import randint, choice

__author__ = "ScarletRaven"


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
        random = randint(2,120)
        if user.id == ctx.bot.user.id:
            await ctx.send("I'm not the fighting kind")
        else:
            await ctx.send(f"{ctx.author.mention} and {user.mention} dueled for {random} hours! \
                           \nIt was a long heated battle, but {choice([ctx.author.mention, user.mention])} came out victorious!")
        await self.counter(ctx, count = self.nsword)

    @commands.command()
    async def love(self, ctx, user: discord.Member):
        """Found your one true love?"""
        self.nlove += 1
        random = randint(0, 100)
        if user.id == ctx.bot.user.id:
            await ctx.send("I am not capable of loving like you can. I'm sorry.")
        else:
            await ctx.send(f"{ctx.author.mention} is capable of loving {user.mention} a whopping {random}%!")
        await self.counter(ctx, count = self.nlove)

    @commands.command()
    async def squat(self, ctx):
        """How is your workout going?"""
        self.nsquat += 1
        random = randint(2, 1000)
        random1 = randint(4, 90)
        await ctx.send(f"{ctx.author.mention} puts on their game face and does {random} squats in {random1} minutes. Wurt it!")
        await self.counter(ctx, count = self.nsquat)

    @commands.command()
    async def pizza(self, ctx):
        """How many slices of pizza have you eaten today?"""
        self.npizza += 1
        random = randint(2, 120)
        await ctx.send(f"{ctx.author.mention} has eaten {random} slices of pizza today.")
        await self.counter(ctx, count = self.npizza)

    @commands.command()
    async def bribe(self, ctx):
        """Find out who is paying under the table"""
        self.nbribe += 1
        random = randint(10, 10000)
        await ctx.send(f"{ctx.author.mention} has bribed {ctx.user.user.mention} with {random} dollars!")
        await self.counter(ctx, count = self.nbribe)

    @commands.command()
    async def daddy(self, ctx):
        """Pass the salt"""
        self.ndad += 1
        await ctx.send(f"I'm kink shaming you, {ctx.author.mention}")
        await self.counter(ctx, count = self.ndad)
    
    @commands.command()
    async def calculated(self, ctx):
        """That was 100% calculated!"""
        self.ncalc += 1
        random = randint(0, 100)
        await ctx.send(f"That was {random}% calculated!")
        await self.counter(ctx, count = self.ncalc)

    @commands.command()
    async def butts(self, ctx):
        """Butts"""
        self.nbutt += 1
        await ctx.send("ლ(́◉◞౪◟◉‵ლ)")
        await self.counter(ctx, count = self.nbutt)
    
    @commands.command(name="commands")
    async def _commands(self, ctx):
        """Command the bot"""
        self.ncom += 1
        await ctx.send("Don't tell me what to do.")
        await self.counter(ctx, count = self.ncom)

    @commands.command()
    async def flirt(self, ctx):
        """Slide into DMs"""
        self.nflirt += 1
        await ctx.send("xoxoxoxoxo ;)) ))) hey b a b e ; ; ;))) ) ;)")
        await self.counter(ctx, count = self.nflirt)
    
    @commands.command()
    async def updog(self, ctx):
        """This is updog"""
        self.nup += 1
        await ctx.send("What's updog?")
        await self.counter(ctx, count = self.nup)

    async def counter(self, ctx, count):
        if self.toggle:
            await ctx.send(f"*This command has been used {count} times.*")