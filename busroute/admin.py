from django.contrib import admin
from .models import *

@admin.register(BusInfo)
class BusInfoAdmin(admin.ModelAdmin):
    list_display = ['id','bus_name','bus_number']

@admin.register(Route)
class RouteAdmin(admin.ModelAdmin):
    list_display = ['id','route_name','route_nmber']

@admin.register(BusRoute)
class BusRouteAdmin(admin.ModelAdmin):
    list_display = ['id','bus','route','from_time','to_time']