from django.db import models
from support_bot_app.lib.validators import customer_validators as cv, message_validators as mv


class Message(models.Model):
    text = models.TextField(mv.validate_text)
    telegram_id = models.CharField(max_length=10, validators=[cv.validate_telegram_id])
    date = models.DateTimeField(validators=[mv.validate_date])
    is_reply = models.BooleanField(validators=[mv.validate_boolean])
    checked = models.BooleanField(validators=[mv.validate_boolean]  )

    def __eq__(self, other):
        if not isinstance(other, Message):
            return NotImplemented
        if self._get_pk_val() is None and other._get_pk_val() is None:
            return self.text == other.text and\
                   self.telegram_id == other.telegram_id and\
                   self.date == other.date and \
                   self.is_reply == other.is_reply and \
                   self.checked == other.checked
        return self._get_pk_val() == other._get_pk_val()


class Customer(models.Model):
    telegram_id = models.CharField(max_length=10, validators=[cv.validate_telegram_id])
    username = models.CharField(max_length=32, validators=[cv.validate_username])
    first_name = models.CharField(max_length=64, validators=[cv.validate_name])
    last_name = models.CharField(max_length=64, validators=[cv.validate_name])

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented
        if self._get_pk_val() is None and other._get_pk_val() is None:
            return self.username == self.username and\
                   self.telegram_id == other.telegram_id and\
                   self.first_name == other.first_name and \
                   self.last_name == other.last_name
        return self._get_pk_val() == other._get_pk_val()
