import TrelloWrapperButClasses
import datetime
import roblox
import requests
import discord
from TrelloWrapperButClasses import ListsDict
from TrelloWrapperButClasses import CardsDict
from TrelloWrapperButClasses import LabelsDict
from discord.ext import commands
from discord import app_commands


TrelloBoard = TrelloWrapperButClasses.TrelloBoard
date = datetime
RoClient = roblox.client    

ToDoBoard = TrelloBoard("Dev ToDo Board", '64f8ad85266330f160f747d7')

ToDoBoard.InitalizeBoard()

class DevCommands(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name='addtodo', description='Adds to the to do list on the trello')
    @app_commands.describe(todoname='Select a name for the problem')
    @app_commands.describe(tododesc='Put a description of the problem')
    async def AddToDo(self, interaction:discord.Interaction, todoname:str, tododesc:str):
        response = requests.get(f'https://api.blox.link/v4/public/guilds/964609612496142416/discord-to-roblox/441389433061638155',  headers={"Authorization" : 'a91fa14d-c868-48b9-af94-73b60a08561f'})
        print(response.json())
        #Put roclient here
        name = f'{todoname} | created by {UserName}'
        desc = f'{tododesc} | created by {Put} on {date.date.today()}'
        ListsDict['Test2'].CreateCard(name,desc)
        await interaction.response.send_message(content=f'Created card {todoname}')
    
    @AddToDo.error
    async def AddToDoError():
        return
    
    @app_commands.command(name='claimtodo', description='Claims a to do on the trello')
    @app_commands.describe(cardname='Claim a card!')
    async def ClaimToDo(self, interaction:discord.Interaction, cardname:str):
        return
    
    @app_commands.command(name='displaytodo', description='Displays the to do list')
    async def DisplayToDo(self, interaction:discord.Interaction):
        


async def setup(client):
    await client.add_cog(DevCommands(client))
    
