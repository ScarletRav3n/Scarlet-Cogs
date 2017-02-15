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

    @commands.command(aliases=["ow"], pass_context=True)
    async def overwatch(self, ctx, username, xbox_ps4: str=None):
        """Overwatch Stats BETA

        If you have a space in your name use quotations"""
        global h, url
        m = ctx.message
        u = username.replace("#", "-")
        async with aiohttp.ClientSession(headers=h) as s:
            if xbox_ps4 is None or xbox_ps4.lower() == "pc":
                p = "pc"
            elif xbox_ps4.lower() == "xbox":
                p = "xbl"
            elif xbox_ps4.lower() == "ps4":
                p = "psn"
            else:
                await self.bot.say("Trouble reading the platform type. \n<pc/xbox/ps4>")
                return
            d = await self.bot.send_message(m.channel, "Fetching player data for " + username + "...")
            async with s.get(url + u + "/stats?platform=" + p) as re:
                rr = await re.json()
                try:
                    if rr['msg'] == "profile not found":
                        await self.bot.say(username + " not found")
                except:
                    if rr['any'] is not None:
                        r = rr['any']
                    elif rr['eu'] is not None:
                        r = rr['eu']
                    elif rr['kr'] is not None:
                        r = rr['kr']
                    elif rr['us'] is not None:
                        r = rr['us']
                    else:
                        await self.bot.say("Trouble getting player info")
                        return
                    ee = r['stats']['quickplay']
                    q = ee['overall_stats']
                    w = ee['average_stats']
                    e = r['stats']['competitive']
                    if q['comprank'] is None:
                        cp = "There's no data to display"
                    else:
                        cp = "Rank: " + str(q['tier']) + "\nSR: " + str(q['comprank']) \
                             + "\nWins: " + str(e['overall_stats']['wins']) \
                             + "\nAvg Elims: " + str(e['average_stats']['eliminations_avg']) \
                             + "\nAvg Healing: " + str(e['average_stats']['healing_done_avg']) \
                             + "\nAvg Deaths: " + str(e['average_stats']['deaths_avg'])
                    await self.bot.edit_message(d, "Overwatch stats on " + p + " for " + username
                                                + "\nLevel: " + str(q['prestige']) + str(q["level"])
                                                + "\n\n**Quick Play**"
                                                + "\nWins: " + str(q['wins'])
                                                + "\nAvg Elims: " + str(w['eliminations_avg'])
                                                + "\nAvg Healing: " + str(w['healing_done_avg'])
                                                + "\nAvg Deaths: " + str(w['deaths_avg'])
                                                + "\n\n**Competitive**"
                                                + "\n" + cp)


def setup(bot):
    n = Overwatch(bot)
    bot.add_cog(n)
