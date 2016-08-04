from django.contrib.gis import admin
from .models import MDoutpoint, outpointMD
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

admin.site.register(MDoutpoint, LeafletGeoAdmin)
admin.site.register(outpointMD, LeafletGeoAdmin)