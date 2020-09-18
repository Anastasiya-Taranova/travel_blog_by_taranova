from apps.photos.apps import PhotosConfig
from apps.photos.views import IndexView
from django.urls import path

app_name = PhotosConfig.label

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
