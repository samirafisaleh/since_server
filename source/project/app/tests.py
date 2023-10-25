from django.urls import reverse
from rest_framework import status



# pylint: disable=import-error
"""[Placeholder module docstring]"""
from django.test import TestCase
from rest_framework.test import APITestCase

class EntryTests(APITestCase):
    """ [Template docstring] """


    ######################################################
    #
    #
    #
    #
    ######################################################
    def test_entry_create_no_title(self):
        """ [Template function docstring] """
        data = {}
        response = self.client.post('/entry/', data, format='json')
        self.assertEqual("title" in response.data, True)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_entry_create_title_whitespace_only(self):
        """ [Template function docstring] """
        data = {'title' : '   '}
        response = self.client.post('/entry/', data, format='json')

        self.assertEqual("title" in response.data, True)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)


    # def test_entry_create_date_of_interest_invalid_date(self):
    #     """ [Template function docstring] """
    #     self.assertEqual(1, 1)

    def test_entry_create(self):
        """ [Template function docstring] """
        data = {'title': 'DabApps'}
        response = self.client.post('/entry/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    ######################################################
    #
    #
    #
    #
    ######################################################
    def test_entry_retrieve_id_non_int(self):
        """ [Template function docstring] """
        response = self.client.get(f'/entry/test/?', format='json')

        self.assertEqual('message' in response.data, True)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_entry_retrieve_id_dne(self):
        """ [Template function docstring] """
        response = self.client.get(f'/entry/12/?', format='json')

        self.assertEqual('message' in response.data, True)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)


    def test_entry_retrieve(self):
        """ [Template function docstring] """

        data = {'title': 'DabApps'}
        response = self.client.post('/entry/', data, format='json')
        id = response.data['data']['id']

        response = self.client.get(f'/entry/{id}/?', format='json')

        self.assertEqual("data" in response.data, True)
        self.assertEqual('id' in response.data['data'], True)
        self.assertEqual('title' in response.data['data'], True)
        self.assertEqual('description' in response.data['data'], True)
        self.assertEqual('datetime_of_interest' in response.data['data'], True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    ######################################################
    #
    #
    #
    #
    ######################################################
    def test_entry_list(self):
        """ [Template function docstring] """

        response = self.client.get(f'/entry/?', format='json')

        self.assertEqual(isinstance(response.data, list), True)




    ######################################################
    #
    #
    #
    #
    ######################################################
    def test_entry_delete_id_notprovided(self):
        """ [Template function docstring] """
        response = self.client.delete(f'/entry/', format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    # def test_entry_delete_id_non_int(self):
    #     """ [Template function docstring] """
    #     self.assertEqual(1, 1)

    # def test_entry_delete_id_dne(self):
    #     """ [Template function docstring] """
    #     self.assertEqual(1, 1)



    def test_entry_delete(self):
        """ [Template function docstring] """
        data = {'title': 'DabApps'}
        response = self.client.post('/entry/', data, format='json')
        id = response.data['data']['id']

        response = self.client.delete(f'/entry/{id}/', format='json')
        self.assertEqual('message' in response.data, True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


