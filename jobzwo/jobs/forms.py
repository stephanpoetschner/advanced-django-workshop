import floppyforms.__future__ as forms

from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 
                  'location', 
                  'external_url', 'contact_email', ]

class SearchForm(forms.Form):
    q = forms.CharField(label='Title', required=False)
    l = forms.CharField(label='Location', required=False)

    is_visual_impairment_accepted = forms.BooleanField(required=False)
    is_hearing_impairment_accepted = forms.BooleanField(required=False)
    is_motor_impairment_accepted = forms.BooleanField(required=False)

    def search(self, jobs):
        q = self.cleaned_data.get('q')
        if q:
            jobs = jobs.filter(title__icontains=q)

        l = self.cleaned_data.get('l')
        if l:
            jobs = jobs.filter(location__icontains=l)

        impairements_filter = {}
        for name in [ 'visual', 'hearing', 'motor' ]:
            impairment = 'is_{}_impairment_accepted'.format(name)
            value = self.cleaned_data.get(impairment)
            if value:
                impairements_filter[impairment] = value
        if impairements_filter:
            jobs = jobs.filter(**impairements_filter)

        return jobs
