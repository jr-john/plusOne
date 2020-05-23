from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = [
            "destination",
            "source",
            "journey_date",
            "journey_time"
        ]
        labels = {
            "source": "WHERE FROM?",
            "destination": "WHERE TO?",
            "journey_date": "WHEN?",
            "journey_time": " "
        }
        widgets = {
            "source": forms.TextInput(attrs = {'class': 'form-control py-4 mb-4'}),
            "destination": forms.TextInput(attrs = {'class': 'form-control py-4 mb-4'}),
            "journey_date": forms.DateInput(attrs = {'class': 'form-control py-4 mb-4 dt-gray'}),
            "journey_time": forms.TimeInput(attrs = {'class': 'form-control py-4 mb-4 dt-gray'})
        }