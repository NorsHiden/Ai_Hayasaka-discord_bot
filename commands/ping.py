import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import datetime
import asyncio

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping_(self, ctx):
        msg = discord.Embed(title='🏓Pong!', description=f'{round(self.bot.latency * 1000)} ms', color=discord.Color.random())
        await ctx.send(embed=msg)
        
    

def setup(bot):
    bot.add_cog(Ping(bot))