import discord
from discord.ext import commands
from discord import app_commands

class Example(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('hi')

    @app_commands.command(name='color', description='nah')
    @app_commands.describe(color = 'fuck uhm')
    async def colour(self, interaction: discord.Interaction, color:str):
        await interaction.response.send_message(content=color)

async def setup(client:commands.Bot) -> None:
    await client.add_cog(Example(client))
    
