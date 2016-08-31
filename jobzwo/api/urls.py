from django.conf import settings
from django.conf.urls import include, url

from rest_framework import routers

from .views import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    # restframework browsable-api
    url(r'^api-auth/', include('rest_framework.urls', 
                               namespace='rest_framework'))
]


