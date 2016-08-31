import mock

from django.test import SimpleTestCase, TestCase

from .utils import rm


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
