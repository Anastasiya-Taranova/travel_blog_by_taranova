from django.db import models as m


class Skyscanner(m.Model):
    name_city = m.CharField(max_length=30)

    def __str__(self):
        return self.name_city

    class Meta:
        verbose_name_plural = "cities"
