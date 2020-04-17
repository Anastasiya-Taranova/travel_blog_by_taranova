from django.views.generic import TemplateView

from apps.index.models import TripInfo


class IndexView(TemplateView):
    template_name = "index/index.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)
        info = TripInfo.objects.first()
        ctx = {"country": info.country}
        ctx.update(parent_ctx)
        return ctx
