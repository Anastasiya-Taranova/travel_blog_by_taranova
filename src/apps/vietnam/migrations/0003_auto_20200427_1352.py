# Generated by Django 3.0.5 on 2020-04-27 13:52

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("vietnam", "0002_auto_20200420_1800"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="responsibility",
            name="vieday",
        ),
        migrations.RemoveField(
            model_name="viedays",
            name="adds",
        ),
        migrations.RemoveField(
            model_name="viedays",
            name="day",
        ),
        migrations.RemoveField(
            model_name="viedays",
            name="money",
        ),
        migrations.AddField(
            model_name="viedays",
            name="h2",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="viedays",
            name="h3",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="viedays",
            name="predecription",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name="Add",
        ),
        migrations.DeleteModel(
            name="Responsibility",
        ),
    ]
