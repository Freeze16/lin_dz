from discord import Member
from discord.ext.commands import Bot
from discord.ext.commands.context import Context


def __init__(bot: Bot):
    kick_member(bot)


def kick_member(bot: Bot):
    @bot.command()
    async def kick(ctx: Context, member: Member):
        print(member.id)
        member: Member = ctx.guild.get_member(member.id)
        print(member)
        await member.kick(reason=f'{ctx.author} Выгнал {member}')
