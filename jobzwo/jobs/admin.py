from django.contrib import admin
from .models import Job
from .mixins import JobStatusTransitionMixin



def make_active(modeladmin, request,queryset):
    queryset.update(status=JobStatusTransitionMixin.STATUS_ACTIVE)
make_active.short_description = "Mark selected jobs active"

def make_inactive(modeladmin,request,queryset):
    queryset.update(status=JobStatusTransitionMixin.STATUS_INACTIVE)
make_inactive.short_description = "Mark selected jobs inactive"

class JobAdmin(admin.ModelAdmin):
    list_display = ['title', 'external_url', 'updated', 'status']
    ordering = ['title']
    actions = [make_active, make_inactive]

admin.site.register(Job, JobAdmin)