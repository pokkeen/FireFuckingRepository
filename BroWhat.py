import discord
from discord.ext import commands
from discord.ext import 

intents = discord.Intents.all()
client = commands.Bot(command_prefix= '!',intents=intents)

@client.event
async def on_ready():
    print("Bot is ready!")
    print("-------------")

client.load_extension("Commmands.Person_Commands.Test")

client.run('MTEzMjgzNjA4MDI5NTYxMjQ2Ng.Gvpt7j.6WuTOQZQDu9aDOea9LZYfXUnSq5ULzhAz1K638')