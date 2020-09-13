from apps.vietnam.models import VieDays
from django.views.generic import ListView


class IndexView(ListView):
    template_name = "vietnam/index.html"
    model = VieDays
