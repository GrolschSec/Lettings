"""
This module contains the Django application configuration for the project.

It defines an AppConfig class that contains the application's configuration settings.
This class is used by Django to initialize the application and its components.

Each Django application should have an apps.py module with a derived AppConfig class.
"""

from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    """
    This class contains the configuration for the 'profiles' application.

    It inherits from Django's AppConfig class and overrides the 'name' attribute with the name of the application.

    Django uses this configuration when initializing the 'profiles' application.
    """

    name = "profiles"
