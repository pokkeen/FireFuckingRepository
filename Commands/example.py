import discord
from discord.ext import commands
from discord import app_commands

class Example(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    #@commands.command()
    #async def ping(self, ctx):
       # response = requests.get(f'https://api.blox.link/v4/public/guilds/964609612496142416/discord-to-roblox/441389433061638155',  headers={"Authorization" : 'a91fa14d-c868-48b9-af94-73b60a08561f'})
       #   print(response.json()['robloxID'])
     #   await ctx.send(ctx.guild.id)

    @app_commands.command(name='color', description='nah')
    @app_commands.describe(color = 'fuck uhm')
    async def colour(self, interaction: discord.Interaction, color:str):
        await interaction.response.send_message(content=color)

async def setup(client:commands.Bot) -> None:
    await client.add_cog(Example(client))
    
