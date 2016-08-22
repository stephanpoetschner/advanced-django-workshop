from django.db import models

from .mixins import JobStatusMixin

class JobQuerySet(models.QuerySet):
    def only_active(self):
        qs = self
        return qs.filter(status=JobStatusMixin.STATUS_ACTIVE)


class JobManager(models.Manager.from_queryset(JobQuerySet),
                 models.Manager):
    pass
