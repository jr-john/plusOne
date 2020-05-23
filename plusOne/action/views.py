from django.shortcuts import render
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