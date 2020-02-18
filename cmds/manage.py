import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core.datahook import yamlhook
from core.errors import Errors

class manage(Cog_Extension):

    @commands.command()
    async def check(self,ctx):
        '''檢查自訂權限'''
        ydata = yamlhook("config.yaml").open()
        if ctx.author.id == ydata['bot']['owner']:
            await ctx.send("你已在自訂權限名單內，恭喜可以存取。")
        else:
            error = "使用者沒有自訂權限(不在自訂權限名單內)。"
            # 因為process是自訂，錯誤訊息需自行撰寫。
            await Errors.error_process(self,ctx,error,process="custom")
            # 自訂錯誤訊息

    @commands.command() #截取對方資訊
    @commands.has_permissions(administrator=True)
    async def userinfo(self, ctx, member: discord.Member):
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
        
    @commands.command()
    async def serverinfo(self, ctx):
        '''伺服器資訊'''
        guild = ctx.guild
        embed=discord.Embed()
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_author(name=guild.name, icon_url=guild.icon_url)
        embed.add_field(name="伺服器擁有者",value=guild.owner.name,inline=True)
        embed.add_field(name="伺服器創立時間",value=guild.created_at.strftime("%Y.%m.%d-%H:%M:%S (UTC)"),inline=True)
        embed.add_field(name="伺服器成員數量",value=guild.member_count,inline=True)
        embed.add_field(name="文字頻道數量",value=len(guild.text_channels),inline=True)
        embed.add_field(name="語音頻道數量",value=len(guild.voice_channels),inline=True)
        embed.add_field(name="伺服器身分組數量",value=len(guild.roles),inline=True)
        embed.set_footer(text=f"ID:{guild.id}")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(manage(bot))
