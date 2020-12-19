from django.core.exceptions import ValidationError
from datetime import datetime as dt

def validate_text(value):
    value = str(value)
    if len(value) == 0:
        raise ValidationError("Empty text")


def validate_date(value):
    value = str(value)
    try:
        dt.strptime(value, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise ValidationError("Incorrect data format, should be YYYY-MM-DD HH:MM:SS")


def validate_boolean(value):
    if type(value) is not bool:
        raise ValidationError("Incorrect type")