import discord
import TrelloWrapper
from discord.ext import commands
from discord import app_commands

MainBoard = TrelloWrapper.TrelloBoard('FRR_MAIN','651d6fb8c277694097949b22')


class MainCommands(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name='add_points', description='add points to someone')
    @app_commands.describe(person= 'Put person in here')
    async def add_points(self, interaction: discord.Interaction, person:str):
        pass

"""
    Things I want for this bot:

    Main Commands (Cross Server For Most Part):
    
        - Add Hunt (Cross Server)
        - Announce (Cross server)
        - Apply (For what? Who knows) (Cross Server)
        - Myth (Main Only)
        - Schedule (Main only maybe)
        - Promote/Demote (Main only maybe)
        - Show hunts (Main Only Maybe)
        
"""
    

    


async def setup(client:commands.Bot) -> None:
    await client.add_cog(MainCommands(client))