# coding: utf-8
from core.utils import getLogger
log = getLogger(__name__)




class ExceptionLoggingMiddleware(object):
    def process_exception(self, request, exception):
        log.exception(exception)