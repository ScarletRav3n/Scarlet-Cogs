# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from random import randint
import aiohttp

__author__ = "ScarletRav3n"


class Overwatch:
    """Statistics for Overwatch"""

    def __init__(self, bot):
        self.bot = bot
        self.header = {"User-Agent": "User_Agent"}
        self.api = None

    @commands.command(aliases=["ow"], pass_context=True)
    async def overwatch(self, ctx, username, xbox_ps4: str = None):
        """Overwatch Stats

        If you have a space in your name use quotations"""
        m = ctx.message
        user = username.replace("#", "-")
        url = "https://api.lootbox.eu/"
        # if "patch" == username.lower():
        #     await self.patch(ctx)
        # else:
        async with aiohttp.ClientSession(headers=self.header) as session:
            if xbox_ps4 is None or xbox_ps4.lower() == "pc":
                platform = "pc"
                region = "us"
            elif xbox_ps4.lower() == "xbox":
                platform = "xbl"
                region = "global"
            elif xbox_ps4.lower() == "ps4":
                platform = "psn"
                region = "global"
            else:
                await self.bot.say("Trouble reading the platform type. \n<pc/xbox/ps4> or missing quotes around name")
                return
            fetch = await self.bot.send_message(m.channel, "Fetching player data for " + username + "..."
                                                + "\n*(This may take awhile)*")
            async with session.get(url + platform + "/" + region + "/" + user + "/profile") as us:
                self.api = await us.json()
                if 'data' in self.api:
                    await self.bot.delete_message(fetch)
                    await self.stats(ctx, username, platform)
                else:
                    region = "eu"
                    async with session.get(url + platform + "/" + region + "/" + user + "/profile") as eu:
                        self.api = await eu.json()
                        if 'data' in self.api:
                            await self.bot.delete_message(fetch)
                            await self.stats(ctx, username, platform)
                        else:
                            region = "kr"
                            async with session.get(url + platform + "/" + region + "/" + user + "/profile") as kr:
                                self.api = await kr.json()
                                if 'data' in self.api:
                                    await self.bot.delete_message(fetch)
                                    await self.stats(ctx, username, platform)
                                else:
                                    if platform == "pc":
                                        reminder = " and remember to add the bnet tag"
                                    else:
                                        reminder = ""
                                    await self.bot.delete_message(fetch)
                                    await self.bot.say(username + " not found. \nUser is cap-sensitive" + reminder)

    async def stats(self, ctx, username, platform):
        m = ctx.message
        data = self.api['data']
        qp = "Wins - " + str(data['games']['quick'].get('wins', [])) \
             + "\nLost - " + str(data['games']['quick'].get('lost', [])) \
             + "\nPlayed - " + str(data['games']['quick'].get('played', []))\
             + "\nPlaytime - " + str(data['playtime'].get('quick', []))
        if data['competitive']['rank'] is None:
            comp = "No data"
        else:
            comp = "Wins - " + str(data['games']['competitive'].get('wins', [])) \
                   + "\nLost - " + str(data['games']['competitive'].get('lost', [])) \
                   + "\nPlayed - " + str(data['games']['competitive'].get('played', [])) \
                   + "\nPlaytime - " + str(data['playtime'].get('competitive', []))
        em = discord.Embed(title="Overwatch Stats on " + platform.upper(),
                           colour=randint(0, 0xFFFFFF),
                           description="Level " + str(data['level']))
        em.set_thumbnail(url=str(data['avatar']))
        em.set_author(name=username)
        em.set_footer(text="Stay Positive")
        em.add_field(name="Quick Play",
                     value=qp)
        em.add_field(name="Competitive",
                     value=comp)
        em.add_field(name="Lucky Number",
                     value=randint(1, 100))
        await self.bot.send_message(m.channel, embed=em)

    # async def patch(self, ctx):
    #     m = ctx.message
    #     url =
    #     async with aiohttp.ClientSession(headers=self.header) as session:
    #         async with session.get(url) as notes:
    #             self.api = await notes.json()
    #             data = self.api['patchNotes'][0]
    #             await self.bot.send_message(m.channel, str(data['detail']))


def setup(bot):
    n = Overwatch(bot)
    bot.add_cog(n)
