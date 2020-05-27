from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Trip
from .forms import TripForm, EditForm
import datetime
import time
import json
from django.contrib.auth.models import User
import logging
import re
from django.contrib import messages
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

# @login_required
def home(request, *args, **kwargs):
    # if not request.user.first_name:
    #    return redirect('/register/')
    form = TripForm(request.POST or None)
    if request.method == 'POST':
        source = request.POST.get('source')
        destin = request.POST.get('destination')
        j_time = request.POST.get('time')
        j_date = request.POST.get('date')
        minima = request.POST.get('minima')
        maxima = request.POST.get('maxima')

        # form validation
        errorMessages = {}
        
        # clean_source
        if destin == source:
            errorMessages['source'] = "Invalid! Source cannot be same as Destination!"

        # clean_journey_time
        journey_datetime = datetime.datetime.combine(
            datetime.datetime.strptime(j_date, '%d/%m/%Y').date(), 
            datetime.datetime.strptime(j_time, '%H:%M').time()
        )
        if journey_datetime < timezone.now():
            errorMessages['journey_time'] = "Invalid Time!"
        
        response = JsonResponse(errorMessages)

        if len(errorMessages) == 0:
            request.session['data'] = {
                "source" : source,
                "destination" : destin,
                "journey_date" : j_date,
                "journey_time" : j_time,
                "minima" : str(minima),
                "maxima" : str(maxima)
            }
        else:
           response.status_code = 403 

        return response

    context = {
        "form" : form
    }
    return render(request, "home.html", context)


# @login_required
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
    # object_list =  sorted(object_list, key = lambda i : (int(datetime.datetime.strptime(i['journey_date'], "%d/%m/%Y").time().strftime("%Y%m%d")),int(datetime.datetime.strptime(i['journey_time'], "%H:%M").time().strftime("%H%M"))),reverse=False)
    object_list =  sorted(object_list, key = lambda i : (i['journey_date'],i['journey_time']),reverse=False)
    context = {
        'trips': object_list,
        'populated': len(object_list)
    }
    return render(request, "activity.html", context)

def profile(request, *args, **kwargs):
    print(request.user.first_name)
    context={
        'user_list' : request.user
    }
    return render(request, 'profile.html', context)

# @login_required
def stop(request, id):
    trip = Trip.objects.get(id = id)
    logger.warning('entered stop')
    logger.warning(trip.is_active)
    trip.is_active = False
    trip.save()
    return redirect("activity")

def edit(request, *args, **kwargs):
    form = EditForm(request.POST or None, instance = request.user)
    if request.method == 'POST':
        if form.is_valid():
            temp_list=form.cleaned_data
            temp_name=temp_list.get('first_name')
            temp_num=temp_list.get('last_name')
            temp_email=temp_list.get('email')
            x=re.findall("[0-9]", temp_num)
            if len(x) == 10 :
                request.user.first_name = temp_name
                request.user.last_name = temp_num
                request.user.email = temp_email
                request.user.save()
                return redirect('/profile')
            else:
                messages.info(request, 'Enter Valid Phone Number')
                return render(request, 'edit.html', {'form' : form})
        else:
            messages.info(request, 'Enter valid email address')
            return render(request, 'edit.html', {'form' : form})       
    context = {
        'form': form
    }
    print("yes")
    return render(request, 'edit.html', context)


# @login_required
def search(request, *args, **kwargs):
    search_query = request.session.get('data', {})
    source_query = search_query.get("source")
    destination_query = search_query.get("destination")
    date_query = search_query.get("journey_date")
    date_query = datetime.datetime.strptime(date_query, "%d/%m/%Y").date()
    time_query = search_query.get("journey_time")
    time_query = datetime.datetime.strptime(time_query, "%H:%M").time()
    min_query = float(search_query.get("minima"))
    max_query = float(search_query.get("maxima"))
    dt_query = datetime.datetime.combine(date_query, time_query)
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
            object_list.append({
                    "id" : trip.id,
                    "source" : TAG_DICT[trip.source],
                    "destination" : TAG_DICT[trip.destination],
                    "journey_date" : trip.journey_date.strftime("%d/%m/%Y"),
                    "journey_time" : trip.journey_time.strftime("%H:%M"),
                    "is_active" : True,
                    "owner" : trip.owner,
                })
    object_list =  sorted(object_list, key = lambda i:abs(int(time_query.strftime("%H%M")) - int(datetime.datetime.strptime(i['journey_time'], "%H:%M").time().strftime("%H%M"))),reverse=False)
    context = {
        "object_list": object_list,
        "populated": len(object_list)
    }
    return render(request, "search.html", context)

# @login_required
def add(request, *args, **kwargs):
    search_query = request.session.get("data", {})
    source_query = search_query.get("source")
    destination_query = search_query.get("destination")
    date_query = search_query.get("journey_date")
    date_query = datetime.datetime.strptime(date_query, "%d/%m/%Y").date()
    time_query = search_query.get("journey_time")
    time_query = datetime.datetime.strptime(time_query, "%H:%M").time()
    Trip.objects.create(
        source = source_query,
        destination = destination_query,
        journey_date = date_query,
        journey_time = time_query,
        is_active = True,
        owner = request.user.username
    )
    return redirect("/")


# @login_required
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
