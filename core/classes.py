import discord
from discord.ext import commands

# --------------------
#
# Cog 核心
# --------------------

class Cog_Extension(commands.Cog):
    def __init__(self,bot):
        self.bot = bot