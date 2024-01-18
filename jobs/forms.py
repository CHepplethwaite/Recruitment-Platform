from django import forms
from job_app.models import job


class JobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = ['details', 'job_title', 'closing_date', 'district', 'province', 'industry', 'logo']
        widgets = {
            'details': forms.Textarea(attrs={'class': 'form-control'}),
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'closing_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'district': forms.TextInput(attrs={'class': 'form-control'}),
            'province': forms.TextInput(attrs={'class': 'form-control'}),
            'industry': forms.TextInput(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
        }