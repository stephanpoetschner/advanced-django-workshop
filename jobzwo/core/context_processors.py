# coding: utf-8
from django.conf import settings

from django.contrib.sites.shortcuts import get_current_site


def site_url(request):
    current_site = get_current_site(request)
    current_site.domain

    ctx = {
        'CURRENT_DOMAIN': current_site.domain,
    }
    return ctx


def contact_email(request):
    ctx = {
        'CONTACT_EMAIL': settings.CONTACT_EMAIL
    }
    return ctx
