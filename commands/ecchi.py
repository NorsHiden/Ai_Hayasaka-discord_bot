import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import nekos
import datetime
import asyncio

class Ecchi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ecchi')
    @commands.is_nsfw()
    async def ecchi_(self, ctx):
        solo = Button(style="1", label="Solo", custom_id="solog")
        lewd = Button(style="2", label="Lewd", custom_id="lewd")
        hentai = Button(style="1", label="Hentai", custom_id="hentai")
        yuri = Button(style="2", label="Yuri", custom_id="yuri")
        futanari = Button(style="1", label="Futanari", custom_id="futanari")
        hololewd = Button(style="2", label="Hololewd", custom_id="hololewd")
        boobies = Button(style="1", label="Boobies", custom_id="boobs")
        delete = Button(style="4", label="Delete", custom_id="delete")

        message = await ctx.send('Choose your character', components=[[solo, lewd, hentai, yuri], [futanari, hololewd, boobies, delete]])

        def check(msg):
            return msg.author.id == ctx.author.id

        while True:
            try:
                interaction = await self.bot.wait_for("button_click", check=lambda i: check(i), timeout=30)
            except:
                await ctx.message.delete()
                await message.delete()
                break

            if interaction.custom_id == 'delete':
                await ctx.message.delete()
                await message.delete()
                break
            else:
                await interaction.send(nekos.img(interaction.custom_id))
        
    

def setup(bot):
    bot.add_cog(Ecchi(bot))