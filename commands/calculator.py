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

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='calculator', aliases=['cal'])
    async def calculator_(self, ctx):
        screen = '0'
        spaces = '᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼᲼'
        dzero = Button(style="2", label="00", custom_id="00")
        zero = Button(style="2", label="0", custom_id="0")
        one = Button(style="2", label="1", custom_id="1")
        two = Button(style="2", label="2", custom_id="2")
        three = Button(style="2", label="3", custom_id="3")
        four = Button(style="2", label="4", custom_id="4")
        five = Button(style="2", label="5", custom_id="5")
        six = Button(style="2", label="6", custom_id="6")
        seven = Button(style="2", label="7", custom_id="7")
        eight = Button(style="2", label="8", custom_id="8")
        nine = Button(style="2", label="9", custom_id="9")

        plus = Button(style="1", label="+", custom_id="+")
        minus = Button(style="1", label="-", custom_id="-")
        devide = Button(style="1", label="/", custom_id="/")
        power = Button(style="1", label="x", custom_id="*")
        point = Button(style="1", label=".", custom_id=".")

        quit = Button(style="4", label="Quit", custom_id="quit")
        back = Button(style="4", label="←", custom_id="back")
        clear = Button(style="4", label="Clear", custom_id="clear")
        equal = Button(style="3", label="=", custom_id="equal")

        embed = discord.Embed(title=f'Calculator{spaces}', description=f'```{screen}```', color=0x303434)
        message = await ctx.send(embed=embed, components=[[one, two, three, power, quit], [four, five, six, devide, back], [seven, eight, nine, plus, clear], [dzero, zero, point, minus, equal]])

        def check(msg):
            return (msg.author.id == ctx.author.id) and (msg.message.id == message.id)

        while True:
            try:
                interaction = await self.bot.wait_for("button_click", check=lambda i: check(i), timeout=60)
            except:
                await ctx.message.delete()
                await message.delete()
                break
            
            if interaction.custom_id == 'clear':
                screen = '0'
            elif interaction.custom_id == 'back':
                if screen == '0':
                    pass
                else:
                    screen = screen[:-1]
            elif interaction.custom_id == 'equal':
                try:
                    screen = str(eval(screen))
                except:
                    screen = 'Error'
            elif interaction.custom_id == 'quit':
                await ctx.message.delete()
                await message.delete()
                return
            else:
                if screen == '0' or screen == 'Error':
                    screen = interaction.custom_id 
                else:
                    screen += interaction.custom_id

            embed = discord.Embed(title=f'Calculator{spaces}', description=f'```{screen}```', color=0x303434)
            await message.edit(embed=embed, components=[[one, two, three, power, quit], [four, five, six, devide, back], [seven, eight, nine, plus, clear], [dzero, zero, point, minus, equal]])
            await interaction.respond(type=6)

            
        
        
    

def setup(bot):
    bot.add_cog(Calculator(bot))