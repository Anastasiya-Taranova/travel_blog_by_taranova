from django.contrib.gis.db import models
from storages.backends.s3boto3 import S3Boto3Storage


class Photos(models.Model):
    name_country = models.CharField(max_length=100)
    photo = models.FileField(storage=S3Boto3Storage())
    url = models.URLField()

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"
