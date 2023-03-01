from django.urls import path
from . import views

urlpatterns = [
    path('',views.houseListings, name = "home"),
    path('details/<pk>/',views.retrieve_details,name='details'),
]
