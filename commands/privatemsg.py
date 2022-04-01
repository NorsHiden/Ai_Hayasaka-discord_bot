import discord
from discord.ext import commands
from discord.ext.commands import CheckFailure
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import datetime
import asyncio

class Privatemsg(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pm')
    @commands.has_permissions(administrator=True)
    async def privatemsg_(self, ctx, member: discord.Member, message: str):
        await ctx.message.delete()
        await member.send(message)

    @privatemsg_.error
    async def clear_error(self, ctx, error):
        if isinstance(error, CheckFailure):
            embedmsg = discord.Embed(title="Ops!", description=error, color = discord.Color.random())
            await ctx.send(embed=embedmsg)

def setup(bot):
    bot.add_cog(Privatemsg(bot))