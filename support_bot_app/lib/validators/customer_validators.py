from django.core.exceptions import ValidationError


def validate_telegram_id(value):
    value = str(value)
    if not value.isdigit() or len(value) > 10:
        raise ValidationError('Incorrect telegram_id value')


def validate_name(value):
    value = str(value)
    if not value.isalpha() or len(value) > 64:
        raise ValidationError('Incorrect name')


def validate_username(value):
    value = str(value)
    if len(value) > 32:
        raise ValidationError('Incorrect username')