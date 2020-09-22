from django.views.generic import DetailView
from django.views.generic import ListView

# class AllCountries(DetailView):
#     template_name = "trips/index.html"
#     model = Countries
from apps.trips.models import Countries


class Count(ListView):
    template_name = "trips/index.html"
    queryset = Countries.objects.all()
