from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name'
        ]
        labels = {
            'first_name': 'YOUR NAME?',
            'last_name': 'CONTACT INFO?'
        }
        widgets = {
            'first_name': forms.TextInput(attrs = {'class': 'form-control py-4 mb-4', 'autocomplete': 'off'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control py-4 mb-4', 'autocomplete': 'off'}),
        }