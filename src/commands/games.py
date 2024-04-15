import os

import discord
from discord.ext import commands
from discord import option
from discord import guild_only

from src.games import rps
from src.games import coinflip

GUILD_IDS = [int(os.getenv('MCP_GUILD_ID'))]


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="rps", guild_ids=GUILD_IDS)
    @guild_only()
    @option("choice", description="Choose your hand!", choices=[
        discord.OptionChoice(name="🪨", value="rock"),
        discord.OptionChoice(name="📃", value="paper"),
        discord.OptionChoice(name="✂️", value="scissors")])
    async def rock_paper_scissors(self, ctx : discord.ApplicationContext, choice:str):
        """Rock paper scisscors 🪨📃✂️"""  # The command description can be supplied as the docstring
        computer_choice = rps.get_computer_choice()
        result = rps.determine_winner(choice, computer_choice)
        await ctx.respond(result)
        
    @discord.slash_command(name="coinflip", guild_ids=GUILD_IDS)
    @guild_only()
    @option("choice", description="Choose your side!", choices=[
    discord.OptionChoice(name="heads", value="heads"),
    discord.OptionChoice(name="tails", value="tails"),])
    async def coinflip(self, ctx: discord.ApplicationContext, choice:str):
        """Flip a coin and get heads or tails!"""
        result = coinflip.coin_flip(choice)
        await ctx.respond(result)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Games(bot)) # add the cog to the bot