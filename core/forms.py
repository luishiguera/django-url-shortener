from django import forms
from .models import Link

class ShortenerForm(forms.ModelForm):

    class Meta:
        model = Link
        fields = ('url',)
        widgets = {
        'url': forms.URLInput(attrs={'class': 'input is-rounded is-medium', 'placeholder': 'URL'}),
        }