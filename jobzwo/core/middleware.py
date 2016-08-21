# coding: utf-8
import uuid

import structlog

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
