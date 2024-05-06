import discord
from discord.ext import commands

from core import talk
from core import music
from core import admin
from core.config import load_config

config = load_config()

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix=config.prefix, intents=intents)


@bot.event
async def on_ready():
    talk.__init__(bot)
    music.__init__(bot)
    admin.__init__(bot)
    await bot.change_presence(status=discord.Status.online)


if __name__ == '__main__':
    bot.run(token=config.token)
