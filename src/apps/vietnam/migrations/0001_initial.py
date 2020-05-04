# Generated by Django 3.0.5 on 2020-04-20 17:01

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Add",
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
                ("add", models.TextField(unique=True)),
                ("something", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="VieDays",
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
                ("day", models.IntegerField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("money", models.IntegerField(blank=True, null=True)),
                ("save", models.BooleanField()),
                (
                    "adds",
                    models.ManyToManyField(related_name="vieday", to="vietnam.Add"),
                ),
            ],
        ),
    ]