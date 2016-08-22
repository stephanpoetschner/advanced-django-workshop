from django.shortcuts import render

from .decorators import apply_jobs
from .models import Job


@apply_jobs
def query(request, jobs):
    return render(request, 'jobs/listing.html', {
        'jobs': jobs,
    })
