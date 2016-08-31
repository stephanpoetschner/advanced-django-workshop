# coding: utf-8
import logging

import structlog

from django.conf import settings


def getLogger(name):
    return structlog.getLogger(settings.LOGGING_PREFIX + name)


class RequireTestingFalse(logging.Filter):
    def filter(self, record):
        return not settings.TESTING
