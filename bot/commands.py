# Here we will create the methods that are directly called from commands through discord
from utils.text_formatter import bold


async def send_greetings(interaction) -> None:
    await interaction.response.send_message(f'Hello, I am {bold("ALIVE")}!')
