from django.utils.decorators import available_attrs
from django.utils.functional import wraps

from .models import Job

def apply_jobs(view_func):
    @wraps(view_func, assigned=available_attrs(view_func))
    def _wrapped_view(request, *args, **kwargs):
        jobs = Job.objects.only_active()

        return view_func(request, jobs=jobs, *args, **kwargs)
    return _wrapped_view
