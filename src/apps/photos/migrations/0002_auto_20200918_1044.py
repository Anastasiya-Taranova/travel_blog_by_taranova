# Generated by Django 3.1.1 on 2020-09-18 10:44

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("photos", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="photos",
            options={"verbose_name": "Photo", "verbose_name_plural": "Photos"},
        ),
        migrations.AlterField(
            model_name="photos",
            name="url",
            field=models.URLField(),
        ),
    ]
