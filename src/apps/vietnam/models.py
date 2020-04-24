from django.db import models as m


class Add(m.Model):
    add = m.TextField(unique=True)
    something = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Add"

    def __str__(self):
        return f"#{self.pk}:{self.add!r}"


class VieDays(m.Model):
    day = m.IntegerField(null=True, blank=True)
    description = m.TextField(null=True, blank=True)
    money = m.IntegerField(null=True, blank=True)
    # save = m.BooleanField()
    adds = m.ManyToManyField(Add, related_name="vieday")

    class Meta:
        verbose_name_plural = "VieDays"

    def __str__(self):
        return f"#{self.pk}:{self.day!r}"


class Responsibility(m.Model):
    vieday = m.ForeignKey(VieDays, on_delete=m.CASCADE, related_name="responsibilities")
    summary = m.TextField()
    class Meta:
        verbose_name_plural = "Responsibility"
