from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse

from apps.onboarding.utils.util import unique_slug_generator

User = get_user_model()


class Trips(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, default="", blank=True)
    name = models.CharField(max_length=50, blank=True)
    user_location = models.CharField(max_length=100, blank=True)
    destination = models.CharField(max_length=100, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    budget = models.IntegerField(default=0)
    participants_total = models.IntegerField(default=1)
    comments_total = models.IntegerField(default=0)
    public = models.BooleanField(default=False)
    packing_list = models.TextField(blank=True, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "trip"
        verbose_name_plural = "Запланированные путешествия"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("account:trips_detailed", kwargs={"slug": self.slug})


def pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.slug == "":
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Trips)
