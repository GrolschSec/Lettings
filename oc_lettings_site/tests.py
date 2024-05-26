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
    """
    Test case for the URLs of the application.

    Methods:
        test_index_view_url_resolves_index_view: Tests that the root URL ("/")
        resolves to the index view.
    """

    def test_index_view_url_resolves_index_view(self):
        """
        Test that the root URL ("/") resolves to the index view.

        This test checks if the root URL ("/") correctly resolves to the index view
        by asserting that the function associated with the resolved URL is the index view function.

        Args:
            self (TestUrls): Instance of the test case.

        Raises:
            AssertionError: If the function associated with the resolved URL is
            not the index view function.

        Returns:
            None
        """
        view = resolve("/")
        self.assertEqual(view.func, index)


class TestIndexView(TestCase):
    """
    Test case for the Index View of the application.

    Methods:
        test_index: Tests that the Index View returns a 200 status code.
    """

    def test_index(self):
        """
        Test that the Index View returns a 200 status code.

        This test checks if the Index View is correctly configured
        by asserting that a GET request to the Index View returns a 200 status code.

        Args:
            self (TestIndexView): Instance of the test case.

        Raises:
            AssertionError: If the status code returned by the GET request is not 200.

        Returns:
            None
        """
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
