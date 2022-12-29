from logic_server.middleware import check_subscribe
from aiogram import types
from init_bot import dispatcher


@dispatcher.message_handler()
@check_subscribe
async def reply_just_text(message: types.Message):
    await message.answer(text=' ')


