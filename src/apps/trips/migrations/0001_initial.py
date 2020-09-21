# Generated by Django 3.1.1 on 2020-09-21 16:15

from django.db import migrations, models
import django.db.models.deletion
import storages.backends.s3boto3
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Content',
            },
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=20, null=True)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='PointsMap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.TextField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'Points',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('original', models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage(), upload_to='')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='trips.content')),
            ],
            options={
                'verbose_name_plural': 'Photos',
            },
        ),
        migrations.AddField(
            model_name='content',
            name='country_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country', to='trips.countries'),
        ),
        migrations.AddField(
            model_name='content',
            name='points',
            field=models.ManyToManyField(to='trips.PointsMap'),
        ),
    ]
