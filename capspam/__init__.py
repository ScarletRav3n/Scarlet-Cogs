"""Package for CapSpam cog"""
from .capspam import CapSpam

def setup(bot):
    bot.add_cog(CapSpam(bot))