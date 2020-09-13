from apps.index.models import TripInfo
from django.views.generic import ListView


class IndexView(ListView):
    template_name = "index/index.html"
    context_object_name = "obj_list"

    def get_queryset(self):
        return TripInfo.objects.all()
