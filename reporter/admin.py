from django.contrib import admin
from .models import Incidence, Airport
from leaflet.admin import LeafletGeoAdmin

# Register your models here.


class IncidenceAdmin(LeafletGeoAdmin):
    pass
    list_display = ['name', 'location',]


class AirportAdmin(LeafletGeoAdmin):
    list_display = ['name', 'elev',]


admin.site.register(Incidence, IncidenceAdmin)
admin.site.register(Airport, AirportAdmin)
