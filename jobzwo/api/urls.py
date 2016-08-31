from django.conf import settings
from django.conf.urls import include, url

from .views import CompanyView

urlpatterns = [
    url(r'^companies/', CompanyView.as_view(), name='api_companies'),

    # restframework browsable-api
    url(r'^api-auth/', include('rest_framework.urls', 
                               namespace='rest_framework'))
]


