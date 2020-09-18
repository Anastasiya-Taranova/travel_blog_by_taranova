from apps.index.models import TripInfo
from django.views.generic import ListView


class IndexView(ListView):
    template_name = "photos/photo.html"

    def get_queryset(self):
        return TripInfo.objects.all()
