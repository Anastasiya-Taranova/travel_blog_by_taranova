# Generated by Django 3.1.1 on 2020-09-22 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("trips", "0003_auto_20200922_0716"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Country",
        ),
        migrations.DeleteModel(
            name="Marker",
        ),
    ]
