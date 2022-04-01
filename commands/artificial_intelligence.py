import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
from prsaw import RandomStuff

import datetime
import asyncio

ai = RandomStuff(dev_name="Nors", bot_name="Ai Hayasaka", api_key = "pOktSd6zsDgW")



class Ai(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if self.bot.user == message.author:
            return
        elif message.content.startswith('ai') or message.content.startswith('Ai'):
            return
        
        if message.channel.id == 900908422202015764:
            async with message.channel.typing():
                response = ai.get_ai_response(message.content)
            if "Nors" in response[0]['message']:
                response[0]['message'] = response[0]['message'].replace("Nors", message.author.name)
            
            if "an AI Chatbot" in response[0]['message']:
                response[0]['message'] = response[0]['message'].replace("an AI Chatbot", self.bot.user.name)
            await message.channel.send(response[0]['message'])
        
    

def setup(bot):
    bot.add_cog(Ai(bot))