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
    async def overwatch(self, ctx, username, xbox_ps4: str = None):
        """Overwatch Stats

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
                await self.bot.say("Trouble reading the platform type. \n<pc/xbox/ps4> or missing quotes around name")
                return
            d = await self.bot.send_message(m.channel, "Fetching player data for " + username + "...")
            await self.bot.send_typing(m.channel)
            async with s.get(url + u + "/stats?platform=" + p) as re:
                rr = await re.json()
                try:
                    if rr['msg'] == "profile not found":
                        await self.bot.say(username + " not found. \n Remember it's cap-sensitive")
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
                        cpp = ""
                    else:
                        cp = "Wins - " + str(e['overall_stats']['wins']) \
                             + "\nAvg Elims - " + str(e['average_stats']['eliminations_avg']) \
                             + "\nAvg Healing - " + str(e['average_stats']['healing_done_avg']) \
                             + "\nAvg Deaths - " + str(e['average_stats']['deaths_avg'])
                        cpp = "\nSR - " + str(q['comprank']) \
                              + "\nRank - " + str(q['tier']).capitalize()
                    if str(q['prestige']) == "0":
                        prr = ""
                    else:
                        prr = str(q['prestige'])
                    await self.bot.delete_message(d)
                    em = discord.Embed(title="Overwatch Stats on " + p.upper(),
                                       colour=discord.Colour(0x392b5),
                                       description="Level " + prr + str(q["level"])
                                                   + cpp)
                    em.set_thumbnail(url=str(q["avatar"]))
                    em.set_author(name=username)
                    em.set_footer(text="Stay Positive")
                    em.add_field(name="Quick Play",
                                 value="Wins - " + str(q['wins'])
                                       + "\nAvg Elims - " + str(w['eliminations_avg'])
                                       + "\nAvg Healing - " + str(w['healing_done_avg'])
                                       + "\nAvg Deaths - " + str(w['deaths_avg']))
                    em.add_field(name="Competitive",
                                 value=cp)
                    await self.bot.send_message(m.channel, embed=em)


def setup(bot):
    n = Overwatch(bot)
    bot.add_cog(n)
