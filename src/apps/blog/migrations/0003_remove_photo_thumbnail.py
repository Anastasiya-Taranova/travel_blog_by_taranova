# Generated by Django 3.0.8 on 2020-07-11 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_photo_thumbnail"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="photo",
            name="thumbnail",
        ),
    ]
