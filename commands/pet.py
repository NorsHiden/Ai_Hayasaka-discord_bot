import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
from petpetgif import petpet as petpetgif
import requests
from io import BytesIO
import datetime
import asyncio

class Pet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pet')
    async def pet_(self, ctx, member: discord.Member=None):
        if member == None:
            member = ctx.author
        async with ctx.typing():
            img = requests.get(member.avatar_url)
            source = BytesIO(img.content) # file-like container to hold the emoji in memory
            source.seek(0)
            dest = BytesIO() # container to store the petpet gif in memory
            petpetgif.make(source, dest)
            dest.seek(0)
        await ctx.send(file=discord.File(dest, filename=f"{member.name}-petpet.gif"))

        
        
    

def setup(bot):
    bot.add_cog(Pet(bot))