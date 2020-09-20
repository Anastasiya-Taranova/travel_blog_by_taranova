from django.urls import path

from apps.account.apps import AccountConfig
from apps.account.views import CreateTrip
from apps.account.views import DeleteTrip
from apps.account.views import TripsDetailed
from apps.account.views import TripsList
from apps.account.views import UpdateTrip

app_name = AccountConfig.label

urlpatterns = [
    path("trips_list/", TripsList.as_view(), name="trips_list"),
    path("create/", CreateTrip.as_view(), name="create_trip"),
    path("<str:slug>/", TripsDetailed.as_view(), name="trips_detailed"),
    path("update/<str:slug>/", UpdateTrip.as_view(), name="update_trip"),
    path("delete/<str:slug>/", DeleteTrip.as_view(), name="delete_trip"),
]
