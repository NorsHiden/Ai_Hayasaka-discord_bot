import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
from forex_python.converter import CurrencyRates
import datetime
import asyncio

class Currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='currency', aliases=['cur'])
    async def currency_(self, ctx, amount: int, format1:str, to: str, format2: str):
        c = CurrencyRates()
        result = c.convert(format1.upper(), format2.upper(), amount)
        embed = discord.Embed(title=f"{format1.upper()} to {format2.upper()}", description=f"{str(amount)} {format1.upper()} = {result} {format2.upper()}", color=discord.Color.random())
        embed.set_thumbnail(url="https://images-eu.ssl-images-amazon.com/images/I/61oqwXlDvOL.png")

        await ctx.send(embed=embed)

        
    

def setup(bot):
    bot.add_cog(Currency(bot))