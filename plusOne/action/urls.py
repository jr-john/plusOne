from django.urls import path
from .views import home, activity, search, add, stop

urlpatterns = [
    path("", home, name="home"),
    path("activity/", activity, name="activity"),
    path("search/", search, name="search"),
    path("search/add/", add, name="add"),
    path("activity/stop/", stop, name="stop")
]