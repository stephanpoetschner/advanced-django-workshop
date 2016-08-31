from django.test import TestCase


class ListingTest(TestCase):
    def test_success(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)


class JsonCompaniesTest(TestCase):
    def test_success(self):
        response = self.client.get('/json/companies/')
        self.assertEqual(200, response.status_code)
