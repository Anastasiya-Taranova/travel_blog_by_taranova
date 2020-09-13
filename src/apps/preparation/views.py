import json

import requests
from apps.preparation.forms import CityForm
from django.views.generic import TemplateView

API_KEY = "bfea1864abmsha9c55f09e75d6adp116740jsn62b2a0553716"
rapidapi_host = "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
headers = {
    "X-RapidAPI-Host": rapidapi_host,
    "X-RapidAPI-Key": API_KEY,
    "Content-Type": "application/x-www-form-urlencoded",
}


def get_placeID(location):
    apicall = (
        "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/USD/en-GB/?query="
        + str(location)
    )
    r = requests.get(apicall, headers=headers)
    body = json.loads(r.text)
    places = body["Places"]
    top_place_id = places[0]["PlaceId"]
    print(top_place_id)
    return top_place_id


def get_country_code(country):
    response = requests.get(
        "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/reference/v1.0/countries/en-US",
        headers=headers,
    )
    response = json.loads(response.text)
    country_code = [
        item["Code"] for item in response["Countries"] if item["Name"] == country
    ][0]
    print(country_code)
    return country_code


def create_session(
    originplace, destinationplace, name_city, outboundpartialdate, inboundpartialdate
):
    apicall = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/browsequotes/v1.0"
    querystring = {
        "country": name_city,
        "currency": "USD",
        "locale": "en-US",
        "originplace": originplace,
        "destinationplace": destinationplace,
        "outboundpartialdate": outboundpartialdate,
        "inboundpartialdate": inboundpartialdate,
    }
    r = requests.get(apicall, headers=headers, params=querystring)
    body = json.loads(r.text)
    quotes = body["Quotes"]
    min_price = quotes[0]["MinPrice"]
    results = []
    results.append(min_price)
    return results


def search_flights(flight: CityForm):
    if not flight:
        return []
    if not flight.is_valid():
        return []
    country_code = get_country_code(flight.cleaned_data["name_city"])
    origin_id = get_placeID(flight.cleaned_data["originplace"])
    destination_id = get_placeID(flight.cleaned_data["destinationplace"])
    session_key = create_session(
        origin_id,
        destination_id,
        country_code,
        flight.cleaned_data["outboundpartialdate"],
        flight.cleaned_data["inboundpartialdate"],
    )
    return session_key


class IndexView(TemplateView):
    template_name = "preparation/index.html"

    def get_context_data(self, *args, **kwargs):
        form = CityForm(self.request.GET)
        results = search_flights(form)
        ctx = super().get_context_data(*args, **kwargs)
        ctx.update(
            {
                "form": form,
                "all_info": results,
            }
        )

        return ctx
