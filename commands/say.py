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

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='say')
    async def say_(self, ctx, *, text):
        await ctx.message.delete()
        await ctx.send(text)
        
    

def setup(bot):
    bot.add_cog(Say(bot))