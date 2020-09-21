from django.views.generic import ListView

from apps.trips.models import Countries


class IndexView(ListView):
    template_name = "trips/index.html"
    model = Countries
