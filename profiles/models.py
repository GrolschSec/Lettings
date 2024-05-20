"""
This module defines the data models for the 'profiles' application.

Each class in this module represents a Django model, which is a single database table. 
Each attribute of the class represents a field of the table.

"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    This class represents the 'Profile' model for the 'profiles' application.

    Each instance of this class represents a single user profile, with a one-to-one relationship with a 'User' and a field for the user's favorite city.

    """

    class Meta:
        """
        This inner class defines metadata for the 'Profile' model.

        It changes the verbose name plural to "Profiles" to correctly represent multiple instances of the 'Profile' model.
        """

        verbose_name_plural = "Profiles"

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        This method returns a string representation of the 'Profile' model instance.
        """
        return self.user.username
