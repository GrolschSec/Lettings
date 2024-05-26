"""
This module contains the unit tests for the Django application.

Each function in this module is a test case, and should start with the word 'test_'.
The tests can be run using the 'python manage.py test' command.

These tests help ensure the correct functionality of the application by testing its individual
 units of code.
"""

from django.test import TestCase
from django.urls import reverse
from .models import Address, Letting


class AddressModelTest(TestCase):
    """
    Test case for the Address model of the application.

    Methods:
        setUp: Sets up the test environment.
        test_address_creation: Tests that the Address instance is correctly created
        with the provided details.
        test_address_str: Tests that the string representation of the Address instance
        is correctly formatted.
    """

    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TSC",
        )

    def test_address_creation(self):
        """
        Test that the Address instance is correctly created with the provided details.

        This test checks if the Address instance is correctly created with the provided details
        by asserting that the attributes of the created Address instance match
        the provided details.

        Args:
            self (AddressModelTest): Instance of the test case.

        Raises:
            AssertionError: If the attributes of the created Address instance do not match
            the provided details.

        Returns:
            None
        """
        self.assertEqual(self.address.number, 123)
        self.assertEqual(self.address.street, "Test Street")
        self.assertEqual(self.address.city, "Test City")
        self.assertEqual(self.address.state, "TS")
        self.assertEqual(self.address.zip_code, 12345)
        self.assertEqual(self.address.country_iso_code, "TSC")

    def test_address_str(self):
        """
        Test that the string representation of the Address instance is correctly formatted.

        This test checks if the string representation of the Address instance is correctly
        formatted by asserting that the string representation of the created Address
        instance matches the expected format.

        Args:
            self (AddressModelTest): Instance of the test case.

        Raises:
            AssertionError: If the string representation of the created Address instance
            does not match the expected format.

        Returns:
            None
        """
        self.assertEqual(str(self.address), "123 Test Street")


class LettingModelTest(TestCase):
    """
    Test case for the Letting model of the application.

    Methods:
        setUp: Sets up the test environment.
        test_letting_creation: Tests that the Letting instance is correctly created with
        the provided details.
        test_letting_str: Tests that the string representation of the Letting instance
        is correctly formatted.
    """

    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TSC",
        )
        self.letting = Letting.objects.create(
            address=self.address,
            title="Test Letting",
        )

    def test_letting_creation(self):
        """
        Test that the Letting instance is correctly created with the provided details.

        This test checks if the Letting instance is correctly created with the provided
        details by asserting that the attributes of the created Letting instance match
        the provided details.

        Args:
            self (LettingModelTest): Instance of the test case.

        Raises:
            AssertionError: If the attributes of the created Letting instance do not
            match the provided details.

        Returns:
            None
        """
        self.assertEqual(self.letting.address, self.address)
        self.assertEqual(self.letting.title, "Test Letting")

    def test_letting_str(self):
        """
        Test that the string representation of the Letting instance is correctly formatted.

        This test checks if the string representation of the Letting instance is
        correctly formatted by asserting that the string representation of the created
        Letting instance matches the expected format.

        Args:
            self (LettingModelTest): Instance of the test case.

        Raises:
            AssertionError: If the string representation of the created Letting instance
            does not match the expected format.

        Returns:
            None
        """
        self.assertEqual(str(self.letting), "Test Letting")


