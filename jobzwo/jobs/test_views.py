from django.test import TestCase


class ListingTest(TestCase):
    def test_success(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
