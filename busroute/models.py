from django.db import models
from django.core.exceptions import ValidationError

class BusInfo(models.Model):
    bus_name = models.CharField(max_length=30)
    bus_number = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.bus_name

class Route(models.Model):
    route_name = models.CharField(max_length=30)
    route_number = models.CharField(max_length=30)

    def __str__(self):
        return self.route_name


class BusRoute(models.Model):
    bus = models.ForeignKey(BusInfo,on_delete=models.CASCADE)
    route = models.ForeignKey(Route,on_delete=models.CASCADE)
    from_time = models.DateTimeField()
    to_time = models.DateTimeField()

    class Meta:
        unique_together = ('bus','from_time','to_time')

    def __str__(self):
        return f'{self.bus} {self.route}'

    def clean(self):
        conflicting_routes = BusRoute.objects.filter(
            bus=self.bus,
            from_time__lt=self.to_time,
            to_time__gt=self.from_time
        ).exclude(pk=self.pk)

        if conflicting_routes.exists():
            conflicting_route = conflicting_routes.first()
            error_msg = f'{self.bus} is already running in {conflicting_route.route} route from {conflicting_route.from_time} to {conflicting_route.to_time}.'
            raise ValidationError(error_msg)
