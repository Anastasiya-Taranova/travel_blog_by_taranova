from django.urls import path
from django.views.generic import TemplateView

from apps.preparation.apps import PreparationConfig
from apps.preparation.views import IndexView

app_name = PreparationConfig.label

urlpatterns = [path("", IndexView.as_view(), name="index")]
