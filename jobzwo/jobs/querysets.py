from django.db import models

from .mixins import JobStatusTransitionMixin

class JobQuerySet(models.QuerySet):
    def only_active(self):
        qs = self
        return qs.filter(status=JobStatusTransitionMixin.STATUS_ACTIVE)


class JobManager(models.Manager.from_queryset(JobQuerySet),
                 models.Manager):
    pass
