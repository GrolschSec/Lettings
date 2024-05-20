"""
This module defines the data models for the 'lettings' application.

Each class in this module represents a Django model, which is a single database table. 
Each attribute of the class represents a field of the table.

"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    This class represents the 'Address' model for the 'lettings' application.

    Each instance of this class represents a single address, with fields for number, street, city, state, zip code, and country ISO code.

    """

    class Meta:
        """
        This inner class defines metadata for the 'Address' model.

        It changes the verbose name plural to "Addresses" to correctly represent multiple instances of the 'Address' model.
        """

        verbose_name_plural = "Addresses"

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """
        This method returns a string representation of the 'Address' model instance.
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    This class represents the 'Letting' model for the 'lettings' application.

    Each instance of this class represents a single letting, with fields for title and a one-to-one relationship with an 'Address'.

    """

    class Meta:
        """
        This inner class defines metadata for the 'Letting' model.

        It changes the verbose name plural to "Lettings" to correctly represent multiple instances of the 'Letting' model.
        """

        verbose_name_plural = "Lettings"

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        This method returns a string representation of the 'Letting' model instance.
        """
        return self.title
