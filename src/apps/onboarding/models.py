from typing import Optional

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.urls import reverse_lazy

from apps.onboarding.utils.util import unique_slug_generator
from apps.onboarding.utils.xdatetime import utcnow

User = get_user_model()


class AuthProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    verification_code = models.CharField(max_length=255, unique=True)
    verified_at = models.DateTimeField(null=True, blank=True)
    notified_at = models.DateTimeField(null=True, blank=True)
    site = models.ForeignKey(
        Site, null=True, blank=True, on_delete=models.CASCADE, db_index=True
    )

    @property
    def is_verified(self) -> bool:
        cond = self.verified_at and self.verified_at <= utcnow()
        return cond

    @property
    def link(self) -> Optional[str]:
        if not self.site:
            return None

        domain = self.site.domain
        scheme = {"localhost": "http"}.get(domain, "https")

        url = f"{scheme}://{domain}{self.get_absolute_url()}"

        return url

    def get_absolute_url(self) -> str:
        return reverse_lazy(
            "onboarding:sign_in_verified", kwargs={"code": self.verification_code}
        )

    def __str__(self) -> str:
        return f"{self.__class__.__name__} #{self.pk} for {self.user.email!r}"


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, related_name="profile"
    )
    name = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__} #{self.pk} for {self.user.email!r}"


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
    pins_total = models.IntegerField(default=0)
    packing_list = models.TextField(blank=True, max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "trip"
        verbose_name_plural = "trips"

    def __str__(self):
        return str(f"Trip ID: " + str(self.pk) + ' "' + self.name)

    def get_absolute_url(self):
        return reverse("onboarding:trips_detailed", kwargs={"slug": self.slug})


def pre_save_receiver(sender, instance, *args, **kwargs):
    if instance.slug == "":
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender=Trips)


class UserNotifications(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "notification"
        verbose_name_plural = "notifications"

    def create_notification(self, instance, message):
        UserNotifications.objects.create(user_id=instance, message=message).save()

    def read_notification(self):
        self.read = True
        self.save()

    def delete_notification(self, id_):
        UserNotifications.objects.delete(id=id_).save()

    def __str__(self):
        return str(
            '"' + self.message + '"' + " for the user: " + self.user_id.get_username()
        )
