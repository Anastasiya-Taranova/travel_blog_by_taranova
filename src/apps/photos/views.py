from apps.photos.models import Photos
from django.views.generic import ListView


class IndexView(ListView):
    template_name = "photos/photo.html"
    model = Photos
