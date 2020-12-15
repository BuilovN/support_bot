import unittest
import json
from support_bot_app.lib.bot.parser import *
import support_bot_app.lib.bot.telegram_entities


class TestParsingTelegramObject(unittest.TestCase):
    def setUp(self):
        request = """{
            "update_id":314677213,
            "message":{
                "message_id":2,
                "from":{
                    "id":342140103,
                    "is_bot":false,
                    "first_name":"Никита",
                    "last_name":"Буйлов",
                    "username":"builovn",
                    "language_code":"en"
                },
                "chat":{
                    "id":342140103,
                    "first_name":"Никита",
                    "last_name":"Буйлов",
                    "username":"builovn",
                    "type":"private"
                },
                "date":1606261401,
                "text":"yo"
            }
        }"""
        self.update = json.loads(request)

    def test_chat_parser(self):
        correct_chat = Chat(342140103,
                    "private",
                    "Никита",
                    "Буйлов",
                    "builovn")
        test_chat = parse_chat(self.update["message"]["chat"])
        self.assertEqual(correct_chat, test_chat)

    def test_message_parser(self):
        chat = Chat(342140103,
                    "private",
                    "Никита",
                    "Буйлов",
                    "builovn")
        correct_message = Message(2,
                          1606261401,
                          chat,
                          "yo")
        test_message = parse_message(self.update["message"])
        self.assertEqual(test_message, correct_message)

    def test_update_parser(self):
        chat = Chat(342140103,
                    "private",
                    "Никита",
                    "Буйлов",
                    "builovn")
        message = Message(2,
                          1606261401,
                          chat,
                          "yo")
        correct_update = Update(self.update["update_id"], message)
        test_update = parse_update(self.update)
        self.assertEqual(correct_update, test_update)