# noinspection PyUnresolvedReferences
import discord
from discord.ext import commands
from cogs.utils import checks

__author__ = "ScarletRav3n"

# TODO: Find a better way to trigger a/an's


class Grammar:
    """Fix those mistakes"""

    def __init__(self, bot):
        self.bot = bot
        self.toggle = False

    @commands.command()
    @checks.admin_or_permissions(administrator=True)
    async def grammar(self, on_off: str):
        """Toggle ^ caret"""
        if on_off.lower() == "on":
            await self.bot.say("Deleting carets is now ON." +
                               "\n`Make sure I have the 'manage_messages' " +
                               "permission`")
            self.toggle = True
        elif on_off.lower() == "off":
            await self.bot.say("Deleting carets is now OFF.")
            self.toggle = False
        else:
            await self.bot.say("I need an ON or OFF state.")

    async def on_message(self, m):
        str_m = m.content.lower()
        for x in self.bot.settings.get_prefixes(m.server):
            if m.author.bot is not True:
                if m.content.startswith(x):
                    return
                # elif " a a" in str_m: # a/an
                #    fix = "an*"
                # elif " a e" in str_m:
                #    fix = "an*"
                # elif " a o" in str_m:
                #    fix = "an*"
                # elif " a u" in str_m:
                #    fix = "an*"
                # elif " a i" in str_m:
                #    fix = "an*"
                elif "your a " in str_m:  # your/there
                    fix = "you're*"
                elif "your an " in str_m:
                    fix = "you're*"
                elif "your on " in str_m:
                    fix = "you're*"
                elif "their not" in str_m:
                    fix = "they're*"
                elif "their a " in str_m:
                    fix = "they're*"
                elif "their an " in str_m:
                    fix = "they're*"
                elif "theres a " in str_m:
                    fix = "there's*"
                elif "theres an " in str_m:
                    fix = "there's*"
                elif "dont " in str_m:  # apostrophes
                    fix = "don't*"
                elif "didnt " in str_m:
                    fix = "didn't*"
                elif "cant " in str_m:
                    fix = "can't*"
                elif "wont " in str_m:
                    fix = "won't*"
                elif "isnt " in str_m:
                    fix = "isn't*"
                elif "its not" in str_m:
                    fix = "it's*"
                elif "laif" in str_m:  # stupid broken english patch start here
                    fix = "life*"
                elif "stronk" in str_m:
                    fix = "strong*"
                elif "noice" in str_m:
                    fix = "nice*"
                elif "lood" in str_m:
                    fix = "lewd*"
                elif "taht" in str_m:
                    fix = "that*"
                elif "nawt" in str_m:
                    fix = "not*"
                elif "lern" in str_m:
                    fix = "learn*"
                elif "spel" in str_m:
                    fix = "spell*"
                elif "tommorrow" in str_m:  # other english words
                    fix = "tomorrow*"
                elif "tomorow" in str_m:
                    fix = "tomorrow*"
                elif "begining" in str_m:
                    fix = "beginning*"
                elif "litteral" in str_m:
                    fix = "literal*"
                elif "rediculous" in str_m:
                    fix = "ridiculous*"
                elif "defiantly" in str_m:
                    fix = "definitely*"
                elif "definately" in str_m:
                    fix = "definitely*"
                elif "definitly" in str_m:
                    fix = "definitely*"
                elif "multible" in str_m:
                    fix = "multiple*"
                elif "becuase" in str_m:
                    fix = "because*"
                elif "^" in m.content:  # caret
                    if self.toggle is True:
                        try:
                            await self.bot.delete_message(m)
                        except discord.errors.Forbidden:
                            await self.bot.say("Wanted to delete mid {} but no permissions".format(m.id))
                    return
                else:
                    return
                await self.bot.send_message(m.channel, fix)


def setup(bot):
    n = Grammar(bot)
    bot.add_cog(n)
