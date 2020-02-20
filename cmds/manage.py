import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core.datahook import yamlhook
from core.errors import Errors

class manage(Cog_Extension):

    @commands.command()
    async def owncheck(self,ctx):
        '''檢查自訂權限'''
        ydata = yamlhook("config.yaml").load()
        try:
            if ctx.author.id in ydata['bot']['owner']:
                await ctx.send("✅你已在自訂權限名單內，恭喜！")
            else:
                error = "使用者沒有自訂權限(不在自訂權限名單內)。"
                # 因為process是自訂，錯誤訊息需自行撰寫。
                await Errors.error_process(self,ctx,error,process="custom")
                # 自訂錯誤訊息
            
        except TypeError: # 權限名單是空的
            error = "權限名單為空。"
            await Errors.error_process(self,ctx,error,process="custom")      

    @commands.command()
    async def ownadd(self,ctx,member:discord.Member):
        '''增加自訂權限者'''
        ydata = yamlhook("config.yaml").load()
        if ctx.author.id in ydata['bot']['owner']:
            if ctx.author.id not in ydata['bot']['owner']: # 再檢查一次，防止有兩個同樣的ID存在
                did = member.id
                yamlhook("config.yaml").owner(did,process="append")
                # 輸出增加成功
                await ctx.send(f"✅自訂權限者`{member.display_name}`已增加！")
            else:
                error = "使用者已在自訂權限名單內。"
                await Errors.error_process(self,ctx,error,process="custom")                
        else:
            error = "使用者沒有自訂權限(不在自訂權限名單內)。"
            await Errors.error_process(self,ctx,error,process="custom")

    @commands.command()
    async def ownre(self,ctx,member:discord.Member):
        '''移除自訂權限者'''
        ydata = yamlhook("config.yaml").load()
        try:
            if ctx.author.id in ydata['bot']['owner']:
                did = member.id
                yamlhook("config.yaml").owner(did,process="remove")
                # 輸出移除成功
                await ctx.send(f"✅自訂權限者`{member.display_name}`已移除！")
            else:
                error = "使用者沒有自訂權限(不在自訂權限名單內)。"
                await Errors.error_process(self,ctx,error,process="custom")
        except ValueError: # 找不到ID
            error = "名單內找不到使用者ID，或許已經刪除。"
            await Errors.error_process(self,ctx,error,process="custom")                  
            

def setup(bot):
    bot.add_cog(manage(bot))
