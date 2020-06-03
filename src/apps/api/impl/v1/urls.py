from django.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.api.impl.v1.views import UserViewSet

router = DefaultRouter()
router.register("user", UserViewSet, "user")

urlpatterns = [
    path("", include(router.urls)),
]
