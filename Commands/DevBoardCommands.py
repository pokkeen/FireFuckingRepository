import TrelloWrapperButClasses
import datetime
import requests
import discord
from roblox import Client
from discord.ext import commands
from discord import app_commands


TrelloBoard = TrelloWrapperButClasses.TrelloBoard
date = datetime
RoClient = Client()

ToDoBoard = TrelloBoard("Dev ToDo Board", '64f8ad85266330f160f747d7')

class DevCommands(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client

    @app_commands.command(name='addtodo', description='Adds to the to do list on the trello')
    @app_commands.describe(todoname='Select a name for the problem')
    @app_commands.describe(tododesc='Put a description of the problem')
    async def AddToDo(self, interaction:discord.Interaction, todoname:str, tododesc:str):
        response = requests.get(f'https://api.blox.link/v4/public/guilds/964609612496142416/discord-to-roblox/441389433061638155',  headers={"Authorization" : 'a91fa14d-c868-48b9-af94-73b60a08561f'})
        ID = response.json()['robloxID']
        User =  f'https://www.roblox.com/users/{ID}/profile'
        UserName = await RoClient.get_user(ID)
        name = f'{todoname} | created by {UserName.name}'
        desc = f'{tododesc} | created by {User} on {date.date.today()}'
        ToDoBoard.CreateCard(name,desc,'To do')
        await interaction.response.send_message(content=f'Created card {todoname}')
    


    @app_commands.command(name='claimtodo', description='Claims a to do on the trello')
    @app_commands.describe(cardname='Claim a card!')
    async def ClaimToDo(self, interaction:discord.Interaction, cardname:str):
        if ToDoBoard.GetBoardCard(cardname)['name'] not in ToDoBoard.GetListCards('To do'):
            await interaction.response.send_message(content='That card is not in the todo list')
        response = requests.get(f'https://api.blox.link/v4/public/guilds/964609612496142416/discord-to-roblox/441389433061638155',  headers={"Authorization" : 'a91fa14d-c868-48b9-af94-73b60a08561f'})
        ID = response.json()['robloxID']
        User =  f'https://www.roblox.com/users/{ID}/profile'
        UserName = await RoClient.get_user(ID)
        OldDesc = ToDoBoard.GetBoardCard(cardname)['desc']
        NewDesc = f'{OldDesc} \nclaimed by {User}'
        ToDoBoard.EditCardDesc(NewDesc, cardname)
        
    
    @app_commands.command(name='displaytodo', description='Displays the to do list')
    async def DisplayToDo(self, interaction:discord.Interaction):
        return
         


async def setup(client):
    await client.add_cog(DevCommands(client))
    
