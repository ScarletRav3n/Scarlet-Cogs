"""Package for TitleCase cog"""
from .titlecase import TitleCase

def setup(bot):
    bot.add_cog(TitleCase(bot))