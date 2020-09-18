from django.contrib import admin
from django.urls import include
from django.urls import path


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.index.urls")),
    path("vietnam/", include("apps.vietnam.urls")),
    path("blog/", include("apps.blog.urls")),
    path("onboarding/", include("apps.onboarding.urls")),
    path("sentry-debug/", trigger_error),
    path("api/", include("apps.api.urls")),
    path("contacts/", include("apps.contacts.urls")),
    path("preparation/", include("apps.preparation.urls")),
    path("account/", include("apps.account.urls")),
    path("photos/", include("apps.photos.urls")),
]
