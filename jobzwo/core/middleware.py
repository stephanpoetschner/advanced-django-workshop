# coding: utf-8
import uuid

import structlog

from django.utils import timezone

from core.utils import getLogger
log = getLogger(__name__)


class StructLoggingMiddleware(object):
    def process_request(self, request):
        request.request_id = uuid.uuid4()

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        logger = structlog.getLogger()
        logger.bind(path=request.path, method=request.method,
                    client_ip=ip,
                    request_id=request.request_id)


class ExceptionLoggingMiddleware(object):
    def process_exception(self, request, exception):
        log.exception(str(exception))


class ResponseTimeLoggingMiddleware(object):
    def process_request(self, request):
        request.response_start = timezone.now()

    def process_response(self, request, response):
        request.response_stop = timezone.now()
        processing_time = (request.response_stop - request.response_start)
        msecs = int(processing_time.total_seconds() * 1000.)
        log.info('View processing finished.', timing_ms=msecs)
        return response
