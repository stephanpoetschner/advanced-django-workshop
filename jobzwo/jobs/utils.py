from datetime import date, timedelta

from django.utils import timezone, dateparse

def sanitize_datespan(since, to, max_days=None, parse_date=None):
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

