from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.index.urls")),
    path('vietnam/', include('apps.vietnam.urls'))]
