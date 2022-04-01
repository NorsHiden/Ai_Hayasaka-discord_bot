import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import random
import datetime
import asyncio

class Slot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='slot')
    async def slot_(self, ctx):
        items = ['🍉', '🍊', '🍌', '🍍', '🍓', '🍒']

        item1 = random.choice(items)
        item2 = random.choice(items)
        item3 = random.choice(items)

        if item1 == item2 == item3:
            embed = discord.Embed(title=f"{item1} | {item2} | {item3}", description="3 in a row, You're **The Champion**!", color=discord.Color.random())
            await ctx.send(embed=embed)
        elif (item1 == item2) or (item1 == item3) or (item2 == item3):
            embed = discord.Embed(title=f"{item1} | {item2} | {item3}", description="2 in a row, You won.", color=discord.Color.random())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title=f"{item1} | {item2} | {item3}", description="No match, you lost.", color=discord.Color.random())
            await ctx.send(embed=embed)
        
    

def setup(bot):
    bot.add_cog(Slot(bot))