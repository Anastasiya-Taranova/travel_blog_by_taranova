from apps.preparation.apps import PreparationConfig
from apps.preparation.views import IndexView
from django.urls import path

app_name = PreparationConfig.label

urlpatterns = [path("", IndexView.as_view(), name="index")]
