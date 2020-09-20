from django.views.generic import ListView

from apps.photos.models import Photos


class IndexView(ListView):
    template_name = "photos/photo.html"
    model = Photos
