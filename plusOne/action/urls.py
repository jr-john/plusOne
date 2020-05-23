from django.urls import path
from .views import NewTrip, home

urlpatterns = [
    path("NewTrip/", NewTrip, name="NewTrip"),
    path("", home, name="home")
]