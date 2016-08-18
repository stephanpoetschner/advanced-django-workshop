# coding: utf-8
import logging

from django.conf import settings


def getLogger(name):
    return logging.getLogger(settings.LOGGING_APPS_PREFIX + name)


class RequireTestingFalse(logging.Filter):
    def filter(self, record):
        return not settings.TESTING

