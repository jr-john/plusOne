from django import forms
from .models import Trip

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
            "minima": "I PREFER TO START BETWEEN",
            "maxima" : "AND"
        }
        widgets = {
            "source": forms.Select(attrs = {'class': 'form-dd py-3 pl-2 mb-4', 'autocomplete': 'off'}),
            "destination": forms.Select(attrs = {'class': 'form-dd py-3 pl-2 mb-4', 'autocomplete': 'off'}),
            "journey_date": forms.DateInput(attrs = {'class': 'form-control py-4 mb-4 dt-gray', 'autocomplete': 'off'}),
            "journey_time": forms.TimeInput(attrs = {'class': 'form-control py-4 mb-4 dt-gray', 'autocomplete': 'off'}),
            "minima": forms.TimeInput(attrs = {'class': 'form-control py-4 mb-4 dt-gray', 'autocomplete': 'off'}),
            "maxima": forms.TimeInput(attrs = {'class': 'form-control py-4 mb-4 dt-gray', 'autocomplete': 'off'})
        }