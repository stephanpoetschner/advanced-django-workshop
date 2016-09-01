from django.conf import settings
from django.conf.urls import include, url

from . import views


urlpatterns = [
    #url(r'^$', views.query, name='jobs_query'),
    url(r'^$', views.JobList.as_view(), name='jobs_query'),

    url(r'^(?P<job_id>\d{1,50})/url/$', views.log_external_url,
        name='jobs_log_external'),

    url(r'add/$', views.JobCreate.as_view(), name='job-add'),
]

