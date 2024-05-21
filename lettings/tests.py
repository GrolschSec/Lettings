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
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TSC'
        )

    def test_address_creation(self):
        self.assertEqual(self.address.number, 123)
        self.assertEqual(self.address.street, 'Test Street')
        self.assertEqual(self.address.city, 'Test City')
        self.assertEqual(self.address.state, 'TS')
        self.assertEqual(self.address.zip_code, 12345)
        self.assertEqual(self.address.country_iso_code, 'TSC')

    def test_address_str(self):
        self.assertEqual(str(self.address), '123 Test Street')

class LettingModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TSC'
        )
        self.letting = Letting.objects.create(
            address=self.address,
            title='Test Letting',
        )

    def test_letting_creation(self):
        self.assertEqual(self.letting.address, self.address)
        self.assertEqual(self.letting.title, 'Test Letting')
    
    def test_letting_str(self):
        self.assertEqual(str(self.letting), 'Test Letting')

class UrlsTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street='Test Street',
            city='Test City',
            state='TS',
            zip_code=12345,
            country_iso_code='TSC'
        )
        self.letting = Letting.objects.create(
            address=self.address,
            title='Test Letting',
        )

    def test_lettings_index_url(self):
        response = self.client.get(reverse('lettings_index'))
        self.assertEqual(response.status_code, 200)

    def test_letting_url(self):
        response = self.client.get(reverse('letting', args=[1]))
        self.assertEqual(response.status_code, 200)

    def test_letting_url_not_found(self):
        response = self.client.get(reverse('letting', args=[100]))
        self.assertEqual(response.status_code, 404)
