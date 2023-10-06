import TrelloWrapper
import datetime
import requests
import discord
from roblox import Client
from discord.ext import commands
from discord import app_commands

date = datetime
RoClient = Client()

ToDoBoard = TrelloWrapper.TrelloBoard("FRR_DEV", '64f8ad85266330f160f747d7')

def ErrorHandler(interaction, data, task=None):
    if interaction.guild_id != 856655880431075369 and data[0] == True:
        return 'Wrong Guild'
    if ToDoBoard.GetBoardList(interaction.user.name) != None and data[1] == True:
        return 'You already have a claim list'
    if data[2] == True:
        if ToDoBoard.GetBoardCard(task) == None:
            return "Task doesn't exist"
    if ToDoBoard.GetBoardList(interaction.user.name) == None and data[3] == True:
        return "You don't have a claim list yet"
    if data[4] == True:
        if ToDoBoard.GetBoardCard(task)['idList'] != ToDoBoard.GetBoardList('To do')['id'] and ToDoBoard.GetBoardCard(task)['idList'] != ToDoBoard.GetBoardList(interaction.user.name)['id']:
            return "This task is already claimed or finished"
    return None

class DevCommands(commands.Cog):

    def __init__(self, client: commands.Bot):
        self.client = client
    
    @app_commands.command(name='add_task', description='Adds a tasks to the to do list')
    @app_commands.describe(taskname='Name the task', taskdesc='Describe the task', tasktype='What type of task is it')
    @app_commands.choices(tasktype=[app_commands.Choice(name='Building', value='Building'),app_commands.Choice(name='Modeling',value='Modeling'),app_commands.Choice(name='Scripting',value='Scripting')])
    async def add_task(self, interaction:discord.Interaction, taskname:str, taskdesc:str, tasktype: app_commands.Choice[str]):
        Error = ErrorHandler(interaction,[True,False,False,False,False])
        if Error != None:
            await interaction.response.send_message(content=Error)
            return
        Response = requests.request('GET', url=f'https://api.blox.link/v4/public/guilds/{interaction.guild_id}/discord-to-roblox/{interaction.user.id}', headers={"Authorization" : '3ea1b936-b4e8-4ed8-82ee-a7aa2be274c7'})
        print(Response.json())
        ID = Response.json()['robloxID']
        Username = await RoClient.get_user(ID)
        name, desc = f'{taskname} | created by {Username.name}', f'{taskdesc} | created on {date.date.today()}'
        ToDoBoard.CreateCard(name,desc,'To do',tasktype.value)
        await interaction.response.send_message(content=f'Created card {taskname}')

    @app_commands.command(name='add_dev',description='Makes you a claim list on the Trello')
    async def add_dev(self, interaction:discord.Interaction):
        Error = ErrorHandler(interaction, [True,True,False,False,False])
        if Error != None:
            await interaction.response.send_message(content=Error)
            return
        ToDoBoard.CreateList(f'Claim List | {interaction.user.name}')
        await interaction.response.send_message(content='List Created!')

    @app_commands.command(name='claim_task', description='Claim a task and put it on your task list')
    @app_commands.describe(taskname='Name the Task you wanna claim')
    async def claim_task(self, interaction:discord.Interaction, taskname:str):
        Error = ErrorHandler(interaction, [True,False,True,True,True], taskname)
        if Error != None:
            await interaction.response.send_message(content=Error)
            return
        ToDoBoard.Move(taskname,interaction.user.name)
        await interaction.response.send_message(content='Task claimed')
    
    @app_commands.command(name='finish_task', description='Set the task as done')
    async def finish_task(self, interaction:discord.Interaction, taskname:str):
        Error = ErrorHandler(interaction, [True,False,True,True,True], taskname)
        if Error != None:
            await interaction.response.send_message(content=Error)
            return
        ToDoBoard.Move(taskname,'Done')
        await interaction.response.send_message(content='Task completed')
    
    @app_commands.command(name='display_tasks', description='Displays the to do list')
    async def DisplayToDo(self, interaction:discord.Interaction):
        Error = ErrorHandler(interaction, [True,False,False,False,False])
        if Error != None:
            await interaction.response.send_message(content=Error)
        ebeder = discord.Embed(title='Task list', description="It's a task list")
        for tasks in ToDoBoard.GetListCards('To do'):
            labels = tasks['labels'][0]['name']
            desc = tasks['desc']
            ebeder.add_field(name=tasks['name'], value=f'Type:{labels} \n{desc}', inline=False)
        await interaction.response.send_message(embed=ebeder)

    @app_commands.command(name='display_claims', description='Displays your personal task list')
    async def DisplayClaims(self, interaction:discord.Interaction):
        Error = ErrorHandler(interaction, [True,False,False,False,False])
        if Error != None:
            await interaction.response.send_message(content=Error)
        ebed = discord.Embed(title='YOUR Task list', description="It's YOUR task list")
        for tasks in ToDoBoard.GetListCards(interaction.user.name):
            labels = tasks['labels'][0]['name']
            desc = tasks['desc']
            ebed.add_field(name=tasks['name'], value=f'Type:{labels} \n{desc}', inline=False)
        await interaction.response.send_message(embed=ebed)

async def setup(client):
    await client.add_cog(DevCommands(client))




