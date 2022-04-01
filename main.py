import discord
import os
import time
import discord.ext
from KeepAlive import keep_alive
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure, check
from discord_components import DiscordComponents, ComponentsBot

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=['Ai ', 'ai '],
                   intents=intents,
                   help_command=None,
                   activity=discord.Activity(type=discord.ActivityType.playing,
                                             name="ai help"),
                   status=discord.Status.idle)

DiscordComponents(bot)

keep_alive()
"""initial_extensions = ["commands.help", "commands.event"]

for extension in initial_extensions:
        try:
            bot.load_extension(extension)
            print(f"{extension} loaded successfully")
        except Exception as e:
            print(e)"""

for extension in os.listdir("./commands"):
    if extension.endswith(".py"):
        bot.load_extension(f"commands.{extension[:-3]}")
        print(f"{extension} loaded successfully")
    else:
        print(f"{extension} can't be loaded.")

bot.run(os.getenv("TOKEN"))
