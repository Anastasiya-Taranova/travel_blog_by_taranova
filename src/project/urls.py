from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from django.http import HttpRequest
from django.shortcuts import render

here = Path(__file__).parent.resolve()


def view(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def view_css(request: HttpRequest) -> HttpResponse:
    return render(request, "styles.css", content_type="text/css")


def view_js(request: HttpRequest) -> HttpResponse:
    return render(request, "html5shiv.js", content_type="application/js")


def view_jpg1(request: HttpRequest) -> HttpResponse:
    return render(request, "imgs/nastya1.jpg", content_type="image/jpg")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path("styles.css", view_css),
    path("html5shiv.js", view_js),
    path("imgs/nastya1.jpg", view_jpg1),
]
