import discord
import os
from discord.ext import commands
from discord import File, guild_only
from src.img.image_manipulator import rotate_image

GUILD_IDS = [int(id) for id in os.getenv('GUILD_IDS').split(',')]

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="rotateimage", guild_ids=GUILD_IDS)
    @commands.guild_only()
    async def rotate(self, ctx: discord.ApplicationContext, degrees: int):
        """Rotate an image by a certain degree."""
        
        # Send an initial response
        await ctx.respond("Processing your request...")
        
        
        # Get the most recent message in the channel with an attachment
        message = next((m for m in await ctx.channel.history(limit=10).flatten() if m.attachments and m.author == ctx.author), None)

        if not message:
            await ctx.send("No image found.")
            return

        
        print("Received message with attachments.")

        # Get the first attachment from the message
        attachment = message.attachments[0]

        # Download the attachment
        await attachment.save("image.png")

        print("Downloaded attachment.")

        # Rotate the image
        rotated_image = rotate_image("image.png", degrees)

        print("Rotated image.")

        # Create a discord.File object from the rotated image
        rotated_file = discord.File(rotated_image, filename="rotated_image.png")

        print("Created File object.")

        # Send the rotated image as a response
        await ctx.send(content="Here's your rotated image:", file=rotated_file)

        print("Sent rotated image.")

        # Delete the downloaded image file
        os.remove("image.png")

        print("Deleted downloaded image file.")

def setup(bot): # this is called by Pycord to setup the cog
    bot.add_cog(Images(bot)) # add the cog to the bot