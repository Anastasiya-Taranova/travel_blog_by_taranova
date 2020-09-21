import uuid

from django.db import models as m
from storages.backends.s3boto3 import S3Boto3Storage


class Countries(m.Model):
    name = m.TextField(max_length=20, null=True,  blank=True)

    class Meta:
        verbose_name_plural = "Countries"


class PointsMap(m.Model):
    points = m.TextField(max_length=50, null=True,  blank=True)

    class Meta:
        verbose_name_plural = "Points"


class Content(m.Model):
    content = m.TextField(null=True, blank=True)
    country_name = m.ForeignKey(Countries, on_delete=m.CASCADE, related_name="country")
    points = m.ManyToManyField(PointsMap)


    class Meta:
        verbose_name_plural = "Content"


class Photo(m.Model):
    uuid = m.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = m.ForeignKey(Content, on_delete=m.CASCADE, related_name="photos")
    original = m.FileField(storage=S3Boto3Storage())

    class Meta:
        verbose_name_plural = "Photos"
