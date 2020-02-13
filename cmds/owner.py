import discord
from discord.ext import commands
from core.classes import Cog_extension

class manage(Cog_extension):

    @commands.command() #重新裝載Cog
    @commands.is_owner() 
    async def re(self, ctx, extension:str):
        '''Cog重新裝載'''
        self.bot.reload_extension(f"cmds.{extension}")
        print(f"[DCB] [{extension}] has reloaded.")
        await ctx.send(f"`{extension} 已重新載入。`")


    @commands.command() #關閉機器人
    @commands.is_owner()     
    async def bye(self,ctx):
        '''關閉機器人'''
        await ctx.send("`已關閉機器人。`")
        await self.bot.close()

def setup(bot):
    bot.add_cog(manage(bot))