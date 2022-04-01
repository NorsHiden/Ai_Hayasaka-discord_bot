import discord
from discord.ext import commands
from discord.utils import get
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import datetime
import asyncio


class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.bot.user.name} is online")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        defaultRole = get(member.guild.roles, id=844333344815841280)
        await member.add_roles(defaultRole)
        welcomeMsg = discord.Embed(
            description=f"**Welcome {member.mention} to Legends Never Die.**",
            color=discord.Colour.random())
        welcomeMsg.set_author(name=f"{member.name} has joined the server!",
                              icon_url=member.avatar_url)
        welcomeMsg.add_field(name='\u200b',
                             value=f"""**Name**: {member.display_name}
        **Discriminator**: {member.discriminator}
        **Created at**: {member.created_at.strftime("%A, %B %d %Y %H:%M:%S %p")}
        **Premium since**: {member.premium_since}""",
                             inline=False)
        welcomeMsg.set_thumbnail(url=member.avatar_url)
        welcomeMsg.timestamp = datetime.datetime.utcnow()
        welcomeMsg.set_footer(text=self.bot.user.display_name)
        auditLogChannel = self.bot.get_channel(848529906173214750)
        await auditLogChannel.send(embed=welcomeMsg)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        welcomeMsg = discord.Embed(
            description=f"**Hope you had a great time here {member.mention}.**",
            color=discord.Colour.random())
        welcomeMsg.set_author(name=f"{member.name} has left the server!",
                              icon_url=member.avatar_url)
        welcomeMsg.add_field(name='\u200b',
                             value=f"""**Name**: {member.display_name}
        **Top Role**: {member.top_role}
        **Created at**: {member.created_at.strftime("%A, %B %d %Y %H:%M:%S %p")}
        **Premium since**: {member.premium_since}""",
                             inline=False)
        welcomeMsg.set_thumbnail(url=member.avatar_url)
        welcomeMsg.timestamp = datetime.datetime.utcnow()
        welcomeMsg.set_footer(text=self.bot.user.display_name)
        auditLogChannel = self.bot.get_channel(848529906173214750)
        await auditLogChannel.send(embed=welcomeMsg)


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.NSFWChannelRequired):
            msg = discord.Embed(title="This channel is not NSFW!!", description="Use NSFW commands in marked NSFW channel", color=0xf55b5b)
            msg.set_image(url="https://i.imgur.com/oe4iK5i.gif")
            return await ctx.send(embed=msg)
        elif isinstance(error, commands.MissingRequiredArgument):
            title_error_one = 'You have not entered anything after the command'
            desc_error_one = 'Use **ai help** to see a list of all the commands available'
            embed_var_one = discord.Embed(title=title_error_one, description=desc_error_one, color=0xFF0000)
            await ctx.reply(embed=embed_var_one)
        elif isinstance(error, commands.CommandNotFound):
            title_error_two = 'The command you have entered does not exist'
            desc_error_two = 'Use **.help** to see a list of all the commands available'
            embed_var_two = discord.Embed(title=title_error_two,description=desc_error_two,color=0xFF0000)
            await ctx.reply(embed=embed_var_two)
        elif isinstance(error, commands.MaxConcurrencyReached):
            title_error_four = 'Someone is already playing'
            desc_error_four = 'Please wait until the person currently playing is done with their turn'
            embed_var_four = discord.Embed(title=title_error_four, description=desc_error_four, color=0xFF0000)
            await ctx.reply(embed=embed_var_four)
        else:
            raise error


def setup(bot):
    bot.add_cog(Event(bot))
