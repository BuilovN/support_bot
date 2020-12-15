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
