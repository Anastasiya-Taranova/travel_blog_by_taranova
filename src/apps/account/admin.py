from django.contrib import admin

from apps.account.models import Trips


@admin.register(Trips)
class TripsAdmin(admin.ModelAdmin):
    pass