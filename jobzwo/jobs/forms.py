from django import forms

from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 
                  'location', 
                  'external_url', 'contact_email', ]

class SearchForm(forms.Form):
    q = forms.CharField(label='Search', required=False)

    def search(self, jobs):
        q = self.cleaned_data.get('q')
        if q:
            jobs = jobs.filter(title__icontains=q)
        return jobs
