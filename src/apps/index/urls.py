from django.urls import path

from apps.index.apps import IndexConfig
from apps.index.views import IndexView

app_name = IndexConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
