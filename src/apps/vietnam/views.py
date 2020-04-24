from django.views.generic import ListView

from apps.vietnam.models import VieDays


class IndexView(ListView):
    template_name = "vietnam/index.html"
    model = VieDays

