import discord
from discord import app_commands, Intents
from datetime import datetime
from constants import GUILD

# through intents, we can set individual flags
# https://discordpy.readthedocs.io/en/stable/api.html?highlight=intents#intents
intents = Intents.default()


class Client(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(intents=intents, *args, **kwargs)
        self.tree = app_commands.CommandTree(self)
        self.guild = discord.Object(id=GUILD)

    async def on_ready(self):
        await self.wait_until_ready()
        try:
            await self.tree.sync(guild=self.guild)
            print('Commands are now sync to the server.')
        except Exception as e:
            print(f"{e}|{type(e)}")
        print(
            f"We have logged in as {self.user} on {datetime.now().strftime('%A %d-%m-%Y, %H:%M:%S')}"
        )
