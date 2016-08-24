from django.contrib import admin

from .exceptions import JobStatusError, JobTransitionError
from .models import Job
from .querysets import JobStatusTransitionMixin

class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'updated', ]
    actions = ['make_active', 'make_inactive', ]

    readonly_fields = ('status', )

    def make_active(self, request, queryset):
        for job in queryset:
            try:
                job.transition(JobStatusTransitionMixin.STATUS_ACTIVE)
            except (JobTransitionError, JobStatusError) as e:
                self.message_user(
                    request,
                    'Transition failed for job-id "{}".'.format(e.job.id))

    def make_inactive(self, request, queryset):
        for job in queryset:
            try:
                job.transition(JobStatusTransitionMixin.STATUS_INACTIVE)
            except (JobTransitionError, JobStatusError) as e:
                self.message_user(
                    request,
                    'Transition failed for job-id "{}".'.format(e.job.id))


admin.site.register(Job, JobAdmin)

