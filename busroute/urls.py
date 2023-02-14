from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',choices,name='choices'),
    path('buses',list_of_buses,name='buslist'),
    path('routes',list_of_route,name='routelist'),
    path('routes/<int:pk>',list_of_routes_for_specific_bus,name='list_of_routes'),
    path('buses/<int:pk>',list_of_buses_for_specific_route,name='list_of_buses_for_specific_route') 
]