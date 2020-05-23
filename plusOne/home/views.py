from django.shortcuts import render

# Create your views here.
def NewTrip(request):
    return render(request, 'entry.html')

def home(request):
    return render(request, "home.html")