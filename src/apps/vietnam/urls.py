from django.urls import path
from apps.index.views import IndexView
from apps.vietnam.apps import VietnamConfig


app_name = VietnamConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"), ]
