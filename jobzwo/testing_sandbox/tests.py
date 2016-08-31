import mock

from django.test import SimpleTestCase, TestCase

from .utils import rm


class RmTest(SimpleTestCase):
    @mock.patch('testing_sandbox.utils.os')
    def test_success(self, mock_os):
        rm('/not/existant')

        mock_os.remove.assert_called_with("/not/existant")
