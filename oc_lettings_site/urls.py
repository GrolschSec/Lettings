"""
This module defines the URL configurations for the 'oc_lettings_site' Django application.

It imports the necessary modules and defines a 'urlpatterns' list which routes URLs to views.

Each URL is mapped to a view function in the 'views' module. When Django encounters an
incoming URL, it checks the 'urlpatterns' list from top to bottom until it finds a
matching pattern.
"""

from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path("admin/", admin.site.urls),
]
