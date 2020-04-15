import discord
from discord.ext import commands
from core.classes import Cog_Extension,permissioncheck
from core.datahook import yamlhook
from core.errors import error_process

class manage(Cog_Extension):

    @commands.command()
    @permissioncheck()
    async def cpccheck(self,ctx):
        '''檢查自訂權限'''
<<<<<<< HEAD
        await ctx.send("✅恭喜！你已在自訂權限名單內。")
=======
        ydata = yamlhook("config.yaml").load()
        try:
            if ctx.author.id in ydata['bot']['owner']:
                await ctx.send("✅你已在自訂權限名單內，恭喜！")
            else:
                error = "使用者沒有自訂權限(不在自訂權限名單內)。"
                # 因為process是自訂，錯誤訊息需自行撰寫。
                await error_process(ctx,error,process="custom")
                # 自訂錯誤訊息
            
        except TypeError: # 權限名單是空的
            error = "權限名單為空。"
            await error_process(ctx,error,process="custom")      
>>>>>>> 300d7bed38fee0f7b4ad0b053a73254f5d4569f2

    @commands.command()
    @permissioncheck()
    async def cpcadd(self,ctx,member:discord.Member):
        '''增加自訂權限者'''
        ydata = yamlhook("config.yaml").load()
<<<<<<< HEAD
        if ctx.author.id in ydata['bot']['owner']: # 檢查一次，防止有兩個同樣的ID存在
            did = member.id
            yamlhook("config.yaml").owner(did,process="append")
            # 輸出增加成功
            await ctx.send(f"✅自訂權限者`{member.display_name}`已增加！")
        else:
            error = "對方已在自訂權限名單內。"
            await Errors.error_process(self,ctx,error,process="custom")
=======
        did = member.id
        if ctx.author.id in ydata['bot']['owner']: # 檢查一次，使用者是否在權限名單內
            if did not in ydata['bot']['owner']: # 再檢查一次，防止有兩個同樣的ID存在
                yamlhook("config.yaml").owner(did,process="append")
                # 輸出增加成功
                await ctx.send(f"✅自訂權限者`{member.display_name}`已增加！")
            else:
                error = "使用者已在自訂權限名單內。"
                await error_process(ctx,error,process="custom")                
        else:
            error = "使用者沒有自訂權限(不在自訂權限名單內)。"
            await error_process(ctx,error,process="custom")
>>>>>>> 300d7bed38fee0f7b4ad0b053a73254f5d4569f2

    @commands.command()
    @permissioncheck()
    async def cpcre(self,ctx,member:discord.Member):
        '''移除自訂權限者'''
        ydata = yamlhook("config.yaml").load()
        try:
            if ctx.author.id in ydata['bot']['owner']:
                did = member.id
                yamlhook("config.yaml").owner(did,process="remove")
                # 輸出移除成功
                await ctx.send(f"✅自訂權限者`{member.display_name}`已移除！")
<<<<<<< HEAD
        except ValueError:
            error = "找不到對方資料。"
            await Errors.error_process(self,ctx,error,process="custom")         
=======
            else:
                error = "使用者沒有自訂權限(不在自訂權限名單內)。"
                await error_process(ctx,error,process="custom")
        except ValueError: # 找不到ID
            error = "名單內找不到使用者ID，或許已經刪除。"
            await error_process(ctx,error,process="custom")                 
            
>>>>>>> 300d7bed38fee0f7b4ad0b053a73254f5d4569f2

def setup(bot):
    bot.add_cog(manage(bot))
