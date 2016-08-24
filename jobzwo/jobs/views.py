from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from .decorators import apply_jobs
from .forms import JobForm, SearchForm
from .models import Job

from core.utils import getLogger
log = getLogger(__name__)


@apply_jobs
def edit(request, jobs, job_id=None):
    job = None
    if job_id:
        try:
            job = jobs.get(id=job_id)
        except Job.DoesNotExist:
            raise Http404

    form = JobForm(request.POST or None,
                   instance=job)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('jobs_search'))

    return render(request, 'jobs/edit.html', {
        'add_form': form,
    })


@apply_jobs
def search(request, jobs):
    jobs = jobs.order_by('-updated')

    form = SearchForm(request.GET or None)
    if form.is_valid():
        jobs = form.search(jobs)

    return render(request, 'jobs/listing.html', {
        'jobs': jobs,
        'search_form': form,
    })


@apply_jobs
def log_external_url(request, jobs, job_id):
    try:
        job = jobs.get(id=job_id)
    except Job.DoesNotExist:
        raise Http404

    log.info('External-link clicked', job=job)

    return HttpResponseRedirect(job.external_url)
