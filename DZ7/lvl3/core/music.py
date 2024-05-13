from yt_dlp import YoutubeDL

import discord
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.ext.commands.context import Context

YDL_OPTIONS = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'noplaylist': True,
    'keepvideo': False,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320'
    }]
}

FFMPEG_OPTIONS = {'before_options': '-reconnect 1.txt -reconnect_streamed 1.txt -reconnect_delay_max 5', 'options': '-vn'}


def __init__(bot: Bot):
    join_voice(bot)
    leave_voice(bot)
    play_music(bot)
    pause_track(bot)


def join_voice(bot: Bot):
    @bot.command()
    async def join(ctx: Context):
        await ctx.author.voice.channel.connect()
        await ctx.message.delete()


def leave_voice(bot: Bot):
    @bot.command()
    async def leave(ctx: Context):
        await ctx.voice_client.disconnect(force=True)
        await ctx.message.delete()


def play_music(bot: Bot):
    @bot.command()
    async def play(ctx: Context, arg='test'):
        voice = await ctx.author.voice.channel.connect()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(arg, download=False)

        url = info['url']
        executable = '/home/freeze/projects/lin/DZ7/lvl3/core/ffmpeg/ffmpeg'
        voice.play(discord.FFmpegPCMAudio(executable=executable, source=url, **FFMPEG_OPTIONS))


def pause_track(bot: Bot):
    @bot.command()
    async def pause(ctx: Context):
        print(ctx.voice_client.client.status)
        # if not voice.is_paused():
        #     return await ctx.send('Not playing.')
        #
        # await voice.pause()
        # await ctx.send('⏭ | Skipped.')
