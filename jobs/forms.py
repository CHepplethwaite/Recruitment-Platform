from django import forms
from job_app.models import job


class JobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = ['job_title','organisation','closing_date','industry','location','country',"logo",'details']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'organisation': forms.TextInput(attrs={'class': 'form-control'}),
            'closing_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'industry': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'details': forms.Textarea(attrs={'class': 'form-control'}),
        }