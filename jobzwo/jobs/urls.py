from django.conf import settings
from django.conf.urls import include, url

from jobs import views

urlpatterns = [
    url(r'^$', views.query, name='jobs_query'),
]

