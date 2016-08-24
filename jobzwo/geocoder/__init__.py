import requests

from django.conf import settings
from django.utils.translation import ugettext as _

from core.utils import getLogger
log = getLogger(__name__)


def geocode(address_string):
    """
    Fetch Latitude/Logitude for address
    https://maps.googleapis.com/maps/api/geocode/json?address=arsenal%2020%208,%20wien,%20austria&key=XXX
    """
    url = settings.GOOGLE_GEOCODE_API_URL
    params = {
        'address': address_string,
        'key': settings.GOOGLE_API_KEY,
    }

    json_response = {}
    try:
        response = requests.get(url,
                                params=params)
        json_response = response.json()
        log.info("geocoding", geocoding_url=url, params=params, 
                 response=json_response)
    except requests.exceptions.RequestException as e:
        log.exception('geocoding failed')

    return json_response
    

