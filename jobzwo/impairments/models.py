from django.db import models


class AbstractImpairmentJob(models.Model):
    is_visual_impairment_accepted = models.BooleanField(default=True)
    is_hearing_impairment_accepted = models.BooleanField(default=True)
    is_motor_impairment_accepted = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def is_impairment_accepted(self):
        return any([
            self.is_visual_impairment_accepted,
            self.is_hearing_impairment_accepted,
            self.is_motor_impairment_accepted,
        ])
