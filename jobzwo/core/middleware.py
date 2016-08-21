# coding: utf-8
import uuid

import structlog

from core.utils import getLogger
log = getLogger(__name__)

class StructLoggingMiddleware(object):
    def process_request(self, request):
        request.request_id = uuid.uuid4()

        logger = structlog.getLogger()
        logger.bind(path=request.path, method=request.method,
                    request_id=request.request_id)


class ExceptionLoggingMiddleware(object):
    def process_exception(self, request, exception):
        log.exception(str(exception))
