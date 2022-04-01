import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
from discord.utils import get
import datetime
import asyncio

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help')
    async def help_(self, ctx):
        welcomeemo = self.bot.get_emoji(902966965855989820)
        serveremo = self.bot.get_emoji(902966965998612481)
        modemo = self.bot.get_emoji(902966958578880562)
        infoemo = self.bot.get_emoji(902966960726372382)
        funemo = self.bot.get_emoji(902966965327523910)
        moduleemo = self.bot.get_emoji(902966927209672766)


        embedmsg = discord.Embed(title=f"{welcomeemo} Welcome!", description=f"{serveremo} Server : `{ctx.guild.name}`", color=0xffe175)
        embedmsg.set_thumbnail(url="https://cdn140.picsart.com/323536520537211.png?type=webp&to=min&r=640")
        embedmsg.add_field(name=f"{moduleemo} Modules:", value=f">>> ┠{modemo} Moderation\n┠ {infoemo} Info user/server\n┠ {funemo} Fun")
        embedmsg.set_footer(text="Choose the module you need!", icon_url=ctx.author.avatar_url)


        helpmod = discord.Embed(title=f"{modemo} Help Moderation", description=f"""`[] - Required Argument | () - Optional Argument`
        ```ini\nai clear - [amount] - Clear Message\nai say - [text] - Bot Message\nai slw - [seconds] - Slow Mode\nai pm - [@user] [text] - Sending a hidden message to private messages```""", color=0xffe175)
        helpmod.set_thumbnail(url="https://cdn140.picsart.com/323536520537211.png?type=webp&to=min&r=640")

        helpinfo = discord.Embed(title=f"{infoemo} Help Information", description=f"""`[] - Required Argument | () - Optional Argument`
        ```ini\nai ping - ping\nai screenshot / scr - [URL] - screenshot a website\nai weather / we - [city] - Weather\nai poll - (text) - Poll\nai serverinfo / si - Server Information```""", color=0xffe175)
        helpinfo.set_thumbnail(url="https://cdn140.picsart.com/323536520537211.png?type=webp&to=min&r=640")

        helpfun = discord.Embed(title=f"{funemo} Help Fun", description=f"""`[] - Required Argument | () - Optional Argument`
        ```ini\nai predict - [text] - Predict future\nai ascii - [text] - Ascii Art\nai slot - Slot Machine\nai achievement / achiev - [text] - Achievement picture```""", color=0xffe175)
        helpfun.set_thumbnail(url="https://cdn140.picsart.com/323536520537211.png?type=webp&to=min&r=640")

        await ctx.send(embed=embedmsg, components=[Select(placeholder = "Select a module!", options = [SelectOption(label = "Help Moderation", value = "A", description="Moderating your server...", emoji=modemo), SelectOption(label = "Help Information", description="Information user/server/weather...", value = "B", emoji=infoemo), SelectOption(label = "Help Fun", description="Fun commands...", value = "C", emoji=funemo)])])

        while True:
            try:
                interaction = await self.bot.wait_for("select_option", timeout=30)
            except:
                break

            if interaction.values[0] == "A":
                await interaction.send(embed=helpmod)
            elif interaction.values[0] == "B":
                await interaction.send(embed=helpinfo)
            elif interaction.values[0] == "C":
                await interaction.send(embed=helpfun)
    

def setup(bot):
    bot.add_cog(Help(bot))