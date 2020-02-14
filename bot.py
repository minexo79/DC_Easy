import discord
from discord.ext import commands
from core.datahook import yamlhook
import os

bot = commands.Bot(command_prefix="dcb.")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="dcb.help."))
    print("[DCB] Bot is on!")

# 裝載Cog
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    # console 訊息清除 
    # windows        : os.system("cls")
    # linux or other : os.system("clear")
    os.system("cls")
    # 抓取 bot token
    ydata = yamlhook("config.yaml").open()
    bot.run(ydata['bot']['token'])
