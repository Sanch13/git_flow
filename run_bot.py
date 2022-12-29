from aiogram import executor
from init_bot import dispatcher
from handlers import handler_just_text, handler_send_photo, handler_commands
# from handlers.handler_just_text import reply_just_text
# from handlers.handler_commands import start_handler, help_handler
# from handlers.handler_send_photo import send_photo_to_group


if __name__ == '__main__':
    executor.start_polling(dispatcher, skip_updates=True)
