import os

import discord
from discord.ext import commands
from discord import option
from discord import guild_only

from src.socials.mastodonbot import MastodonBot

GUILD_IDS = [int(os.getenv('MCP_GUILD_ID'))]

class Socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mastodonBot = MastodonBot() 

    @discord.slash_command(name="mastodon", guild_ids=GUILD_IDS)
    @guild_only()
    @option("post_text", description="Enter your post text", required=True)
    async def mastodon(self, ctx : discord.ApplicationContext, post_text:str):
        """Mastodon Function Calls"""  # The command description can be supplied as the docstring
             
        self.mastodonBot.post_status(post_text) 
        post_text = str(post_text)
        await ctx.respond(f"The following message has been send to Mastodon: {post_text}")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Socials(bot)) # add the cog to the bot