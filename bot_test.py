import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="dcb.")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="use dcb.help."))
    print("[DCB] Bot is on!")
    
@bot.command() #截取對方的頭貼
async def avatar(ctx, id: int):
    user = await bot.fetch_user(id)
    avatar_url = user.avatar_url
    embed=discord.Embed(color=0xff66fd)
    embed.set_image(url=avatar_url)
    await ctx.send(embed=embed)

bot.run("NjcwODExNTg5Njk1MjQyMjQw.XkTgiA.vUKt6EvK60GEFydivfLYpdplmAo")
