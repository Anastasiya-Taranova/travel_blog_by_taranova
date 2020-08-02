from django.urls import path

from apps.preparation import views
from apps.preparation.apps import PreparationConfig

app_name = PreparationConfig.label

urlpatterns = [path("", views.index, name="preparation")]
