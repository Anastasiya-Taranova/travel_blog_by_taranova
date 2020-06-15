from django.views.generic import TemplateView

from apps.vietnam.models import VieDays


class IndexView(TemplateView):
    template_name = "vietnam/index.html"
    model = VieDays
