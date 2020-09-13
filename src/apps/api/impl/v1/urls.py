from apps.api.impl.v1.views import UserViewSet
from apps.api.views import TelegramView
from django.urls import include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("user", UserViewSet, "user")

urlpatterns = [
    path("", include(router.urls)),
    path("telegram/", csrf_exempt(TelegramView.as_view())),
]
