from .exceptions import JobStatusError, JobTransitionError

from core.utils import getLogger
log = getLogger(__name__)

class JobStatusTransitionMixin(object):
    STATUS_DRAFT = 'DRAFT'
    STATUS_ACTIVE = 'ACTIVE'
    STATUS_INACTIVE = 'INACTIVE'

    CHOICES_STATUS = (
        (STATUS_DRAFT, 'Draft'),
        (STATUS_ACTIVE, 'Active'),
        (STATUS_INACTIVE, 'Inactive'),
    )

    ALLOWED_TRANSITIONS = {
        STATUS_DRAFT: [STATUS_ACTIVE, STATUS_INACTIVE, ],
        STATUS_ACTIVE: [STATUS_INACTIVE, ],
        STATUS_INACTIVE: [],
    }

    def transition(self, target, commit=True):
        if not self.status in self.ALLOWED_TRANSITIONS:
            raise JobStatusError('Job.status in invalid state',
                                 job=self,
                                 current=self.status)

        if target not in self.ALLOWED_TRANSITIONS[self.status]:
            raise JobTransitionError('Job.status transition failed',
                                     job=self,
                                     current=self.status, target=target)

        previous = self.status
        self.status = target
        log.info('Job status transition success',
                 job=self,
                 status=self.status, previous=previous)

        if commit:
            self.save()

