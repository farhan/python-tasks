from django import forms


class UrlForm(forms.Form):
    url = forms.URLField(required=True, max_length=500,
                         widget=forms.TextInput(attrs={'placeholder': 'Paste your url here to shorten it'}))
