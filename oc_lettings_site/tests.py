"""
This module contains the unit tests for the Django application.

Each function in this module is a test case, and should start with the word 'test_'.
The tests can be run using the 'python manage.py test' command.

These tests help ensure the correct functionality of the application by testing its
 individual units of code.
"""

from django.test import TestCase
from django.urls import resolve, reverse
from .views import index


class TestUrls(TestCase):
    def test_index_view_url_resolves_index_view(self):
        view = resolve("/")
        self.assertEqual(view.func, index)


class TestIndexView(TestCase):
    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)


class TestCopyModelData(TestCase):
    pass
