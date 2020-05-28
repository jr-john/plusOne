from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Trip
from .forms import TripForm
import datetime
import json
from django.contrib.auth.models import User
import logging
logger = logging.getLogger(__name__)

TAG_DICT = {
    'airport': 'Rajiv Gandhi International Airport',
    'railway-secunderabad': 'Secunderabad Railway Station',
    'railway-lingam': 'Lingampally Railway Station',
    'railway-begumpet': 'Begumpet Railway Station',
    'railway-nampally': 'Hyderabad Deccan Railway Station (Nampally)',
    'bus-mg': 'Mahatma Gandhi Bus Station',
    'college':'IIIT Hyderabad Campus'
}

@login_required
def home(request, *args, **kwargs):
    if not request.user.first_name:
        return redirect('/register/')
    
    form = TripForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("search/")
    context = {
        "form" : form
    }
    return render(request, "home.html", context)


@login_required
def activity(request, *args, **kwargs):
    trips = Trip.objects.filter(owner = request.user.username)
    object_list=[]
    for trip in trips:
        if datetime.datetime.combine(trip.journey_date, trip.journey_time) < datetime.datetime.now():
            trip.delete()
            continue
        object_list.append(
            {
                "id" : trip.id,
                "source" : TAG_DICT[trip.source],
                "destination" : TAG_DICT[trip.destination],
                "journey_date" : trip.journey_date.strftime("%d/%m/%Y"),
                "journey_time" : trip.journey_time.strftime("%H:%M"),
                "is_active" : trip.is_active
            })
    context = {
        'trips': object_list,
        'populated': len(object_list)
    }
    return render(request, "activity.html", context)


@login_required
def stop(request, id):
    trip = Trip.objects.get(id = id)
    logger.warning('entered stop')
    logger.warning(trip.is_active)
    trip.is_active = False
    trip.save()
    return redirect("activity")


@login_required
def stop(request, id):
    trip = Trip.objects.get(id = id)
    logger.warning('entered stop')
    logger.warning(trip.is_active)
    trip.is_active = False
    trip.save()
    return redirect("activity")


@login_required
def search(request, *args, **kwargs):
    search_query = Trip.objects.latest("id")
    source_query = search_query.source
    destination_query = search_query.destination
    date_query = search_query.journey_date
    time_query=search_query.journey_time
    min_query = search_query.minima
    max_query = search_query.maxima
    dt_query=datetime.datetime.combine(date_query, time_query)
    dt_query_min = dt_query - datetime.timedelta(minutes = min_query)
    dt_query_max = dt_query + datetime.timedelta(minutes = max_query)
    trips = Trip.objects.filter(
        source=source_query,
        destination=destination_query,
        is_active=True).exclude(owner=request.user.username)
    object_list = []
    for trip in trips:
        dt = datetime.datetime.combine(trip.journey_date, trip.journey_time)
        if dt < datetime.datetime.now():
            trip.delete()
            continue
        if dt >= dt_query_min and dt <= dt_query_max:
            object_list.append(
                {
                    "id" : trip.id,
                    "source" : TAG_DICT[trip.source],
                    "destination" : TAG_DICT[trip.destination],
                    "journey_date" : trip.journey_date.strftime("%d/%m/%Y"),
                    "journey_time" : trip.journey_time.strftime("%H:%M"),
                    "is_active" : True,
                    "owner" : trip.owner,
                })
    context = {
        "object_list": object_list,
        "populated": len(object_list)
    }
    return render(request, "search.html", context)

@login_required
def add(request, *args, **kwargs):
    search_query = Trip.objects.latest("id")
    search_query.is_active = True
    search_query.owner = request.user.username
    search_query.save()
    return redirect("/")


@login_required
def tripdetails(request, id):
    trip = Trip.objects.get(id = id)
    owner = User.objects.get(username = trip.owner)

    context = {
        "owner_name": owner.first_name,
        "owner_contact": owner.last_name,
        "source" : TAG_DICT[trip.source],
        "destination" : TAG_DICT[trip.destination],
        "journey_date" : trip.journey_date.strftime("%d/%m/%Y"),
        "journey_time" : trip.journey_time.strftime("%H:%M"),
    }
    return render(request, 'tripdetails.html', context)
