# Generated by Django 3.0.6 on 2020-05-22 19:00

import uuid

import django.db.models.deletion
import storages.backends.s3boto3
from django.conf import settings
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.TextField(blank=True, null=True)),
                ("content", models.TextField(blank=True, null=True)),
                ("nr_likes", models.IntegerField(blank=True, null=True)),
                ("nr_dislikes", models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "original",
                    models.FileField(
                        storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to=""
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="blog.Post",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nr_likes", models.IntegerField(blank=True, null=True)),
                ("nr_dislikes", models.IntegerField(blank=True, null=True)),
                ("message", models.TextField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="blog.Post",
                    ),
                ),
            ],
        ),
    ]
