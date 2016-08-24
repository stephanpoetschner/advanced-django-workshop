from django.conf import settings
from django.conf.urls import include, url

from jobs import views

id_patterns = {
    'job_id': r'(?P<job_id>\d{1,50})',
}

urlpatterns = [
    url(r'^add/$', views.edit, name='jobs_edit'),
    url(r'^edit/{job_id}/$'.format(**id_patterns), views.edit, name='jobs_edit'),

    url(r'^$', views.query, name='jobs_query'),

    url(r'^{job_id}/url/$'.format(**id_patterns), views.log_external_url,
        name='jobs_log_external'),
]

