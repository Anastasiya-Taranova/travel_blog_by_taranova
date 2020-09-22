# Generated by Django 3.1.1 on 2020-09-22 07:14

import django_2gis_maps.fields
import django_2gis_maps.mixins
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("trips", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Markerttttt",
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
                ("address", django_2gis_maps.fields.AddressField(max_length=100)),
            ],
            bases=(django_2gis_maps.mixins.DoubleGisMixin, models.Model),
        ),
    ]
