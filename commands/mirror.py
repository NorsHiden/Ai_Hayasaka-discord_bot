import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import io
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
import datetime
import asyncio

class Mirror(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='mirxl')
    async def mirXL_(self, ctx):
        with ctx.typing():
            image = Image.open(requests.get(ctx.message.attachments[0].url, stream=True).raw).convert("RGBA")
            width, height = image.size
            im1 = image.crop((0, 0, width/2, height))
            image = ImageOps.mirror(image)
            image.paste(im1)
            buffer = io.BytesIO()

            image.save(buffer, format='PNG')

            buffer.seek(0)

        await ctx.send(file=discord.File(buffer, 'myimage.png'))

    @commands.command(name='mirxr')
    async def mirXR_(self, ctx):
        with ctx.typing():
            image = Image.open(requests.get(ctx.message.attachments[0].url, stream=True).raw).convert("RGBA")
            width, height = image.size
            im1 = image.crop((width/2, 0, width, height))
            image = ImageOps.mirror(image)
            image.paste(im1, (int(width/2), 0))
            buffer = io.BytesIO()

            image.save(buffer, format='PNG')

            buffer.seek(0)

        await ctx.send(file=discord.File(buffer, 'myimage.png'))
        
    

def setup(bot):
    bot.add_cog(Mirror(bot))