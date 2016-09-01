from django import forms
from .models import Job


class JobForm(forms.ModelForm):

    accept_terms = forms.BooleanField(label='Accept Terms', initial=False)

    class Meta:
        model = Job
        fields = ['title', 'description', 'external_url', 'contact_email',
                  'is_visual_impairment_accepted', 'is_hearing_impairment_accepted',
                  'is_motor_impairment_accepted']



    def clean(self):
        cleaned_data = super(JobForm, self).clean()



        if not any([
            self.cleaned_data.get('is_visual_impairment_accepted'),
            self.cleaned_data.get('is_hearing_impairment_accepted'),
            self.cleaned_data.get('is_motor_impairment_accepted')
        ]):
            raise forms.ValidationError(
                'Kein Impairment', code='impairment_error'
            )