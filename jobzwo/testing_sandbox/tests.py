import mock

import responses

from django.conf import settings
from django.test import SimpleTestCase, TestCase, override_settings

from .utils import geocode, rm
from .test_data import geocode_success_response


class RmTest(SimpleTestCase):
    @mock.patch('testing_sandbox.utils.os.path')
    @mock.patch('testing_sandbox.utils.os')
    def test_missing_file(self, mock_os, mock_path):
        mock_path.isfile.return_value = False
        rm('/not/existant')

        self.assertFalse(mock_os.remove.called,
                         "Failed to not remove the file if not present.")

    @mock.patch('testing_sandbox.utils.os.path')
    @mock.patch('testing_sandbox.utils.os')
    def test_success(self, mock_os, mock_path):
        mock_path.isfile.return_value = True
        rm("/exists")
        mock_os.remove.assert_called_with("/exists")


class GeocodeTest(SimpleTestCase):
    @responses.activate
    def test_success(self):
        with responses.RequestsMock() as rsps:
            rsps.add(responses.GET, settings.GOOGLE_GEOCODE_API_URL,
                     body=geocode_success_response, status=200,
                     content_type='application/json')

            retval = geocode('Wien')

            self.assertTrue('status' in retval)
            self.assertEqual('OK', retval['status'])

    @override_settings(GOOGLE_API_KEY='YYYY',
                       GOOGLE_GEOCODE_API_URL='http://not-google.com/api/')
    @mock.patch('testing_sandbox.utils.requests')
    def test_api_key(self, mock_requests):
        mock_requests.json.return_value = {}

        retval = geocode('Wien')

        mock_requests.get.assert_called_with('http://not-google.com/api/',
                                             params={
                                                 'address': 'Wien',
                                                 'key': 'YYYY',
                                             })
