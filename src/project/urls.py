from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

here = Path(__file__).parent.resolve()


def view(r):
    index = here.parent.parent / "index.html"
    with index.open() as f:
        return HttpResponse(f.read())


def view_css(r):
    index = here.parent.parent / "styles.css"
    with index.open() as f:
        return HttpResponse(f.read())


def view_js(r):
    index = here.parent.parent / "html5shiv.js"
    with index.open() as f:
        return HttpResponse(f.read())


def view_jpg1(r):
    index = here.parent.parent / "imgs/nastya1.jpg"
    with index.open("rb") as f:
        return HttpResponse(f.read())





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path("css", view_css),
    path("js", view_js),
    path("nastya1/jpg", view_jpg1), ]
