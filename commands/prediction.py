import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import datetime
import random
import asyncio

class Predict(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='predict')
    async def predict_(self, ctx, *, text):
        
        positive = ['Yes', 'Absolutely', 'Sure', 'I guarantee it', 'If it\'s not, what would it be?', 'Definitely', 'Unquestionably', 'It depends', 'May be', 'I think so', 'Obviously', 'Certainly']

        negative = ['No', 'Absolutely Not', 'Definitely not', 'Surely Not', 'I don\'t guarantee it', 'Most certainly not', 'Of course not', 'No way', 'On no occasion', 'Not the slightest bit', 'I don\'t think so', 'I guess not']

        choices = [random.choice(positive), random.choice(negative)]
        embedmsg = discord.Embed(title='Prediction', description=random.choice(choices), color=discord.Color.random())
        embedmsg.set_thumbnail(url='https://i.ibb.co/rQjCrzN/3vxSjtS.png')

        await ctx.send(embed=embedmsg)
        
    

def setup(bot):
    bot.add_cog(Predict(bot))