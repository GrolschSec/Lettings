"""
This module defines the admin interface configurations for the Django application.

It imports the models from the models module and registers them with the admin site using
the admin.site.register function.

This allows the admin site to have access to the models, enabling it to perform CRUD operations
 on them.
"""

from django.contrib import admin

from .models import Letting
from .models import Address

admin.site.register(Letting)
admin.site.register(Address)
