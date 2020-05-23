from django.db import models
from datetime import datetime
# Create your models here.
class Trip(models.Model):
    source = models.CharField(max_length = 100)
    destination = models.CharField(max_length = 100)
    journey_datetime = models.DateTimeField(default = datetime.now)
    is_active = models.BooleanField(default = False)
    owner = models.CharField(max_length = 100)  
