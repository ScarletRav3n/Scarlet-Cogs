"""Package for CommandSpice cog"""
from redbot.core import data_manager
from .spice import Spice

def setup(bot):
    n = Spice(bot)
    data_manager.load_bundled_data(n, __file__)
    bot.add_cog(n)
    