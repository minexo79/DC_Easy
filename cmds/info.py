import discord
from discord.ext import commands
from core.classes import Cog_Extension

class info(Cog_Extension):

    @commands.command()
    async def ping(self,ctx):
        '''查詢延遲'''
        await ctx.send(f"延遲：`{round(self.bot.latency*1000)} ms`")

    @commands.command()
    async def about(self,ctx):
        '''關於機器人'''
        embed=discord.Embed(title="About Me")
        embed.add_field(name="名稱",value="DC_Easy",inline=False)
        embed.add_field(name="版本",value="1.0",inline=False)
        embed.add_field(name="簡介",value="Just for the Beginner.",inline=False)
        embed.set_footer(text="👾")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))
