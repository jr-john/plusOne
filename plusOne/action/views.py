from django.shortcuts import render, redirect
from .models import Trip
from .forms import TripForm
# Create your views here.
def home(request, *args, **kwargs):
    return render(request, "home.html", {})

def newTrip(request, *args, **kwargs):
    form = TripForm(request.POST or None)
    if form.is_valid():
        form.save()
        form=TripForm()
    context = {
        "form" : form
    }
    return render(request, 'newTrip.html', context)

def activity(request, *args, **kwargs):
    trips = []
    req = []
    trips = Trip.objects.all()
    for trip in trips:
        if request.user.username == trip.owner:
            req.append(list)
    context = {'feeds' : req}
    return render(request, "activity.html", context)

def stop(request, *args, **kwargs):
    trips = Trip.objects.all()
    for trip in trips:
        if trip.owner == request.user.username:
            trip.is_active = False
            break
    return redirect("MyActivity")
