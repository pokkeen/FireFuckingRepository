import discord
from discord.ext import commands
import os

class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!',intents = discord.Intents.all())

    async def on_ready(self):
        await self.tree.sync()
        print("Bot is ready!")
        print("-------------")

    async def setup_hook(self):
        for filename in os.listdir('Commands'):
            if filename.endswith('.py'):
                await self.load_extension(f'Commands.{filename[:-3]}')
                print(f'Commands.{filename[:-3]} loaded')

client = Client()

client.run('MTEzMjgzNjA4MDI5NTYxMjQ2Ng.Gvpt7j.6WuTOQZQDu9aDOea9LZYfXUnSq5ULzhAz1K638')





