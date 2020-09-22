from django.contrib.gis.db import models
from geopy import Point


class Shop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField(
        geography=True,
        default=Point(0.0, 0.0),
    )
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
