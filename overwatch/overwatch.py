# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
import aiohttp

__author__ = "ScarletRav3n"


class Overwatch:
    """Statistics for Overwatch (Beta Cog)"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ow"], pass_context=True)
    async def overwatch(self, ctx, username, xbox_ps4: str = None):
        """Overwatch Stats (Beta Cog)

        If you have a space in your name use quotations"""
        m = ctx.message
        user = username.replace("#", "-")
        header = {"User-Agent": "my_user_agent/0.1.0"}
        url = "https://owapi.net/api/v3/u/"
        async with aiohttp.ClientSession(headers=header) as session:
            if xbox_ps4 is None or xbox_ps4.lower() == "pc":
                platform = "pc"
            elif xbox_ps4.lower() == "xbox":
                platform = "xbl"
            elif xbox_ps4.lower() == "ps4":
                platform = "psn"
            else:
                await self.bot.say("Trouble reading the platform type. \n<pc/xbox/ps4> or missing quotes around name")
                return
            fetch = await self.bot.send_message(m.channel, "Fetching player data for " + username + "...")
            await self.bot.send_typing(m.channel)
            async with session.get(url + user + "/stats?platform=" + platform) as re:
                try:
                    if await re.json()['msg'] == "profile not found":
                        await self.bot.say(username + " not found. \n Remember it's cap-sensitive")
                except:
                    if await re.json()['any'] is not None:
                        region = await re.json()['any']
                    elif await re.json()['eu'] is not None:
                        region = await re.json()['eu']
                    elif await re.json()['kr'] is not None:
                        region = await re.json()['kr']
                    elif await re.json()['us'] is not None:
                        region = await re.json()['us']
                    else:
                        await self.bot.say("Trouble getting player info")
                        return
                    quickplay = region['stats']['quickplay']
                    overall = quickplay['overall_stats']
                    avg = quickplay['average_stats']
                    comp = region['stats']['competitive']
                    if overall['comprank'] is None:
                        cp = "There's no data to display"
                        comprank = ""
                    else:
                        cp = "Wins - " + str(comp['overall_stats']['wins']) \
                             + "\nAvg Elims - " + str(comp['average_stats']['eliminations_avg']) \
                             + "\nAvg Healing - " + str(comp['average_stats']['healing_done_avg']) \
                             + "\nAvg Deaths - " + str(comp['average_stats']['deaths_avg'])
                        comprank = "\nSR - " + str(overall['comprank']) \
                              + "\nRank - " + str(overall['tier']).capitalize()
                    if str(overall['prestige']) == "0":
                        prestige = ""
                    else:
                        prestige = str(overall['prestige'])
                    await self.bot.delete_message(fetch)
                    em = discord.Embed(title="Overwatch Stats on " + platform.upper(),
                                       colour=discord.Colour(0x392b5),
                                       description="Level " + prestige + str(overall["level"])
                                                   + comprank)
                    em.set_thumbnail(url=str(overall["avatar"]))
                    em.set_author(name=username)
                    em.set_footer(text="Stay Positive")
                    em.add_field(name="Quick Play",
                                 value="Wins - " + str(overall['wins'])
                                       + "\nAvg Elims - " + str(avg['eliminations_avg'])
                                       + "\nAvg Healing - " + str(avg['healing_done_avg'])
                                       + "\nAvg Deaths - " + str(avg['deaths_avg']))
                    em.add_field(name="Competitive",
                                 value=cp)
                    await self.bot.send_message(m.channel, embed=em)


def setup(bot):
    n = Overwatch(bot)
    bot.add_cog(n)
