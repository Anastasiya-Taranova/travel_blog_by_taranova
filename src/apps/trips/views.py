from django.views.generic import DetailView

from apps.trips.models import Countries


class Count(DetailView):
    template_name = "trips/index.html"
    model = Countries
