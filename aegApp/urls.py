from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('teams', views.teams),
    path('contact', views.contact),
    path('partners', views.partners),
    path('calendar', views.calendar),
]