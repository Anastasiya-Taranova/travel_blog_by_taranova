from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def view(request: HttpRequest) -> HttpResponse:
    return render(request, "index/index.html")