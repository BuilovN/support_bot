import os
from support_bot_app.models import Message as MessageModel, Customer as CustomerModel
from django.utils import timezone
from datetime import datetime as dt
from .parser import *
import requests

# from pytz import timezone


class SupportBot:
    def __init__(self):
        pass

    def send_message(self, chat_id, text):
        apikey = os.environ['APIKEY']
        url = f"https://api.telegram.org/bot{apikey}/sendMessage"
        data = {
            "chat_id": chat_id,
            "text": text,
        }
        requests.post(url, json=data)

    @staticmethod
    def parse_update_to_message_model(update: dict, checked=False, is_reply=False):
        try:
            update = parse_update(update)
            message = update.message
            chat = message.chat
            text = message.text
            message_date = dt.fromtimestamp(message.date)
            user_id = chat.id
            message_checked = checked
            message_is_reply = is_reply
        except KeyError as e:
            raise e

        new_message = MessageModel(text=text,
                                   telegram_id=user_id,
                                   date=message_date,
                                   checked=message_checked,
                                   is_reply=message_is_reply, )
        return new_message

    @staticmethod
    def parse_update_to_customer_model(update: dict, checked=False, is_reply=False):
        try:
            update = parse_update(update)
            message = update.message
            chat = message.chat
            user_id = chat.id
            first_name = chat.first_name
            last_name = chat.last_name
            username = chat.username
        except KeyError as e:
            raise e

        new_customer = CustomerModel(telegram_id=user_id,
                                     username=username,
                                     first_name=first_name,
                                     last_name=last_name,)
        return new_customer