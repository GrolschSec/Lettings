"""
This module contains the unit tests for the Django application.

Each function in this module is a test case, and should start with the word 'test_'.
The tests can be run using the 'python manage.py test' command.

These tests help ensure the correct functionality of the application by testing its
individual units of code.
"""

from django.test import TestCase
from django.urls import reverse
from .models import Profile
from django.contrib.auth import get_user_model


class ProfileModelTest(TestCase):
    """
    A test case for the Profile model.

    Methods:
        setUp(self): Set up the necessary objects for the tests.
        test_profile_creation(self): Test the creation of a profile.
        test_profile_str(self): Test the string representation of a profile.
    """

    def setUp(self):
        self.user = get_user_model().objects.create(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profile_creation(self):
        """
        Test the creation of a profile.

        This test checks if a profile is correctly created by asserting that the user
         and favorite city of the created profile match the expected user and favorite city.

        Args:
            self (ProfileTest): Instance of the test case.

        Raises:
            AssertionError: If the user or favorite city of the created profile do not
            match the expected values.

        Returns:
            None
        """
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.favorite_city, "Test City")

    def test_profile_str(self):
        """
        Test the string representation of a profile.

        This test checks if the string representation of a profile is correctly
        implemented by asserting that the string representation of the profile matches
        the expected string.

        Args:
            self (ProfileTest): Instance of the test case.

        Raises:
            AssertionError: If the string representation of the profile does not match
             the expected string.

        Returns:
            None
        """
        self.assertEqual(str(self.profile), "testuser")


class UrlsTest(TestCase):
    """
    Test case for the URLs of the Profile app.

    Methods:
        setUp: Sets up the test environment.
        test_profiles_index_url: Tests the profiles index URL.
        test_profile_url: Tests the profile URL for a valid user.
        test_profile_url_invalid: Tests the profile URL for an invalid user.
    """

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profiles_index_url(self):
        """
        Test the profiles index URL.

        This test checks if the profiles index URL is correctly implemented by asserting
        that a GET request to the profiles index URL returns a 200 status code.

        Args:
            self (UrlsTest): Instance of the test case.

        Raises:
            AssertionError: If the status code returned by the GET request is not 200.

        Returns:
            None
        """
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)

    def test_profile_url(self):
        """
        Test the testuser's profile index URL.

        This test checks if the testuser's profile URL is correctly implemented by asserting
        that a GET request to the profile URL returns a 200 status code.

        Args:
            self (UrlsTest): Instance of the test case.

        Raises:
            AssertionError: If the status code returned by the GET request is not 200.

        Returns:
            None
        """
        response = self.client.get(reverse("profile", args=["testuser"]))
        self.assertEqual(response.status_code, 200)

    def test_profile_url_invalid(self):
        """
        Test the profile URL for an invalid user.

        This test checks if the profile URL for an invalid user is correctly implemented
        by asserting that a GET request to the profile URL for an invalid user
        returns a 404 status code.

        Args:
            self (UrlsTest): Instance of the test case.

        Raises:
            AssertionError: If the status code returned by the GET request is not 404.

        Returns:
            None
        """
        response = self.client.get(reverse("profile", args=["invaliduser"]))
        self.assertEqual(response.status_code, 404)


class IndexViewTest(TestCase):
    """
    Test case for the index view of the Profile app.

    Methods:
        setUp: Sets up the test environment.
        test_index_view: Tests that the index view displays the username of a profile
        when a profile exists.
        test_index_view_no_profiles: Tests that the index view displays a specific
         message when no profiles exist.
    """

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_index_view(self):
        """
        Test that the index view displays the username of a profile when a profile exists.

        This test checks if the index view correctly displays the username of a profile
         when a profile exists by asserting that a GET request to the index view contains
         the username of the created profile.

        Args:
            self (IndexViewTest): Instance of the test case.

        Raises:
            AssertionError: If the response of the GET request does not contain
             the username of the created profile.

        Returns:
            None
        """
        response = self.client.get(reverse("profiles_index"))
        self.assertContains(response, "testuser")

    def test_index_view_no_profiles(self):
        """
        Test that the index view displays a specific message when no profiles exist.

        This test checks if the index view correctly displays a specific message when
        no profiles exist by asserting that a GET request to the index view contains
        the message "No profiles are available."

        Args:
            self (IndexViewTest): Instance of the test case.

        Raises:
            AssertionError: If the response of the GET request does not contain the
            message "No profiles are available."

        Returns:
            None
        """
        Profile.objects.all().delete()
        response = self.client.get(reverse("profiles_index"))
        self.assertContains(response, "No profiles are available.")


class ProfileViewTest(TestCase):
    """
    Test case for the profile view of the Profile app.

    Methods:
        setUp: Sets up the test environment.
        test_profile_view: Tests that the profile view displays the username of a
        valid profile.
        test_profile_view_invalid: Tests that the profile view returns a 404 status
        code for an invalid profile.
    """

    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profile_view(self):
        """
        Test that the profile view displays the username of a valid profile.

        This test checks if the profile view correctly displays the username of a valid profile
        by asserting that a GET request to the profile view contains
        the username of the created profile.

        Args:
            self (ProfileViewTest): Instance of the test case.

        Raises:
            AssertionError: If the response of the GET request does not contain the username
            of the created profile.

        Returns:
            None
        """
        response = self.client.get(reverse("profile", args=["testuser"]))
        self.assertContains(response, "testuser")

    def test_profile_view_invalid(self):
        """
        Test that the profile view returns a 404 status code for an invalid profile.

        This test checks if the profile view correctly handles an invalid profile
        by asserting that a GET request to the profile view with an invalid username
        returns a 404 status code.

        Args:
            self (ProfileViewTest): Instance of the test case.

        Raises:
            AssertionError: If the status code returned by the GET request is not 404.

        Returns:
            None
        """
        response = self.client.get(reverse("profile", args=["invaliduser"]))
        self.assertEqual(response.status_code, 404)
