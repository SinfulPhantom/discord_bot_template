import discord
from discord import Interaction

from bot import constants, client
from bot.commands import send_greetings

from dotenv import load_dotenv
from os import getenv


# set up our environment
load_dotenv()
TOKEN = getenv("DISCORD_TOKEN")
GUILD = discord.Object(id=constants.GUILD_ID)

# set up our client
bot_client = client.Client()
tree = bot_client.tree


@tree.command(guild=GUILD, name='introduce', description='Meet the bot')
async def introduce(interaction: Interaction) -> None:
    await send_greetings(interaction)


# Run the bot!
bot_client.run(TOKEN)
