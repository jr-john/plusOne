from django.db import models
from django.utils import timezone

def def_time():
    return timezone.now().strftime("%H:%M")

TAG_LIST = [
    ['airport', 'Rajiv Gandhi Intenational Airport'],
    ['railway-secunderabad', 'Secunderabad Railway Station'],
    ['railway-lingam', 'Lingampally Railway Station'],
    ['railway-begumpet', 'Begumpet Railway Station'],
    ['railway-nampally', 'Hyderabad Deccan Railway Station (Nampally)'],
    ['bus-mg', 'Mahatma Gandhi Bus Station'],
    ['college','IIIT Hyderabad Campus']
]

class Trip(models.Model):
    source = models.CharField(max_length = 100, choices = TAG_LIST, default = 'other')
    destination = models.CharField(max_length = 100, choices = TAG_LIST, default = 'other')
    journey_date = models.DateField(default = timezone.now)
    journey_time = models.TimeField(default = def_time)
    is_active = models.BooleanField(default = False)
    owner = models.CharField(max_length = 100, null = True, blank = True)