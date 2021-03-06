import unittest
import json
from django.test import TestCase
from support_bot_app.lib.bot.support_bot import SupportBot
from support_bot_app.models import Message, Customer
from datetime import datetime as dt

class TestSupportBot(TestCase):
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

    def test_parse_json_request_to_model_message(self):
        telegram_message_entity = self.update["message"]
        correct_message_model = Message(text=telegram_message_entity["text"],
                                        telegram_id=telegram_message_entity["chat"]["id"],
                                        date=dt.fromtimestamp(telegram_message_entity["date"]),
                                        is_reply=False,
                                        checked=False)
        test_message_model = SupportBot.parse_update_to_message_model(self.update)
        self.assertEqual(correct_message_model, test_message_model)

    def test_parse_json_request_to_model_customer(self):
        telegram_customer_entity = self.update['message']['chat']
        correct_customer_model = Customer(telegram_id=telegram_customer_entity['id'],
                                          first_name=telegram_customer_entity['first_name'],
                                          last_name=telegram_customer_entity['last_name'],
                                          username=telegram_customer_entity['username'], )
        test_customer_model = SupportBot.parse_update_to_customer_model(self.update)
        self.assertEqual(correct_customer_model, test_customer_model)
