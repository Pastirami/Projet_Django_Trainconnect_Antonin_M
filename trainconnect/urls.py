from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    #pas beosoin d'avoir de / pour renvoyer a l'acceuil
    path('', views.index, name="acceuil"),
    path('details/<int:id>', views.details, name="details"),
    path('random/', views.random, name="random"),
]
