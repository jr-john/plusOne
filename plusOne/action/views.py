from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Trip
from .forms import TripForm


# @login_required
def home(request, *args, **kwargs):
    # if not request.user.first_name:
    #     return redirect('/register/')
    
    form = TripForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TripForm()

    context = {
        "form" : form
    }
    return render(request, "home.html", context)


# @login_required
def activity(request, *args, **kwargs):
    trips = []
    req = []
    trips = Trip.objects.all()
    for trip in trips:
        if request.user.username == trip.owner:
            req.append(trip)

    context = {
        'feeds' : req
    }
    return render(request, "activity.html", context)


# @login_required
def stop(request, *args, **kwargs):
    trips = Trip.objects.all()
    for trip in trips:
        if trip.owner == request.user.username:
            trip.is_active = False
            break
    return redirect("MyActivity")
