import json

import requests
from django.shortcuts import render

from apps.preparation.forms import CityForm
from apps.preparation.models import Skyscanner

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/EUR/en-US/"

headers = {
    "x-rapidapi-host": "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    "x-rapidapi-key": "bfea1864abmsha9c55f09e75d6adp116740jsn62b2a0553716",
}


def index(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = Skyscanner.objects.all()

    all_cities = []

    for name_city in cities:
        querystring = {"query": name_city.name_city}
        response = requests.request("GET", url, headers=headers, params=querystring)
        j = json.loads(response.text)

        city_trip = {
            "city": name_city.name_city,
            "CountryName": j["Places"][0]["CountryName"],
            "PlaceId": j["Places"][0]["PlaceId"],
        }

        all_cities.append(city_trip)
        print(all_cities)

    context = {
        "all_info": all_cities,
        "form": form,
    }

    return render(request, "preparation/index.html", context)
