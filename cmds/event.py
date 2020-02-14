import discord
from discord.ext import commands
from core.classes import Cog_Extension
from core.errors import Errors

class error(Cog_Extension):

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        try:
            # 傳送至錯誤處理器
            await Errors.error_process(self,ctx,error)
        except AttributeError:
            pass

def setup(bot):
    bot.add_cog(error(bot))