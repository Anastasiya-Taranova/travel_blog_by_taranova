from django.db import models as m


class TripInfo(m.Model):
    country = m.TextField(unique=True)
    descr = m.TextField(null=True, blank=True)
    number = m.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Trip Info"
