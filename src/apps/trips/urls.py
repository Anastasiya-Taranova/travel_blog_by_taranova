from django.urls import path

from apps.trips.apps import TripsConfig
from apps.trips.views import IndexView

app_name = TripsConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
