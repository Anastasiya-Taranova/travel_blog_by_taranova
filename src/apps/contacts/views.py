from apps.contacts.models import Shop
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.views.generic import ListView

longitude = -80.191788
latitude = 25.761681

user_location = Point(longitude, latitude, srid=4326)


class IndexView(ListView):
    template_name = "contacts/index.html"
    model = Shop
    queryset = Shop.objects.annotate(
        distance=Distance("location", user_location)
    ).order_by("distance")[0:6]
    context_object_name = "shops"
