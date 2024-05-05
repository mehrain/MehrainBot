import os
from dotenv import load_dotenv
from src.logs.logger_setup import setup_logger
import discord
import pokebase as pb
from src.socials.mastodonbot import MastodonBot

# Set the cache directory to a persistent directory inside the Docker container for caching Pokemon data
pb.cache.CACHE_DIR = '/home/container/.cache'


logger = setup_logger()
load_dotenv()
bot = discord.Bot()

# ** Guild_ids are used instead of global since these have instant updates, global commands take up to an hour to update
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
    'images',
]

for cog in cogs_list:
    bot.load_extension(f'src.commands.{cog}')

bot.run(DISC_TOKEN)