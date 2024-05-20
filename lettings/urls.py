"""
This module defines the URL configurations for the 'lettings' Django application.

It imports the necessary modules and defines a 'urlpatterns' list which routes URLs to views.

Each URL is mapped to a view function in the 'views' module. When Django encounters an incoming
 URL, it checks the 'urlpatterns' list from top to bottom until it finds a matching pattern.
"""


from django.urls import path
from .views import index, letting

urlpatterns = [
    path("", index, name="lettings_index"),
    path("<int:letting_id>/", letting, name="letting"),
]
