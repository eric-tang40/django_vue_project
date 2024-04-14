from django import forms
from .models import Destination

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'country', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }