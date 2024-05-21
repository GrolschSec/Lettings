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
    def setUp(self):
        self.user = get_user_model().objects.create(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profile_creation(self):
        self.assertEqual(self.profile.user, self.user)
        self.assertEqual(self.profile.favorite_city, "Test City")

    def test_profile_str(self):
        self.assertEqual(str(self.profile), "testuser")


class UrlsTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profiles_index_url(self):
        response = self.client.get(reverse("profiles_index"))
        self.assertEqual(response.status_code, 200)

    def test_profile_url(self):
        response = self.client.get(reverse("profile", args=["testuser"]))
        self.assertEqual(response.status_code, 200)

    def test_profile_url_invalid(self):
        response = self.client.get(reverse("profile", args=["invaliduser"]))
        self.assertEqual(response.status_code, 404)


class IndexViewTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_index_view(self):
        response = self.client.get(reverse("profiles_index"))
        self.assertContains(response, "testuser")

    def test_index_view_no_profiles(self):
        Profile.objects.all().delete()
        response = self.client.get(reverse("profiles_index"))
        self.assertContains(response, "No profiles are available.")


class ProfileViewTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="testuser", password="testpassword"
        )
        self.profile = Profile.objects.create(user=self.user, favorite_city="Test City")

    def test_profile_view(self):
        response = self.client.get(reverse("profile", args=["testuser"]))
        self.assertContains(response, "testuser")

    def test_profile_view_invalid(self):
        response = self.client.get(reverse("profile", args=["invaliduser"]))
        self.assertEqual(response.status_code, 404)
