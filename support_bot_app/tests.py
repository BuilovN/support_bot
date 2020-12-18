# from django.test import TestCase
# from django.utils import timezone
# from support_bot_app.lib.bot.support_bot import SupportBot
# from .models import Message
# from datetime import datetime
#
#
# class BotTestCase(TestCase):
#     def test_parse_correct_income_request_to_bot(self):
#         text = "Hello world!"
#         message_date = 1606261401
#         user_id = 342140103
#         user_username = "builovn"
#         user_first_name = "Никита"
#         user_last_name = "Буйлов"
#         body = {
#             "update_id": 314677213,
#             "message": {
#                 "message_id": 2,
#                 "from": {
#                     "id": 342140103,
#                     "is_bot": False,
#                     "first_name": "Никита",
#                     "last_name": "Буйлов",
#                     "username": "builovn",
#                     "language_code": "en"
#                 },
#                 "chat": {
#                     "id": user_id,
#                     "first_name": user_first_name,
#                     "last_name": user_last_name,
#                     "username": user_username,
#                     "type": "private"
#                 },
#                 "date": message_date,
#                 "text": text
#             }
#         }
#         correct_message = Message(text=text,
#                                   telegram_id=user_id,
#                                   username=user_username,
#                                   first_name=user_first_name,
#                                   last_name=user_last_name,
#                                   date=datetime.fromtimestamp(message_date, tz=timezone.get_current_timezone()),
#                                   checked=False,
#                                   is_reply=False, )
#
#         message = SupportBot.parse_update_to_message_model(body)
#         self.assertEqual(message.text, correct_message.text)
#         self.assertEqual(message.username, correct_message.username)
#         self.assertEqual(message.first_name, correct_message.first_name)
#         self.assertEqual(message.last_name, correct_message.last_name)
#         self.assertEqual(message.date, correct_message.date)
#         self.assertEqual(message.checked, correct_message.checked)
#         self.assertEqual(message.is_reply, correct_message.is_reply)
#
#     def test_parse_incorrect_income_request_to_bot(self):
#         body = {
#             "message": {
#                 "from": {
#                     "id": 342140103,
#                     "is_bot": False,
#                     "first_name": "Никита",
#                     "last_name": "Буйлов",
#                     "username": "builovn",
#                     "language_code": "en"
#                 },
#             }
#         }
#         self.assertRaises(KeyError, SupportBot.parse_update_to_message_model, body)
