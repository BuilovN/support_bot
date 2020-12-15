from support_bot_app.models import Message
from django.utils import timezone
from datetime import datetime
from .parser import *


# from pytz import timezone


class SupportBot:
    def __init__(self):
        pass

    @staticmethod
    def parse_update_to_message_model(update: dict, checked=False, is_reply=False):
        try:
            update = parse_update(update)
            message = update.message
            chat = message.chat
            text = message.text
            message_date = datetime.fromtimestamp(message.date)
            user_id = chat.id
            user_username = chat.username
            user_first_name = chat.first_name
            user_last_name = chat.last_name
            message_checked = checked
            message_is_reply = is_reply
        except KeyError as e:
            raise e

        new_message = Message(text=text,
                              telegram_id=user_id,
                              username=user_username,
                              first_name=user_first_name,
                              last_name=user_last_name,
                              date=message_date,
                              checked=message_checked,
                              is_reply=message_is_reply, )
        return new_message
