import os
from discord.ext import commands
from discord import File
from src.img.image_manipulator import rotate_image  

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rotate")
    async def rotate(self, ctx, degree: int = None):
        """Rotate an image by a certain degree."""
        if degree is None or degree < 0 or degree > 360:
            await ctx.send("Please provide valid degrees to rotate the image. The degree should be between 0 and 360.")
            return

        if not ctx.message.attachments:
            await ctx.send("No image found. Please send the command again with an image.")
            return

        # Get the first attachment from the message
        attachment = ctx.message.attachments[0]

        # Download the attachment
        await attachment.save("image.png")

        # Rotate the image
        rotated_image = rotate_image("image.png", degree)

        # Create a discord.File object from the rotated image
        rotated_file = File(rotated_image, filename="rotated_image.png")

        # Send the rotated image as a response
        await ctx.send(file=rotated_file)

        # Delete the downloaded image file
        os.remove("image.png")

def setup(bot):
    bot.add_cog(Images(bot))