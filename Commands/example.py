import discord
from discord.ext import commands

class Example(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await print('Bot is online')

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

async def setup(client):
    await client.add_cog(Example(client))
        