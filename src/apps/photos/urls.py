from django.urls import path

from apps.photos.apps import PhotosConfig
from apps.photos.views import IndexView

app_name = PhotosConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
