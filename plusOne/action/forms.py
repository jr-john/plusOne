from django import forms
from .models import Trip
import datetime
from django.utils import timezone

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
            "source": forms.Select(attrs = {'class': 'form-dd py-3 pl-2 mb-4', 'autocomplete': 'off'}),
            "destination": forms.Select(attrs = {'class': 'form-dd py-3 pl-2 mb-4', 'autocomplete': 'off'}),
            "journey_date": forms.DateInput(attrs = {'class': 'form-control py-4 mb-4 dt-gray', 'autocomplete': 'off'}),
            "journey_time": forms.TimeInput(attrs = {'class': 'form-control py-4 mb-4 dt-gray', 'autocomplete': 'off'})
        }

    def clean_source(self, *args, **kwargs):
        print(self.instance.source)
        print(self.instance.destination)
        if self.instance.destination == self.instance.source:
            raise forms.ValidationError("Invalid! Source cannot be same as Destination!")
        return self.instance.source
    
    def clean_journey_time(self, *args, **kwargs):
        journey_time = datetime.datetime.strptime(self.instance.journey_time, "%H:%M").time()
        journey_datetime = datetime.datetime.combine(self.instance.journey_date, journey_time)
        if journey_datetime < timezone.now():
            raise forms.ValidationError("Invalid Time!")
        return self.instance.destination