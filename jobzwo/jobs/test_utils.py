from datetime import date, timedelta

import mock

from django.conf import settings
from django.test import TestCase, override_settings

from .utils import send_mail, sanitize_datespan

class SanitizeTimespanTest(TestCase):
    def test_basic(self):
        with self.assertRaises(ValueError):
            sanitize_datespan(None, None)

        with self.assertRaises(ValueError):
            sanitize_datespan('2014-10-30', None)

        with self.assertRaises(ValueError):
            sanitize_datespan(None, '2014-10-30')


        with self.assertRaises(ValueError):
            sanitize_datespan('xxxxx', '2014-10-30')

        with self.assertRaises(ValueError):
            sanitize_datespan('2014-10-30', 'xxxxx')

        self.assertEqual(
            (date(2014, 10, 30), date(2014, 10, 30)),
            sanitize_datespan('2014-10-30', '2014-10-30')
        )

    def test_order(self):
        """
        raise Exception, when `to` is less than `since`
        """
        with self.assertRaises(ValueError):
            sanitize_datespan('2014-10-30', '2014-10-25')


    def test_max_span(self):
        """
        raise Exception, when `max_days` is set.
        """
        self.assertEqual(
            (date(2014, 10, 25), date(2014, 10, 30)),
            sanitize_datespan('2014-10-25', '2014-10-30', max_days=10)
        )

        with self.assertRaises(ValueError):
            sanitize_datespan('2014-10-25', '2014-10-30', max_days=1)


class SendMailTest(TestCase):
    @override_settings(EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend')
    @mock.patch('jobs.utils.EmailMultiAlternatives')
    def test_success(self, mock_email_alternatives):
        mail = mock.MagicMock()
        mail.attach_alternative.return_value = None
        mail.send.return_value = None

        mock_email_alternatives.return_value = mail

        send_mail(subject='test-subject',
                  message='test-message',
                  from_email=None,
                  reply_to=None,
                  recipient_list=['tech@wifitiger.com', ],
                  html_message='test-html-message')

