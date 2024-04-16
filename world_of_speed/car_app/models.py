from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.car_app.validators import validate_year
from world_of_speed.profile_app.models import Profile

"""
• Car
    ◦ Image URL
        ▪ A placeholder: "https://..."
    ◦ Owner
        ▪ The ON DELETE constraint must be configured to an appropriate value in alignment with the specified additional tasks.
        ▪ This field should remain hidden in forms.
"""


class Car(models.Model):
    class Type(models.TextChoices):
        RALLY = 'Rally', 'Rally'
        OPEN_WHEEL = 'Open-wheel', 'Open-wheel'
        KART = 'Kart', 'Kart'
        DRAG = 'Drag', 'Drag'
        OTHER = 'Other', 'Other'

    type = models.CharField(
        max_length=10,
        choices=Type.choices,
        blank=False,
        null=False,
    )

    model = models.CharField(
        max_length=15,
        validators=[MinLengthValidator(1),
                    ],
        blank=False,
        null=False,
    )

    year = models.IntegerField(
        blank=False,
        null=False,
        validators=[
                    validate_year,
                    ]

    )

    image_URL = models.URLField(
        unique=True,
        error_messages={'unique': "This image URL is already in use! Provide a new one."},
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[MinValueValidator(0.1,)]
    )

    owner = models.ForeignKey(Profile,
                              on_delete=models.CASCADE)
