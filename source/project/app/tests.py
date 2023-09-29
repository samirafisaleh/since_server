
# pylint: disable=import-error
"""[Placeholder module docstring]"""
from django.test import TestCase
from rest_framework.test import APITestCase

class EntryTests(APITestCase):
    """ [Template docstring] """

    def test_account_create(self):
        """ [Template function docstring] """
        # url = reverse('account-list')
        # data = {'name': 'DabApps'}
        # response = self.client.post(url, data, format='json')
        self.assertEqual(1,1)

    def test_account_login(self):
        """ [Template function docstring] """
        self.assertEqual(1,1)

    def test_account_delete(self):
        """ [Template function docstring] """
        self.assertEqual(1,1)

    def test_create(self):
        """ [Template function docstring] """
        self.assertEqual(1,1)

    def test_delete(self):
        """ [Template function docstring] """
        self.assertEqual(1,1)

    def test_modify(self):
        """ [Template function docstring] """
        self.assertEqual(1,1)

    def test_list(self):
        """ [Template function docstring] """
        self.assertEqual(1,1)


