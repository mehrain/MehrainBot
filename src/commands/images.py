import discord
import os
from discord.ext import commands
from src.img.image_manipulator import rotate_image, grayscale_image

GUILD_IDS = [int(id) for id in os.getenv('GUILD_IDS').split(',')]

#todo put image locations in a better place
class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="rotateimage", guild_ids=GUILD_IDS)
    @commands.guild_only()
    async def rotate(self, ctx: discord.ApplicationContext, degrees: int):
        """Rotate an image by a specified number of degrees. Upload an image to the channel first.""" 
        
        if not 0 <= degrees <= 360:
            await ctx.respond("Degrees must be between 0 and 360.")
            return

        await ctx.respond("Processing your request...")
        
        message = next((m for m in await ctx.channel.history(limit=10).flatten() if m.attachments and m.author == ctx.author), None)

        if not message:
            await ctx.send("No image found.")
            return

        attachment = message.attachments[0]
        await attachment.save("image.png")
        rotated_image = rotate_image("image.png", degrees)
        rotated_file = discord.File(rotated_image, filename="rotated_image.png")
        await ctx.send(content="Here's your rotated image:", file=rotated_file)
        os.remove("image.png")
        
    @discord.slash_command(name="grayscaleimage", guild_ids=GUILD_IDS)
    @commands.guild_only()
    async def grayscale(self, ctx: discord.ApplicationContext):
        """grayscale an image. Upload an image to the channel first.""" 
        await ctx.respond("Processing your request...")
        
        message = next((m for m in await ctx.channel.history(limit=10).flatten() if m.attachments and m.author == ctx.author), None)

        if not message:
            await ctx.send("No image found.")
            return

        attachment = message.attachments[0]
        await attachment.save("image.png")
        grayscaled_image = grayscale_image("image.png")
        grayscaled_file = discord.File(grayscaled_image, filename="grayscaled_image.png")
        await ctx.send(content="Here's your grayscaled image:", file=grayscaled_file)
        os.remove("image.png")

def setup(bot):
    bot.add_cog(Images(bot))
