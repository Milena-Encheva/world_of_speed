from django import forms
from world_of_speed.profile_app.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')

        widgets = {
            'password': forms.PasswordInput(),
            'age': forms.NumberInput(),
            'username': forms.TextInput(),
            'email': forms.EmailInput(),
        }

        help_texts = {
            'age': 'Age requirement: 21 years and above.',
        }
