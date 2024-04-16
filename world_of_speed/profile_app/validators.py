from django.core.exceptions import ValidationError


def username_valid(value):
    for char in value:
        if not char.isalnum() or not char != '_':
            raise ValidationError("Username must contain only letters, digits, and underscores!")
