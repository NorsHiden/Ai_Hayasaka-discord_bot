import discord
from discord.ext import commands
import re
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import aiohttp
import io
import datetime
import asyncio

class Screenshot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='screenshot', aliases=['scr'])
    async def screenshot_(self, ctx, URL: str):
        if not (URL.startswith('https://') or URL.startswith('http://')):
            URL = 'https://www.' + URL

        mainurl = "https://image.thum.io/get/width/1280/crop/1280/noanimate"
        
        async with ctx.typing():
            async with aiohttp.ClientSession() as session:
                async with session.get(mainurl + URL) as resp:
                    if resp.status != 200:
                        msg = discord.Embed(title='Invalid URL', description='Check if the url is valid.', color=discord.Color.random())
                        await ctx.send(embed=msg)
                        return
                    data = io.BytesIO(await resp.read())
                    await ctx.send(file=discord.File(data, 'website.png'))

def setup(bot):
    bot.add_cog(Screenshot(bot))