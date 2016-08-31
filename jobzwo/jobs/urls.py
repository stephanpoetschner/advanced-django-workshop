from django.conf import settings
from django.conf.urls import include, url

from jobs import views


id_patterns = {
    'job_id': r'(?P<job_id>\d{1,50})',
}

urlpatterns = [
    # add/edit
    url(r'^add/$', views.edit, name='jobs_add'),
    url(r'^edit/{job_id}/$'.format(**id_patterns), views.edit,
        name='jobs_edit'),

    # list
    url(r'^$', views.search, name='jobs_search'),
    url(r'^{job_id}/url/$'.format(**id_patterns), views.log_external_url,
        name='jobs_log_external'),

    # json-helpers
    url(r'^json/companies/$', views.json_companies,
        name='jobs_json_companies'),
]
