from django.shortcuts import render

# Create your views here.
def newTrip(request, *args, **kwargs):
    return render(request, 'entry.html')

def home(request, *args, **kwargs):
    return render(request, "home.html")