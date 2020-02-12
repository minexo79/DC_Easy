import discord
from discord.ext import commands

bot = commands.Bot(commands_prefix="dcb.")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="use dcb.help."))
    print("[DCB] Bot is on!")

bot.run("YOUR TOKEN")