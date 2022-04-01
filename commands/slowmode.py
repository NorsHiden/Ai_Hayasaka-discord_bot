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

class Slowmode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='slowmode', aliases=['slw'])
    @commands.has_permissions(administrator=True)
    async def slowmode_(self, ctx, seconds: int=5):
        
        if seconds > 0:
            embedmsg = discord.Embed(title="Slowmode Enabled", description=f"Set the slowmode delay in this channel to {seconds} seconds!", color=0x63ff7d)
            await ctx.send(embed=embedmsg)
            await ctx.channel.edit(slowmode_delay=seconds)
        elif seconds == 0:
            embedmsg = discord.Embed(title="Slowmode Disabled", description=f"Set the slowmode delay in this channel to {seconds} seconds!", color=0x59c2ff)
            await ctx.send(embed=embedmsg)
            await ctx.channel.edit(slowmode_delay=seconds)
        else:
            embedmsg = discord.Embed(title="Error", description=f"Are you serious?", color=0xffdb70)
            await ctx.send(embed=embedmsg)

    @slowmode_.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            embedmsg = discord.Embed(title="Ops!", description=error, color = discord.Color.random())
            await ctx.send(embed=embedmsg)
    

def setup(bot):
    bot.add_cog(Slowmode(bot))