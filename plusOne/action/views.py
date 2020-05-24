from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Trip
from .forms import TripForm
import datetime
import json
from django.contrib.auth.models import User

TAG_DICT = {
    'airport': 'Rajiv Gandhi International Airport',
    'railway-secunderabad': 'Secunderabad Railway Station',
    'railway-lingam': 'Lingampally Railway Station',
    'railway-begumpet': 'Begumpet Railway Station',
    'railway-nampally': 'Hyderabad Deccan Railway Station (Nampally)',
    'bus-mg': 'Mahatma Gandhi Bus Station',
    'college':'IIIT Hyderabad Campus'
}

# @login_required
def home(request, *args, **kwargs):
    # if not request.user.first_name:
    #     return redirect('/register/')
    
    form = TripForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("search/")
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
        'feeds' : req,
        'hidemy': True
    }
    return render(request, "activity.html", context)


# @login_required
def stop(request, *args, **kwargs):
    trips = Trip.objects.all()
    for trip in trips:
        if trip.owner == request.user.username:
            trip.is_active = False
            trip.save()
    return redirect("activity")

# @login_required
def search(request, *args, **kwargs):
    search_query = Trip.objects.latest("id")
    source_query = search_query.source
    destination_query = search_query.destination
    date_query = search_query.journey_date
    time_query = search_query.journey_time
    dt_query = datetime.datetime.combine(date_query, time_query)
    trips = Trip.objects.filter(
        source=source_query,
        destination=destination_query,
        journey_time__gte= dt_query - datetime.timedelta(hours=1.5),
        journey_time__lte= dt_query + datetime.timedelta(minutes=30),
        is_active=True)
    object_list = [
        {
            "id" : trip.id,
            "source" : TAG_DICT[trip.source],
            "destination" : TAG_DICT[trip.destination],
            "journey_date" : trip.journey_date.strftime("%d/%m/%Y"),
            "journey_time" : trip.journey_time.strftime("%H:%M"),
            "is_active" : True,
            "owner" : trip.owner,
        }
        for trip in trips
    ]
    context = {"object_list":object_list}
    return render(request, "search.html", context)

# @login_required
def add(request, *args, **kwargs):
    search_query = Trip.objects.latest("id")
    search_query.is_active = True
    search_query.owner = request.user.username
    search_query.save()
    return redirect("/")


def tripdetails(request, id):
    trip = Trip.objects.get(id = id)
    owner = User.objects.get(username = trip.owner)

    context = {
        'owner': owner,
        'trip': trip
    }
    return render(request, 'tripdetails.html', context)