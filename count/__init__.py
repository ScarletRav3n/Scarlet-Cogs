"""Package for Count cog"""
from .count import Count

def setup(bot):
    bot.add_cog(Count(bot))