class UrlsTest(TestCase):
    """
    Test case for the URLs of the application.

    Methods:
        setUp: Sets up the test environment.
        test_lettings_index_url: Tests that the lettings index URL returns a 200 status code.
        test_letting_url: Tests that the letting URL returns a 200 status code for a valid letting.
    """

    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TSC",
        )
        self.letting = Letting.objects.create(
            address=self.address,
            title="Test Letting",
        )

    def test_lettings_index_url(self):
        """
        Test that the lettings index URL returns a 200 status code.

        This test checks if the lettings index URL is correctly configured
        by asserting that a GET request to the lettings index URL returns a 200 status code.

        Args:
            self (UrlsTest): Instance of the test case.

        Raises:
            AssertionError: If the status code returned by the GET request is not 200.

        Returns:
            None
        """
        response = self.client.get(reverse("lettings_index"))
        self.assertEqual(response.status_code, 200)

    def test_letting_url(self):
        """
        Test that the letting URL returns a 200 status code for a valid letting.

        This test checks if the letting URL is correctly configured
        by asserting that a GET request to the letting URL with a valid letting
        ID returns a 200 status code.

        Args:
            self (UrlsTest): Instance of the test case.

        Raises:
            AssertionError: If the status code returned by the GET request is not 200.

        Returns:
            None
        """
        response = self.client.get(reverse("letting", args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_letting_url_not_found(self):
        """
        Test that the letting URL returns a 404 status code for an invalid letting.

        This test checks if the letting URL correctly handles an invalid letting
        by asserting that a GET request to the letting URL with an invalid letting
        ID returns a 404 status code.

        Args:
            self (UrlsTest): Instance of the test case.

        Raises:
            AssertionError: If the status code returned by the GET request is not 404.

        Returns:
            None
        """
        response = self.client.get(reverse("letting", args=[100]))
        self.assertEqual(response.status_code, 404)


class IndexViewTest(TestCase):
    """
    Test case for the Index View of the application.

    Methods:
        setUp: Sets up the test environment.
        test_index_view_status_code: Tests that the Index View returns a 200 status code.
        test_index_view_lettings_list: Tests that the Index View correctly displays
        the list of lettings.
    """

    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TSC",
        )
        self.letting = Letting.objects.create(
            address=self.address,
            title="Test Letting",
        )

    def test_index_view(self):
        """
        Test that the Index View correctly displays the list of lettings.

        This test checks if the Index View correctly displays the list of lettings
        by asserting that the 'lettings_list' context variable of the response matches
        the expected queryset.

        Args:
            self (IndexViewTest): Instance of the test case.

        Raises:
            AssertionError: If the 'lettings_list' context variable of the response
            does not match the expected queryset.

        Returns:
            None
        """
        response = self.client.get(reverse("lettings_index"))
        self.assertQuerysetEqual(
            response.context["lettings_list"], ["<Letting: Test Letting>"]
        )

    def test_index_no_lettings(self):
        """
        Test that the Index View correctly handles an empty list of lettings.

        This test checks if the Index View correctly handles an empty list of lettings
        by asserting that the 'lettings_list' context variable of the response is an
        empty list when all Letting instances are deleted.

        Args:
            self (IndexViewTest): Instance of the test case.

        Raises:
            AssertionError: If the 'lettings_list' context variable of the response
            is not an empty list.

        Returns:
            None
        """
        Letting.objects.all().delete()
        response = self.client.get(reverse("lettings_index"))
        self.assertQuerysetEqual(response.context["lettings_list"], [])


class LettingViewTest(TestCase):
    """
    Test case for the Letting View of the application.

    Methods:
        setUp: Sets up the test environment.
        test_letting_view: Tests that the Letting View returns a 200 status
        code for a valid letting and correctly displays the details of a letting.
    """

    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Test Street",
            city="Test City",
            state="TS",
            zip_code=12345,
            country_iso_code="TSC",
        )
        self.letting = Letting.objects.create(
            address=self.address,
            title="Test Letting",
        )

    def test_letting_view(self):
        """
        Test that the Letting View returns a 200 status code for a valid letting and
        correctly displays the details of a letting.

        This test checks if the Letting View correctly displays the details of a letting
        by asserting that the response contains the title and address of the letting.

        Args:
            self (LettingViewTest): Instance of the test case.

        Raises:
            AssertionError: If the response does not contain the title and address of the letting.

        Returns:
            None
        """
        response = self.client.get(reverse("letting", args=[1]))
        self.assertContains(response, "Test Letting")
        self.assertContains(response, "123 Test Street")

    def test_letting_not_found(self):
        """
        Test that the Letting View returns a 404 status code for an invalid letting.

        This test checks if the Letting View correctly handles an invalid letting
        by asserting that a GET request to the Letting View with an invalid letting
        ID returns a 404 status code.

        Args:
            self (LettingViewTest): Instance of the test case.

        Raises:
            AssertionError: If the status code returned by the GET request is not 404.

        Returns:
            None
        """
        response = self.client.get(reverse("letting", args=[100]))
        self.assertEqual(response.status_code, 404)
