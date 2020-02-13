import discord
from discord.ext import commands
from core.classes import Cog_extension

class manage(Cog_extension):

    @commands.command() #截取對方資訊
    @commands.has_permissions(administrator=True)
    async def avatar(self, ctx, member: discord.Member):
        '''查詢對方資訊'''
        roles = [role for role in member.roles] # 計算身分組 
        embed=discord.Embed(color=member.color)
        embed.set_thumbnail(url=member.avatar_url) # 用戶的頭貼
        embed.add_field(name="對方名稱",value=member,inline=True) # 顯示名稱
        embed.add_field(name="對方暱稱",value=member.display_name,inline=True) # 顯示在此群的名稱
        embed.add_field(name="創建日期",value=member.created_at.strftime("%Y.%m.%d-%H:%M:%S (UTC)"),inline=False) # 顯示創建日期
        embed.add_field(name="加入日期",value=member.joined_at.strftime("%Y.%m.%d-%H:%M:%S (UTC)"),inline=False) # 顯示加入日期 
        if member.is_on_mobile() == True:
            # 如手機在線
            embed.add_field(name="對方狀態",value="Moblie Online",inline=True) # 顯示對方狀態
        else:
            # 不是手機在線
            embed.add_field(name="對方狀態",value=member.status,inline=True) # 顯示對方狀態
        embed.add_field(name="機器人",value=member.bot,inline=True) # 顯示對方狀態 
        embed.add_field(name=f"身分組：{len(roles)}",value=" ".join([role.mention for role in roles]),inline=False) # 顯示身分組
        embed.set_footer(text=f"ID:{member.id}")
        await ctx.send(embed=embed)

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