import os
from dotenv import load_dotenv
from src.logs.logger_setup import setup_logger
import discord
from src.socials.mastodonbot import MastodonBot

logger = setup_logger()
load_dotenv()
bot = discord.Bot()

GUILD_IDS = [int(id) for id in os.getenv('GUILD_IDS').split(',')]
DISC_TOKEN = os.getenv('DISCORD_TOKEN')

CHANNEL_IDS = [int(id) for id in os.getenv('CHANNEL_IDS').split(',')]
discord_channels = []

mastodon_bot = MastodonBot(bot, discord_channels)
bot.mastodon_bot = mastodon_bot

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    discord_channels.extend([bot.get_channel(id) for id in CHANNEL_IDS])

cogs_list = [
    'games',
    'socials',
]

for cog in cogs_list:
    bot.load_extension(f'src.commands.{cog}')

bot.run(DISC_TOKEN)