# coding: utf-8
from django.http import Http404
from django.core.exceptions import PermissionDenied

from core.utils import getLogger
log = getLogger(__name__)


def raise400(request):
    raise Http404("404 – Not found")


def raise403(request):
    raise PermissionDenied("403 – Not allowed")


def raise500(request):
    raise Exception("500 – Server Error")
