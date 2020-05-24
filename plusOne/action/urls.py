from django.urls import path
from .views import home, activity, search

urlpatterns = [
    path("", home, name="home"),
    path("activity/", activity, name="activity"),
    path("search/", search, name="search")
]