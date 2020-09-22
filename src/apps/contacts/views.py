from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.views.generic import ListView

from apps.contacts.models import Shop


class IndexView(ListView):
    template_name = "contacts/index.html"
    model = Shop
    queryset = Shop.objects.all()
    context_object_name = "shops"
