import discord
from discord.ext import commands
from discord import option
from discord import guild_only

from src.rps import rps
from src.cf.coinflip import coin_flip
from src.mastodon.mastodonbot import MastodonBot

GUILD_IDS = [1226637122526515320]

class Socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mastodonBot = MastodonBot() 

    # @discord.slash_command(name="mastodon", guild_ids=GUILD_IDS)
    # @guild_only()
    # @option("choice", description="Choose!", choices=[
    #     discord.OptionChoice(name="🪨", value="rock"),
    #     discord.OptionChoice(name="📃", value="paper"),
    #     discord.OptionChoice(name="✂️", value="scissors")])
    # async def rock_paper_scissors(self, ctx : discord.ApplicationContext, choice:str):
    #     """Rock paper scisscors 🪨📃✂️"""  # The command description can be supplied as the docstring
         
    #     mastodonBot.post_status(choice) 
    #     await ctx.respond(result)

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Games(bot)) # add the cog to the bot