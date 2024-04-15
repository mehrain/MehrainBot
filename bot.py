import os
from dotenv import load_dotenv

from src.logs.logger_setup import setup_logger

import discord


logger = setup_logger()
load_dotenv()
bot = discord.Bot()

GUILD_IDS = [int(id) for id in os.getenv('GUILD_IDS').split(',')]
DISC_TOKEN = os.getenv('DISCORD_TOKEN')

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

cogs_list = [
    'games',
    'socials',
]

for cog in cogs_list:
    bot.load_extension(f'src.commands.{cog}')

bot.run(DISC_TOKEN)