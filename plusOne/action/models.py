from django.db import models
from django.utils import timezone


class Trip(models.Model):
    source = models.CharField(max_length = 100)
    destination = models.CharField(max_length = 100)
    journey_date = models.DateField(default = timezone.now)
    journey_time = models.TimeField(default = timezone.now)
    is_active = models.BooleanField(default = False)
    owner = models.CharField(max_length = 100, null = True, blank = True)