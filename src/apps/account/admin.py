from apps.account.models import Trips
from django.contrib import admin


@admin.register(Trips)
class TripsAdmin(admin.ModelAdmin):
    pass
