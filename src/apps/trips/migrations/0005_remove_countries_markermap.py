# Generated by Django 3.1.1 on 2020-09-22 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("trips", "0004_auto_20200922_0717"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="countries",
            name="markermap",
        ),
    ]
