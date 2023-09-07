import discord
from discord.ext import commands
import os
import asyncio

intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix= '!',intents=intents)

async def load():
    for filename in os.listdir('./Commands'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

load()

client.run('MTEzMjgzNjA4MDI5NTYxMjQ2Ng.Gvpt7j.6WuTOQZQDu9aDOea9LZYfXUnSq5ULzhAz1K638')





