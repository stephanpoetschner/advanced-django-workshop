from django.db import models

from .mixins import JobStatusTransitionMixin

class JobQuerySet(models.QuerySet):
    def only_active(self):
        return self.filter(status=JobStatusTransitionMixin.STATUS_ACTIVE)

    def only_draft(self):
        return self.filter(status=JobStatusTransitionMixin.STATUS_DRAFT)
