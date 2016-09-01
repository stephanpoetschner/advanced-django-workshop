from django.core.urlresolvers import reverse
from django.db import models

from impairments.models import AbstractImpairmentJob

from .mixins import JobStatusTransitionMixin
from .querysets import JobManager
from django.core.urlresolvers import reverse



class Job(JobStatusTransitionMixin, AbstractImpairmentJob):
    title = models.CharField(max_length=254)
    description = models.TextField()

    location = models.CharField(max_length=254)

    external_url = models.URLField()
    contact_email = models.EmailField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=254,
                              choices=JobStatusTransitionMixin.CHOICES_STATUS, default=JobStatusTransitionMixin.STATUS_DRAFT)

    objects = JobManager()

    def __str__(self):
        return ", ".join([
            str(self.id) or '-',
            self.title or '-',
        ])

    def contact_mail_link(self):
        return 'mailto:{}'.format(self.contact_email)

    def get_log_external_url(self):
        return reverse('jobs_log_external', kwargs={'job_id': self.id, })

    def get_absolute_url(self):
        return reverse('jobs_query')

