from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(min_length=1, widget=forms.TextInput(attrs={'placeholder': 'Search jobs...'}))