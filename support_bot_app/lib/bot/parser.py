from .telegram_entities import *
import datetime


def parse_update(update: dict):
    try:
        update_id = update["update_id"]
        message = parse_message(update["message"])
        return Update(update_id, message)
    except KeyError as e:
        raise e


def parse_message(message: dict):
    try:
        message_id = message["message_id"]
        date = message["date"]
        chat = parse_chat(message["chat"])
        text = message["text"]
        return Message(message_id, date, chat, text)
    except KeyError as e:
        raise e


def parse_chat(chat: dict):
    try:
        id = chat["id"]
        type = chat["type"]
        first_name = chat["first_name"]
        last_name = chat["last_name"]
        username = chat["username"]
        return Chat(id, type, first_name, last_name, username)
    except KeyError as e:
        raise e
