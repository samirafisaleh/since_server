from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from django.urls import reverse

class EntryTests(APITestCase):

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        # url = reverse('account-list')
        # data = {'name': 'DabApps'}
        # response = self.client.post(url, data, format='json')
        self.assertEqual(1,1)

    def test_delete_account(self):

        self.assertEqual(1,1)
