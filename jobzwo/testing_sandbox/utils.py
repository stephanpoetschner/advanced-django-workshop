import os
import os.path

import requests

from django.conf import settings

from .exceptions import GeocodeError


def rm(filename):
    if os.path.isfile(filename):
        os.remove(filename)


def geocode(address_string):
    url = settings.GOOGLE_GEOCODE_API_URL
    params = {
        'address': address_string,
        'key': settings.GOOGLE_API_KEY,
    }

    json_response = {}
    try:
        response = requests.get(url, params=params)
        json_response = response.json()
    except (ValueError, requests.exceptions.RequestException) as e:
        raise GeocodeError(e)

    return json_response
