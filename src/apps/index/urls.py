from apps.index.apps import IndexConfig
from apps.index.views import IndexView
from django.contrib.auth import views
from django.urls import path

app_name = IndexConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
