import discord
from discord.ext import commands
from core.classes import Cog_Extension

class owner(Cog_Extension):

    @commands.command()
    @commands.is_owner() 
    async def reload(self, ctx, extension:str):
        '''Cog重新裝載'''
        self.bot.reload_extension(f"cmds.{extension}")
        print(f"[DCB] [{extension}] has reloaded.")
        await ctx.send(f"`{extension} 已重新載入。`")

    @commands.command()
    @commands.is_owner() 
    async def load(self, ctx, extension:str):
        '''Cog裝入'''
        self.bot.load_extension(f"cmds.{extension}")
        print(f"[DCB] [{extension}] has loaded.")
        await ctx.send(f"`{extension} 已載入。`")

    @commands.command()
    @commands.is_owner() 
    async def unload(self, ctx, extension:str):
        '''Cog移除'''
        self.bot.unload_extension(f"cmds.{extension}")
        print(f"[DCB] [{extension}] has unloaded.")
        await ctx.send(f"`{extension} 已移除。`")

    @commands.command() 
    async def bye(self,ctx):
        '''關閉機器人'''
        await ctx.send("`機器人已關閉。`")
        await self.bot.close()

def setup(bot):
    bot.add_cog(owner(bot))