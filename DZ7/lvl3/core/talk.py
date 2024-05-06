from discord.ext.commands import Bot
from discord.ext.commands.context import Context


def __init__(bot: Bot):
    say_hello(bot)
    show_commands(bot)


def say_hello(bot: Bot):
    @bot.command()
    async def hello(ctx: Context):
        await ctx.reply('hello')


def show_commands(bot: Bot):
    @bot.command()
    async def commands(ctx: Context):
        await ctx.reply(
            'Для того чтобы включить музыку, введите "!play" и укажите ссылку на альбом с ютуба'
        )
