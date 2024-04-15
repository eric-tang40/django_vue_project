from django import forms
from .models import Destination, Accommodation, Activity

class DestinationForm(forms.ModelForm):
    class Meta:
        model = Destination
        fields = ['name', 'country', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }
        
class AccommodationForm(forms.ModelForm):
    class Meta:
        model = Accommodation
        fields = ['name', 'price_per_night', 'destination']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter accommodation name'}),
            'price_per_night': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price per night', 'step': '0.01'}),
            'destination': forms.Select(attrs={'class': 'form-control'}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'price', 'destination']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'destination': forms.Select(attrs={'class': 'form-control'})
        }