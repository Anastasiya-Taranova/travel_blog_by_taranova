from apps.contacts.apps import ContactsConfig
from apps.contacts.views import IndexView
from django.urls import path

app_name = ContactsConfig.label

urlpatterns = [path("", IndexView.as_view(), name="contacts")]
