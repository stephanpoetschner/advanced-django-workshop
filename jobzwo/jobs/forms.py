from django.core.urlresolvers import reverse

import floppyforms.__future__ as forms

from .models import Job


class InputClassInsertionMixin(object):
    def add_css_classes(self, fields, css_classes):
        for field in fields.values():
            attrs = field.widget.attrs
            attrs['class'] = ' '.join(filter(None, [
                attrs.get('class', '').strip(),
                css_classes,
            ]))


class JobForm(InputClassInsertionMixin, forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company',
                  'description',
                  'location',
                  'external_url', 'contact_email',

                  'is_visual_impairment_accepted',
                  'is_hearing_impairment_accepted',
                  'is_motor_impairment_accepted', ]

    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)

        attrs = self.fields['company'].widget.attrs
        attrs.update({
            'data-api-url': reverse('jobs_json_companies'),
        })
        self.fields['location'].attrs = attrs

        self.add_css_classes(self.fields,
                             'form-control input-lg')

    def clean(self):
        data = super(JobForm, self).clean()

        if not any([
            data['is_visual_impairment_accepted'],
            data['is_hearing_impairment_accepted'],
            data['is_motor_impairment_accepted'],
        ]):
            raise forms.ValidationError(
                'At least one impairment must be active.')


class JobSearchForm(forms.Form):
    q = forms.CharField(
        label='What', required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'job title, keywords or tags',
        }),
    )
    l = forms.CharField(
        label='Where', required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'job title, keywords or tags',
        }),
    )

    is_visual_impairment_accepted = forms.BooleanField(
        label='visual disabilities',
        required=False, initial=False)
    is_hearing_impairment_accepted = forms.BooleanField(
        label='hearing disabilities',
        required=False, initial=False)
    is_motor_impairment_accepted = forms.BooleanField(
        label='motor disabilities',
        required=False, initial=False)

    def search(self, jobs):
        q = self.cleaned_data.get('q')
        if q:
            jobs = jobs.filter(title__icontains=q)

        l = self.cleaned_data.get('l')
        if l:
            jobs = jobs.filter(location__icontains=l)

        impairements_filter = {}
        for name in ['visual', 'hearing', 'motor', ]:
            impairment = 'is_{}_impairment_accepted'.format(name)
            value = self.cleaned_data.get(impairment)
            if value:
                impairements_filter[impairment] = value
        if impairements_filter:
            jobs = jobs.filter(**impairements_filter)

        return jobs


class CompanySearchForm(forms.Form):
    term = forms.CharField()

    def search(self, companies):
        q = self.cleaned_data.get('term')
        if q:
            companies = companies.filter(name__icontains=q)
        return companies
