import requests
from django.shortcuts import render

from apps.weather.forms import CityForm
from apps.weather.models import City


def index(request):
    appid = "b4be221bb02fa8a7be1d57407c585b5b"
    url = "http://api.openweathermap.org/data/2.5/find?q={}&units=metric&appid=" + appid

    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
        city_info = {
            "city": city.name,
            "temp": res["main"][0]["temp"],
            "icon": res["weather"][0]["icon"],
        }

        all_cities.append(city_info)

    context = {"all_info": all_cities, "form": form}

    return render(request, "weather/index.html", context)
