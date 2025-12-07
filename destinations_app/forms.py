# destinations_app/forms.py
from django import forms
from .models import TouristDestination

class TouristDestinationForm(forms.ModelForm):
    class Meta:
        model = TouristDestination
        fields = ['place_name', 'weather', 'state', 'district',
                  'google_map_link', 'description', 'destination_img']
        widgets = {
            'place_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter place name'
            }),
            'weather': forms.Select(attrs={
                'class': 'form-control'
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter state'
            }),
            'district': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter district'
            }),
            'google_map_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Google Map URL'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter description',
                'rows': 4
            }),
            'destination_img': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }