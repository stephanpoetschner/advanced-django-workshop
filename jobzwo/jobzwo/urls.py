from django.conf import settings
from django.conf.urls import include, url

from jobzwo import views

urlpatterns = [
    url(r'', include('core.urls')),
    
    url(r'^$', views.home, name='home'),
]
