from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django_2gis_maps.admin import DoubleGisAdmin

from apps.trips.models import Countries
from apps.trips.models import Points


@admin.register(Countries)
class UserInfoAdminModel(ModelAdmin):
    pass


@admin.register(Points)
class UserInfoAdminModel(DoubleGisAdmin):
    pass
