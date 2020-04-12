from django.urls import path
from apps.vietnam.apps import VietnamConfig
from apps.vietnam.views import IndexView

app_name = VietnamConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"), ]
