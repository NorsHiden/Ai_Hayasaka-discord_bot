import discord
from discord.ext.commands import CheckFailure
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import datetime
import asyncio

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='clear')
    @commands.has_permissions(administrator=True)
    async def clear_(self, ctx, amount: int=5):
        await ctx.channel.purge(limit=amount+1)

    @clear_.error
    async def clear_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            embedmsg = discord.Embed(title="Ops!", description=error, color = discord.Color.random())
            await ctx.send(embed=embedmsg)
    

def setup(bot):
    bot.add_cog(Clear(bot))