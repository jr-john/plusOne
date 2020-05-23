from django.urls import path
from .views import home, activity

urlpatterns = [
    path("", home, name="home"),
    path("activity/", activity, name="activity")
]