from django.conf import settings
from django.conf.urls import include, url


urlpatterns = [
    # restframework browsable-api
    url(r'^api-auth/', include('rest_framework.urls', 
                               namespace='rest_framework'))
]


