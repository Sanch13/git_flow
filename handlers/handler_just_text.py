from settings import settings
from logic_server.middleware import check_sub_channel
from aiogram import types
from init_bot import bot, dispatcher


@dispatcher.message_handler()
async def reply_just_text(message: types.Message):
    user_id = message.from_user.id
    if check_sub_channel(await bot.get_chat_member(chat_id=settings.CHANNEL_ID, user_id=user_id)):
        text = f"Вы можете отправлять только изображения и команды :" \
               # + get_all_bot_commands(commands=settings.COMMANDS)
        await message.answer(text=text)
    else:
        text = settings.ANSWER_NOT_SUB
        await message.answer(text=text)
        await message.delete()
