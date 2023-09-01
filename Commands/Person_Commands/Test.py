from discord.ext import commands

class Test(commands.Cog, name="Bro"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.command()
    async def test(self, ctx: commands.context):
        return await ctx.send(ctx, "hi")

def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))