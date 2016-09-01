from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView
from django.db.models import Q
from .decorators import apply_jobs
from .models import Job
from .forms import JobForm
import operator

from core.utils import getLogger
log = getLogger(__name__)



@apply_jobs
def query(request, jobs):
    return render(request, 'jobs/listing.html', {
        'jobs': jobs,
    })


@apply_jobs
def log_external_url(request, jobs, job_id):
    try:
        job = jobs.get(id=job_id)
    except Job.DoesNotExist:
        raise Http404

    log.info('External-link clicked', job=job)

    return HttpResponseRedirect(job.external_url)

class JobCreate(CreateView):
    model = Job
    form_class = JobForm

class JobList(ListView):
    model = Job
    template_name = 'jobs/listing.html'
    context_object_name = 'job'

    def get_queryset(self):
        result = super(JobList, self).get_queryset()

        query = self.request.GET.get('q')
        if query:
            result = result.filter(title__icontains=query)

        return result

