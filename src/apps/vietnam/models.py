from django.db import models as m


class VieDays(m.Model):
    h2 = m.TextField(null=True, blank=True)
    h3 = m.TextField(null=True, blank=True)
    predescription = m.TextField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "VieDays"

