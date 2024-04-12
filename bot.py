from src.rps import rps
from src.cf.coinflip import coin_flip
import os
from dotenv import load_dotenv
import discord, logging, logging.handlers

load_dotenv()

# Set up logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename='src/logs/botlog.txt',
    encoding='utf-8',
    maxBytes=32 * 1024 * 1024,  
    backupCount=5,  
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)

class MyClient(discord.Client):
    async def on_ready(self):
        logger.info('Logged on as {0}!'.format(self.user))
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        logger.info('Message from {0.author}: {0.content}'.format(message))
        print(f'Message from {message.author}: {message.content}')
        await self.bot_command(message)

    async def bot_command(self, message):
        if message.content == 'ping':
            await message.channel.send('```bong```')
            
        elif message.content.startswith('rps'):
            await self.rps_command(message)
            
        elif message.content.startswith('cf'):
            await self.coinflip_command(message)
            
    async def rps_command(self, message):
        try:
            _, user_choice = message.content.split(' ')
            if user_choice not in ['rock', 'paper', 'scissors']:
                raise ValueError
            computer_choice = rps.get_computer_choice()
            result = rps.determine_winner(user_choice, computer_choice)
            await message.channel.send(result)
        except ValueError:
            await message.channel.send("```Invalid input. Input 'rps' followed by rock, paper, or scissors```")

    async def coinflip_command(self, message):
        try:
            _, user_guess = message.content.split(' ')
            if user_guess not in ['heads', 'tails']:
                raise ValueError
            response = coin_flip(user_guess)
            await message.channel.send(response)
        except ValueError:
            await message.channel.send("```Invalid input. Input 'cf' followed by heads or tails```")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv('DISCORD_TOKEN'))

