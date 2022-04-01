import discord
from discord.ext import commands
from discord_components import (
    Button,
    ButtonStyle,
    Select,
    SelectOption,
)
import datetime
import requests
import asyncio


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='weather', aliases=["we"])
    async def weather_(self, ctx, *, city: str):
        apikey = '1db892f27f613456cfba78af25416f11'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = f"{base_url}appid={apikey}&q={city}"
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel
        if x["cod"] != "404":
            async with channel.typing():
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature_celsiuis = str(
                    round(current_temperature - 273.15))
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                weather_description = z[0]["description"]
                embed = discord.Embed(
                    title=f"Weather in {city}",
                    color=ctx.guild.me.top_role.color,
                    timestamp=ctx.message.created_at,
                )
                embed.add_field(name="Descripition",
                                value=f"**{weather_description}**",
                                inline=False)
                embed.add_field(name="Temperature(C)",
                                value=f"**{current_temperature_celsiuis}°C**",
                                inline=False)
                embed.add_field(name="Humidity(%)",
                                value=f"**{current_humidity}%**",
                                inline=False)
                embed.add_field(name="Atmospheric Pressure(hPa)",
                                value=f"**{current_pressure}hPa**",
                                inline=False)
                embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                await channel.send(embed=embed)
        else:
            await channel.send("City not found.")


def setup(bot):
    bot.add_cog(Weather(bot))
