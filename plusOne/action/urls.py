from django.urls import path
from .views import home, activity, search, add, stop, tripdetails, profile, edit

urlpatterns = [
    path("", home, name="home"),
    path("activity/", activity, name="activity"),
    path("search/", search, name="search"),
    path("search/add/", add, name="add"),
    path("activity/stop/<int:id>", stop, name="stop"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", edit, name="edit"),
    path("search/trip/<int:id>", tripdetails, name="tripdetails")
]