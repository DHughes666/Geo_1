# Generated by Django 4.1.4 on 2022-12-19 01:53

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporter', '0002_airport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
        ),
    ]
