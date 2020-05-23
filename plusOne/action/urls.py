from django.urls import path
from .views import newTrip, home, activity

urlpatterns = [
    path("new/", newTrip, name="newTrip"),
    path("", home, name="home"),
    path("activity/", activity, name="activity")
]