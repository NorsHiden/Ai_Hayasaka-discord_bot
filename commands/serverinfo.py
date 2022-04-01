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


class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='serverinfo', aliases=['si'])
    async def serverinfo_(self, ctx):
        servermsg = discord.Embed(title="📜 Server Information",
                                  description=ctx.message.guild.description,
                                  color=discord.Color.random())
        servermsg.set_author(name=ctx.message.guild.name,
                             icon_url=ctx.message.guild.icon_url)
        servermsg.add_field(name='\u200b',
                            value=f"""**Name**: {ctx.message.guild.name}
        **Owner**: <@{ctx.message.guild.owner_id}>
        **Region**: {ctx.message.guild.region}
        **Rules channel**: <#848310173194125332>
        **Members**: {ctx.message.guild.member_count}
        **Verification level**: {ctx.message.guild.verification_level}
        **Created**: <t:{ctx.message.guild.created_at.strftime("%s")}:R>
        **Premium tier**: {ctx.message.guild.premium_tier}""",
                            inline=False)
        servermsg.set_thumbnail(url=ctx.message.guild.icon_url)
        servermsg.timestamp = datetime.datetime.utcnow()
        servermsg.set_footer(text=self.bot.user.display_name)
        await ctx.send(embed=servermsg)


def setup(bot):
    bot.add_cog(ServerInfo(bot))
