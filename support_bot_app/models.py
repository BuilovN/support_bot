from django.db import models


class Message(models.Model):
    text = models.TextField()
    telegram_id = models.CharField(max_length=10)
    username = models.CharField(max_length=32)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date = models.DateTimeField()
    is_reply = models.BooleanField()
    checked = models.BooleanField()

    def __eq__(self, other):
        if not isinstance(other, Message):
            return NotImplemented
        if self._get_pk_val() is None and other._get_pk_val() is None:
            return self.text == self.text and\
                   self.telegram_id == other.telegram_id and\
                   self.username == other.username and \
                   self.first_name == other.first_name and \
                   self.last_name == other.last_name and \
                   self.date == other.date and \
                   self.is_reply == other.is_reply and \
                   self.checked == other.checked
        return self._get_pk_val() == other._get_pk_val()
