import discord
from redbot.core import commands, checks
from random import randint, choice

__author__ = "ScarletRaven"


class Fun(commands.Cog):
    """fun random commands"""

    @commands.command()
    async def sword(self, ctx, *, user: discord.Member):
        """Sword Duel!"""
        random = randint(2,120)
        if user.id == ctx.bot.user.id:
            await ctx.send("I'm not the fighting kind")
        else:
            await ctx.send(f"{ctx.author.mention} and {user.mention} dueled for {random} hours! \
                           \nIt was a long heated battle, but {choice([ctx.author.mention, user.mention])} came out victorious!")

    @commands.command()
    async def love(self, ctx, user: discord.Member):
        """Found your one true love?"""
        random = randint(0, 100)
        if user.id == ctx.bot.user.id:
            await ctx.send("I am not capable of loving like you can. I'm sorry.")
        else:
            await ctx.send(f"{ctx.author.mention} is capable of loving {user.mention} a whopping {random}%!")

    @commands.command()
    async def squat(self, ctx):
        """How is your workout going?"""
        random = randint(2, 1000)
        random1 = randint(4, 90)
        await ctx.send(f"{ctx.author.mention} puts on their game face and does {random} squats in {random1} minutes. Wurt it!")

    @commands.command()
    async def pizza(self, ctx):
        """How many slices of pizza have you eaten today?"""
        random = randint(2, 120)
        await ctx.send(f"{ctx.author.mention} has eaten {random} slices of pizza today.")

    @commands.command()
    async def bribe(self, ctx):
        """Find out who is paying under the table"""
        random = randint(10, 10000)
        await ctx.send(f"{ctx.author.mention} has bribed {ctx.user.user.mention} with {random} dollars!")

    @commands.command()
    async def daddy(self, ctx):
        """Pass the salt"""
        await ctx.send(f"I'm kink shaming you, {ctx.author.mention}")
    
    @commands.command()
    async def calculated(self, ctx):
        """That was 100% calculated!"""
        random = randint(0, 100)
        await ctx.send(f"That was {random}% calculated!")

    @commands.command()
    async def butts(self, ctx):
        """Butts"""
        await ctx.send("ლ(́◉◞౪◟◉‵ლ)")
    
    @commands.command(name="commands")
    async def _commands(self, ctx):
        """Command the bot"""
        await ctx.send("Don't tell me what to do.")

    @commands.command()
    async def flirt(self, ctx):
        """Slide into DMs"""
        await ctx.send("xoxoxoxoxo ;)) ))) hey b a b e ; ; ;))) ) ;)")
    
    @commands.command()
    async def updog(self, ctx):
        """This is updog"""
        self.nup += 1
        await ctx.send("What's updog?")