from django.shortcuts import render

from .models import Job

def query(request, jobs):
    jobs = Job.objects.only_active()

    return render(request, 'jobs/listing.html', {
        'jobs': jobs,
    })
