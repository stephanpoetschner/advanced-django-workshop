from datetime import date, timedelta

from django.conf import settings
from django.core.mail.message import EmailMultiAlternatives
from django.utils import timezone, dateparse

from core.utils import getLogger
log = getLogger(__name__)

def sanitize_datespan(since, to, max_days=None, parse_date=None):
    """
    given two dates (as strings) return two valid date-objects or
    raise ValueError.

    sanitize_datespan('2014-10-30', '2014-10-30')
    """
    if not parse_date:
        parse_date = dateparse.parse_date

    since = since or u''
    to = to or u''
    args = (since.strip(), to.strip())
    for arg in args:
        if arg is None:
            raise ValueError('Argument `{}` must not be `None`.'.format(arg))

    args = map(lambda arg: parse_date(arg) \
               if not isinstance(arg, date) \
               else arg,
               args)

    for arg, orig_value in zip(args, (since, to)):
        if arg is None:
            raise ValueError(
                'Argument `{}` ({}) is not a valid string (YYYY-MM-DD).' \
                .format(arg, orig_value))

    since, to = args
    if to < since:
        raise ValueError('Argument `to` must not be less than `since`.')

    if max_days and (to - since) > timedelta(days=max_days):
        raise ValueError('`since` and `to` must span a maximum of {} days '
                         '(Spanning {} days).'.format(max_days,
                                                      (to - since).days))

    return tuple(args)


def send_mail(subject, message, from_email=None, reply_to=None,
              recipient_list=None, html_message=None):
    """
    send html email, instead of plain-text.
    """

    if not recipient_list:
        return

    if not from_email:
        from_email = settings.CONTACT_EMAIL

    mail = EmailMultiAlternatives(subject, message, from_email, recipient_list,
                                  reply_to=reply_to)
    if html_message:
        mail.attach_alternative(html_message, 'text/html')

    log.info('Sending email',
             from_email=from_email,
             recipients=recipient_list,
             subject=subject)

    return mail.send()
