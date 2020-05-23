from django.urls import path
from .views import newTrip, home

urlpatterns = [
    path("new/", newTrip, name="newTrip"),
    path("", home, name="home")
]