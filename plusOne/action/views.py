from django.shortcuts import render
from .models import Trip
# Create your views here.
def newTrip(request, *args, **kwargs):
    return render(request, 'newTrip.html')

def home(request, *args, **kwargs):
    return render(request, "home.html")

def activity(request, *args, **kwargs):
    trips = []
    req = []
    trips = Trip.objects.all()
    for trip in trips:
        if request.user.username == trip.owner:
            req.append(list)
    context = {'feeds' : req}
    return render(request, "activity.html", context)