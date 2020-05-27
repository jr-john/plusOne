from django import forms
from .models import Trip, Profile
import datetime
from django.utils import timezone

from django.contrib.auth.models import User


class EditForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = [
            'first_name',
            'last_name',
            'email'
        ]
        labels = {
            'first_name': 'YOUR NAME?',
            'last_name': 'PHONE NUMBER?',
            'email': 'EMAIL ADDRESS?'
        }
        widgets = {
            'first_name': forms.TextInput(attrs = {'class': 'form-control py-4 mb-4', 'autocomplete': 'off'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control py-4 mb-4', 'autocomplete': 'off'}),
            'email': forms.TextInput(attrs = {'class': 'form-control py-4 mb-4', 'autocomplete': 'off'})
        }


class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            "destination",
            "source",
            "journey_date",
            "journey_time",
            "minima",
            "maxima"
        ]
        labels = {
            "source": "WHERE FROM?",
            "destination": "WHERE TO?",
            "journey_date": "WHEN?",
            "journey_time": "",
            "minima": "I AM WILLING TO START BETWEEN",
            "maxima" : "AND"
        }
        widgets = {
            "source": forms.Select(attrs = {'class': 'form-dd py-3 pl-2 mb-3', 'autocomplete': 'off'}),
            "destination": forms.Select(attrs = {'class': 'form-dd py-3 pl-2 mb-3', 'autocomplete': 'off'}),
            "journey_date": forms.DateInput(attrs = {'class': 'form-control py-4 mb-3 dt-gray', 'autocomplete': 'off'}),
            "journey_time": forms.TimeInput(attrs = {'class': 'form-control py-4 mb-3 dt-gray', 'autocomplete': 'off'}),
            "minima": forms.NumberInput(attrs = {'class': 'form-control py-4 mb-1 dt-gray', 'autocomplete': 'off'}),
            "maxima": forms.NumberInput(attrs = {'class': 'form-control py-4 mb-1 dt-gray', 'autocomplete': 'off'})
        }