from django.views.generic import ListView

from apps.index.models import TripInfo


class IndexView(ListView):
    template_name = "index/index.html"
    # model = TripInfo
    context_object_name = 'obj_list'

    def get_queryset(self):
        return TripInfo.objects.all()
