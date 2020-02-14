import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Errors():

    # 錯誤處理器
    async def error_process(self,ctx,error):
        member = ctx.author.name
        errormsg = f"[DCB] {member}:{error}"
        # 印出至console
        print(errormsg)
        # embed
        embed=discord.Embed()
        embed.add_field(name="使用者",value=member,inline=False)
        # 判別錯誤原因
        if isinstance(error, commands.MissingRequiredArgument):
            problem = "缺少重要的參數!"
        elif isinstance(error, commands.CommandNotFound):
            problem = "找不到指令!"
        elif isinstance(error, commands.MissingPermissions):
            problem = "你沒有足夠的權限!"
        elif isinstance(error, commands.NotOwner):
            problem = "你不是主人!"
        else:
            problem = "未知原因!"
        embed.add_field(name="錯誤原因",value=problem,inline=False)
        # 加框: 粗體
        embed.add_field(name="錯誤訊息",value=f"**{error}**",inline=False)
        await ctx.send(embed=embed)