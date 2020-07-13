from django.views.generic import ListView

from apps.contacts.models import Shop


class IndexView(ListView):
    template_name = "contacts/index.html"
    model = Shop
