import django_tables2 as tables
from .models import *
from django_tables2.utils import A
class BusTable(tables.Table): 
    num_of_routes = tables.LinkColumn('list_of_routes',args=[tables.A('pk')],verbose_name='Number of routes this bus runs on', accessor='busroute_set.count', order_by=('num_of_routes'))
    class Meta:
        model = BusInfo
        attrs = {'class':'table'}
        fields = ('bus_name','bus_number')

class RouteTable(tables.Table):
    num_of_buses = tables.LinkColumn('list_of_buses_for_specific_route',args=[tables.A('pk')],verbose_name='Number of buses in this route', accessor='busroute_set.count', order_by=('num_of_buses'))
    class Meta:
        model = Route
        attrs = {'class':'table'}
        fields = ('route_name','route_number')

class BusDetailTable(tables.Table):
    bus_name = tables.Column(verbose_name='Bus Name',accessor='bus.bus_name')
    bus_number = tables.Column(verbose_name='Bus Number',accessor='bus.bus_number')
    

    class Meta:
        model = BusRoute
        attrs = {'class':'table'}
        fields = ('bus_name','bus_number','from_time','to_time')

class RouteDetailTable(tables.Table):
    route_name = tables.Column(verbose_name='Route Name',accessor='route.route_name')
    route_number = tables.Column(verbose_name='Route Number',accessor='route.route_number')

    class Meta:
        model = BusRoute
        attrs = {'class':'table'}
        fields = ('route_name','route_number','from_time','to_time')

