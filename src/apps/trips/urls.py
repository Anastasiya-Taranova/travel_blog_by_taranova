from django.urls import path

from apps.trips.apps import TripsConfig
from apps.trips.views import Count

app_name = TripsConfig.label

urlpatterns = [
    path("<int:pk>/", Count.as_view(), name="index"),
]
