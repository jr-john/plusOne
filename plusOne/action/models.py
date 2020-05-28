from django.db import models
from django.utils import timezone
from datetime import datetime, timedelta, date

def def_journey_time():
    dt = timezone.now() + timedelta(minutes=10)
    return dt.time().strftime("%H:%M")


TAG_LIST = [
    ['airport', 'Rajiv Gandhi International Airport'],
    ['railway-secunderabad', 'Secunderabad Railway Station'],
    ['railway-lingam', 'Lingampally Railway Station'],
    ['railway-begumpet', 'Begumpet Railway Station'],
    ['railway-nampally', 'Hyderabad Deccan Railway Station (Nampally)'],
    ['bus-mg', 'Mahatma Gandhi Bus Station'],
    ['college','IIIT Hyderabad Campus']
]

class Trip(models.Model):
    source = models.CharField(max_length = 100, choices = TAG_LIST, default = 'college')
    destination = models.CharField(max_length = 100, choices = TAG_LIST, default = 'airport')
    journey_date = models.DateField(default = timezone.now)
    journey_time = models.TimeField(default = def_journey_time)
    is_active = models.BooleanField(default = False)
    owner = models.CharField(max_length = 100, null = True, blank = True)
    minima = models.IntegerField(default = 10)
    maxima = models.IntegerField(default = 10)