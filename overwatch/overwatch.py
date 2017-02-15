# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
import aiohttp

__author__ = "ScarletRav3n"

h = {"User-Agent": "my_user_agent/0.1.0"}
url = "https://owapi.net/api/v3/u/"


class Overwatch:
    """Statistics for Overwatch"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ow"])
    async def overwatch(self, username, xbox_ps4: str=None):
        """Overwatch Stats BETA

        If you have a space in your name,
        use quotations"""
        global h
        global url
        u = username.replace("#", "-")

        async with aiohttp.ClientSession(headers=h) as s:
            if xbox_ps4.lower() == "xbox":
                p = "xbl"
            elif xbox_ps4.lower() == "ps4":
                p = "psn"
            else:
                p = "pc"
            print(username + " on " + p)
            async with s.get(url + u + "/stats?platform=" + p) as re:
                r = await re.json()
                qq = r["any"]["stats"]
                q = qq["quickplay"]["overall_stats"]
                if str(q["comprank"]) == "null":
                    cp = "There's no data to display"
                else:
                    cp = "SR: " + str(q["comprank"])
                await self.bot.say("Overwatch stats on " + p + " for " + username
                                   + "\nLevel: " + str(q["prestige"]) + str(q["level"])
                                   + "\n\n**Quick Play**"
                                   + "\nWins: " + str(q["wins"])
                                   + "\n\n**Competitive**"
                                   + "\n" + cp)


def setup(bot):
    n = Overwatch(bot)
    bot.add_cog(n)
