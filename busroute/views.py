from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import *
from .tables import *

def choices(request):
    return render(request,'busroute/button.html')


def list_of_buses(request):
    bus_query = BusInfo.objects.all()
    table = BusTable(bus_query)
    return render(request,'busroute/bus_list_view.html',{'table':table})

def list_of_route(request):
    bus_routes = Route.objects.all()
    table = RouteTable(bus_routes)
    return render(request,'busroute/route_list_view.html',{'table':table})

def list_of_routes_for_specific_bus(request,pk):
    bus = get_object_or_404(BusInfo,id=pk)
    routes = BusRoute.objects.filter(bus=bus).distinct()
    table = RouteDetailTable(routes)
    return render(request,'busroute/routes_for_bus.html',{'table':table})
    

def list_of_buses_for_specific_route(request,pk):
    route = get_object_or_404(Route,id=pk)
    buses = BusRoute.objects.filter(route=route).distinct()
    table = BusDetailTable(buses)
    return render(request,'busroute/buses_on_route.html',{'table':table})

