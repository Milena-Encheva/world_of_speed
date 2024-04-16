from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speed.profile_app.validators import username_valid


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 3
    AGE_MIN_VALUE = 21

    username = (models.CharField
                (max_length=USERNAME_MAX_LENGTH,
                 validators=[MinLengthValidator(USERNAME_MIN_LENGTH,
                                                "Username must be at least 3 chars long!"),
                             username_valid],
                 )
                )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.IntegerField(
        validators=[
            MinValueValidator(AGE_MIN_VALUE, 'Age requirement: 21 years and above.')
        ],
        blank=False,
        null=False,
    )

    password = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=25,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    def total_car_price(self):
        """
        Calculate the total price of all cars owned by the user.
        """
        return sum(car.price for car in self.car_set.all())

