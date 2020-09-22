from ckeditor.fields import RichTextField
from django.db import models as m
from django.urls import reverse_lazy
from django_2gis_maps import fields as map_fields
from django_2gis_maps.mixins import DoubleGisMixin


class Points(DoubleGisMixin, m.Model):
    address = map_fields.AddressField(max_length=100)
    geolocation = map_fields.GeoLocationField()

    class Meta:
        verbose_name_plural = "Точки на карте"

    def __str__(self):
        return self.geolocation


class Countries(m.Model):
    name = m.TextField(max_length=20, null=True, blank=True)
    content = RichTextField(null=True, blank=True)
    marker_map = m.ManyToManyField(Points)

    def get_absolute_url(self):
        return reverse_lazy("trips:index", kwargs={"pk": str(self.pk)})

    class Meta:
        verbose_name_plural = "Контент"

    def __str__(self):
        return self.name
