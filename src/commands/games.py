import os

import discord
from discord.ext import commands
from discord import option
from discord import guild_only

from src.games import rps
from src.games import coinflip
from src.games.pokeapi import PokeApi

GUILD_IDS = [int(id) for id in os.getenv('GUILD_IDS').split(',')]


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.pokeApi = PokeApi()

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
        
    @discord.slash_command(name="pokemon", guild_ids=GUILD_IDS)
    @guild_only()
    @option("pokemon_name", description="Enter your Pokemon name", required=True)
    async def poke_search(self, ctx: discord.ApplicationContext, pokemon_name:str):
        """Search for a Pokemon!"""
        pokemon = self.pokeApi.get_pokemon(pokemon_name, is_shiny=True, is_female=False)  # replace with your function to search for a Pokemon

        if pokemon is None:
            await ctx.respond(f"No Pokemon found with the name {pokemon_name}")
        else:
            embed = discord.Embed(
                title=pokemon.name,
                description="Placeholder more stats will be added soon!",
                color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
            )

            embed.set_image(url=pokemon.sprite)

            await ctx.respond(" ", embed=embed)
            
            #async def hello(ctx):
                
    # embed = discord.Embed(
    #     title="My Amazing Embed",
    #     description="Embeds are super easy, barely an inconvenience.",
    #     color=discord.Colour.blurple(), # Pycord provides a class with default colors you can choose from
    # )
    # embed.add_field(name="A Normal Field", value="A really nice field with some information. **The description as well as the fields support markdown!**")

    # embed.add_field(name="Inline Field 1", value="Inline Field 1", inline=True)
    # embed.add_field(name="Inline Field 2", value="Inline Field 2", inline=True)
    # embed.add_field(name="Inline Field 3", value="Inline Field 3", inline=True)
 
    # embed.set_footer(text="Footer! No markdown here.") # footers can have icons too
    # embed.set_author(name="Pycord Team", icon_url="https://example.com/link-to-my-image.png")
    # embed.set_thumbnail(url="https://example.com/link-to-my-thumbnail.png")
    # embed.set_image(url="https://example.com/link-to-my-banner.png")
 
    # await ctx.respond("Hello! Here's a cool embed.", embed=embed) # Send the embed with some text

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Games(bot)) # add the cog to the bot