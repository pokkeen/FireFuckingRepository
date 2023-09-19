import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix= '!',intents=intents)

def Cog_loader():
    for filename in os.listdir('Commands'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
            print(f'cogs.{filename[:-3]} loaded')


@client.event
async def on_ready():
    Cog_loader()
    print("Bot is ready!")
    print("-------------")

client.run('MTEzMjgzNjA4MDI5NTYxMjQ2Ng.Gvpt7j.6WuTOQZQDu9aDOea9LZYfXUnSq5ULzhAz1K638')





