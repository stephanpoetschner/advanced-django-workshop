from django.db import models
from .errors import StateError
from structlog import get_logger
log = get_logger()


STATUS = (
    ('draft', 'draft'),
    ('active', 'active'),
    ('inactive', 'inactive'),
)

class AbstractTimestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AbstractDisability(models.Model):
    is_visual_impairment_accepted = models.BooleanField(default=False)
    is_hearing_impairment_accepted = models.BooleanField(default=False)
    is_motor_impairment_accepted = models.BooleanField(default=False)

    def impairment_set(self):
        return (self.is_visual_impairment_accepted
                or self.is_hearing_impairment_accepted
                or self.is_motor_impairment_accepted)

    class Meta:
        abstract = True

class JobQuerySet(models.QuerySet):
    def only_active(self):
        return self.filter(status='active')

class JobStatusMixin(object):

    states_dict = {
        'draft' : ('active', 'inactive'),
        'active' : ('inactive',),
        'inactive': (),
    }

    def change_state(self, new_state):
        current_status = self.status
        if new_state in self.states_dict[current_status]:
            self.status = new_state
            log.info('Job.status.changed', old_status=current_status, new_status=new_state)
            return self
        else:
            raise StateError('State change from {} to {} not allowed'.format(current_status, new_state))


class Job(JobStatusMixin, AbstractDisability, AbstractTimestamp):
    titel = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    location = models.CharField(max_length=30)
    external_url = models.URLField()
    contact_email = models.EmailField()
    status = models.CharField(max_length=10, choices=STATUS)

    objects = JobQuerySet.as_manager()

    def __str__(self):
        return self.titel









