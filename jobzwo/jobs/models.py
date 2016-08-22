from django.db import models

from impairments.models import AbstractImpairmentJob

JOB_STATUS = (
    ('DRAFT', 'Draft'),
    ('ACTIVE', 'Active'),
    ('INACTIVE', 'Inactive'),
)

class Job(AbstractImpairmentJob):
    title = models.CharField(max_length=254)
    description = models.TextField()

    location = models.CharField(max_length=254)

    external_url = models.URLField()
    contact_email = models.EmailField()

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    status = models.CharField(max_length=254, choices=JOB_STATUS)

    def __str__(self):
        return ", ".join([
            str(self.id) or '-',
            self.title or '-',
        ])
