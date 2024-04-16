from django import forms
from .models import Car


class CarCreationForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['type', 'model', 'year', 'image_URL', 'price']
        widgets = {
            'image_URL': forms.TextInput(attrs={'placeholder': 'https://...'})
        }
