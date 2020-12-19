from django.test import TestCase
from datetime import datetime as dt
from support_bot_app.lib.validators import customer_validators as cv, message_validators as mv
from django.core.exceptions import ValidationError

class TestCostumerValidators(TestCase):

    def test_validate_telegram_id(self):
        correct_value = '123456789'
        cv.validate_telegram_id(correct_value)
        wrong_value = 'abcdf'
        self.assertRaises(ValidationError, cv.validate_telegram_id, wrong_value)

    def test_validate_name(self):
        correct_value = 'Nikita'
        cv.validate_name(correct_value)
        wrong_value = 'n1kit4'
        self.assertRaises(ValidationError, cv.validate_telegram_id, wrong_value)

    def test_validate_username(self):
        correct_value = 'Nikita'
        cv.validate_name(correct_value)
        wrong_value = 'n1kit4afafddafadfadfdasfdasfsafdacasdfewffasdfrewsfaqrfaefwfafeaw'
        self.assertRaises(ValidationError, cv.validate_telegram_id, wrong_value)

class TestMessageValidators(TestCase):

    def test_validate_text(self):
        correct_value = 'text'
        mv.validate_text(correct_value)
        wrong_value = ''
        self.assertRaises(ValidationError, mv.validate_text, wrong_value)

    def test_validate_date(self):
        correct_value = dt.now().replace(microsecond=0)
        mv.validate_date(correct_value)
        wrong_value = 'about Two pi am'
        self.assertRaises(ValidationError, mv.validate_date, wrong_value)

    def test_validate_boolean(self):
        correct_value = True
        mv.validate_boolean(correct_value)
        wrong_value = 'thats wrong value'
        self.assertRaises(ValidationError, mv.validate_boolean, wrong_value)