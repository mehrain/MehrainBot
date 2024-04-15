import os

import discord
from discord.ext import commands
from discord import option
from discord import guild_only

from src.socials.mastodonbot import MastodonBot

GUILD_IDS = [int(os.getenv('MCP_GUILD_ID'))]
MEHRAIN_ID = int(os.getenv('MEHRAIN_ID'))

class Socials(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mastodonBot = MastodonBot() 

    @discord.slash_command(name="mastodon", guild_ids=GUILD_IDS)
    @guild_only()
    @option("post_text", description="Enter your post text", required=True)
    async def mastodon(self, ctx : discord.ApplicationContext, post_text:str):
        """Mastodon Function Calls"""  
        if ctx.author.id == MEHRAIN_ID:     
            self.mastodonBot.post_status(post_text) 
            post_text = str(post_text)
            await ctx.respond(f"The following message has been send to Mastodon: {post_text}")
        else:
            author = str(ctx.author.display_name)
            await ctx.respond(f"Stop trolling {author}! You are not allowed to use this command.")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Socials(bot)) # add the cog to the bot