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


class User(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='user', aliases=['u'])
    async def user_(self, ctx, member: discord.Member = None):
        if member is None:
            member = ctx.author

        servermsg = discord.Embed(color=discord.Color.random())
        servermsg.set_author(name=member.name, icon_url=member.avatar_url)
        servermsg.add_field(name='User information:',
                            value=f"""**Name**: {member.name}
        **Nickname**: {member.nick}
        **Joined**: <t:{member.joined_at.strftime("%s")}:R>
        **Created**: <t:{member.created_at.strftime("%s")}:R>""")
        servermsg.set_thumbnail(url=member.avatar_url)
        servermsg.timestamp = datetime.datetime.utcnow()
        servermsg.set_footer(text=self.bot.user.display_name)
        await ctx.send(embed=servermsg)


def setup(bot):
    bot.add_cog(User(bot))
