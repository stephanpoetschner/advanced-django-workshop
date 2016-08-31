from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    url(r'', include('core.urls')),
    url(r'api/', include('api.urls')),
    url(r'', include('jobs.urls')),
]
