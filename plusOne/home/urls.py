from django.urls import path



from . import views

urlpatterns = [
    #path("register", views.register, name="register"),
    #path("login", views.login, name="login"),
    #path("logout", views.logout, name="logout")
    path("NewTrip", views.NewTrip, name="NewTrip"),
    path("", views.home, name="home")
    ]
