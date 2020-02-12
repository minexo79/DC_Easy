import discord
from discord.ext import commands

bot = commands.Bot(commands_prefix="dcb.")

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="use dcb.help."))
    print("[DCB] Bot is on!")
    
@commands.command() #截取對方的頭貼
async def avatar(ctx, id: int):
    user = await client.fetch_user(id)
    avatar_url = user.avatar_url
    embed=discord.Embed(color=0xff66fd)
    embed.set_image(url=avatar_url)
    await ctx.send(embed=embed)

bot.run("YOUR TOKEN")
