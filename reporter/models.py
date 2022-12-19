from django.contrib.gis.db import models

# Create your models here.


class Incidence(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    object = models.Manager()

    def __str__(self):
        return self.name


class Airport(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fk_region = models.BigIntegerField()
    elev = models.FloatField()
    name = models.CharField(max_length=80)
    use = models.CharField(max_length=80)
    geom = models.MultiPointField(srid=4326)

    def __str__(self):
        return self.name
