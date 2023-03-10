# Generated by Django 4.1.4 on 2022-12-18 17:16

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fk_region', models.BigIntegerField()),
                ('elev', models.FloatField()),
                ('name', models.CharField(max_length=80)),
                ('use', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
