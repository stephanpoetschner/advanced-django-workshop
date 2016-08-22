from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .decorators import apply_jobs
from .models import Job

from core.utils import getLogger
log = getLogger(__name__)


@apply_jobs
def query(request, jobs):
    return render(request, 'jobs/listing.html', {
        'jobs': jobs,
    })


@apply_jobs
def log_mail(request, jobs, job_id):
    try:
        job = jobs.get(id=job_id)
    except Job.DoesNotExist:
        raise Http404

    log.info('Email-link clicked', job=job)

    return HttpResponseRedirect('mailto:' + job.contact_email)


@apply_jobs
def log_external_url(request, jobs, job_id):
    try:
        job = jobs.get(id=job_id)
    except Job.DoesNotExist:
        raise Http404

    log.info('External-link clicked', job=job)

    return HttpResponseRedirect(job.external_url)
