from apps.vietnam.apps import VietnamConfig
from apps.vietnam.views import IndexView
from django.urls import path

app_name = VietnamConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
