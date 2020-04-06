from pathlib import Path
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
#from django.shortcuts import render

here = Path(__file__).parent.resolve()


def view(r):
    index = here.parent.parent / "index.html"
    with index.open() as f:
        return HttpResponse(f.read())


def view_css(r):
    index = here.parent.parent / "styles.css"
    with index.open() as f:
        return HttpResponse(f.read(), content_type="text/css")


def view_js(r):
    index = here.parent.parent / "html5shiv.js"
    with index.open() as f:
        return HttpResponse(f.read(), content_type="application/js")


def view_jpg1(r):
    index = here.parent.parent / "imgs/nastya1.jpg"
    with index.open("rb") as f:
        return HttpResponse(f.read())


# def view(request):
# return render(request, "index.html")


# def view_jpg1(request):
# return render(request, "imgs/nastya1.jpg", content_type="image/jpg")


# def view_css(request):
# return render(request, "styles.css", content_type="text/css")


# def view_js(request):
# return render(request, "html5shiv.js", content_type="application/js")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view),
    path("styles.css", view_css),
    path("html5shiv.js", view_js),
    path("imgs/nastya1.jpg", view_jpg1),
]
