import discord
from discord.ext import commands
import pyfiglet
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import datetime
import asyncio

class Ascii(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ascii')
    async def ascii_(self, ctx, *, text):
        ascii_banner = pyfiglet.figlet_format(text)
        await ctx.send(f"```{ascii_banner}```")
        
    

def setup(bot):
    bot.add_cog(Ascii(bot))