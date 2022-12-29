# import settings
#
# var = settings.Settings()
#
# print(settings.Settings().CHANNEL_LINK)
# print(var.CHANNEL_LINK)
users = {
    "alex": "left",
    "sanch": "admin",
}


def check_sub_channel1(key) -> bool:
    """Return True if user is in group otherwise False"""
    return users.get(key) != 'left'


def dec2(check_sub_channel1):
    text_answer_not_sub = f"Вы не подписаны на группу "

    def wrapper(key, *args, **kwargs):
        if check_sub_channel1(key):
            text = f"Вы можете отправлять только изображения и команды :"
            return text
        else:
            return text_answer_not_sub

    return wrapper

@dec2
def reply_just_text(message: str):
    return message



print(reply_just_text('1'))















