from aiogram.types import ChatMember
from init_bot import bot


def check_sub_channel(chat_member: ChatMember) -> bool:
    """Return True if user is in group otherwise False"""
    return chat_member['status'] != 'left'


def get_all_bot_commands(commands: dict) -> str:
    """Return all the bot commands"""
    return ''.join(["\n/" + command for command in commands.values()])


def check_subscribe(func):
    from settings import settings

    async def wrapper(message, *args, **kwargs):
        user_id = message.from_user.id
        status = await bot.get_chat_member(chat_id=settings.CHANNEL_ID, user_id=user_id)
        print(status.status)
        print(status.__dict__)
        if status.status == 'left':
            text = f"Вы не подписаны на группу {settings.CHANNEL_LINK}." \
                   f"\nЧтобы пользоваться ботом подпишитесь!!!"
            await message.answer(text=text)
            await message.delete()
        else:
            text = f"Вы можете отправлять только изображения и команды :"
            await message.answer(text=text)
            await message.delete()
    return wrapper
