import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
from PIL import Image, ImageDraw, ImageFont
import io
import datetime
import asyncio

class Achievement(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='achievement', aliases=['achiev'])
    async def achievement_(self, ctx, *, achievement: str):
        ctx.message.delete()
        image = Image.open('achievement_unlocked.png')
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype('arial.ttf', 60)
        draw.text( (400, 280), achievement, fill=(255,255,255), font=font)
        buffer = io.BytesIO()

        image.save(buffer, format='PNG')

        buffer.seek(0)

        await ctx.send(file=discord.File(buffer, 'myimage.png'))
        
    

def setup(bot):
    bot.add_cog(Achievement(bot))