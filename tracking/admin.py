from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from tracking.models import Tracking, Houmer, Property


@gisadmin.register(Tracking)
class TrackingAdmin(gisadmin.OSMGeoAdmin):
    map_template = 'gis/admin/osm.html'
    default_lon = -7144296
    default_lat = -3682101
    openlayers_url = "https://cdnjs.cloudflare.com/ajax/libs/openlayers/"\
                     "2.13.1/OpenLayers.js"
    default_zoom = 12
    map_width = 1200
    map_height = 500


@admin.register(Houmer)
class HoumerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Houmer._meta.fields]


@admin.register(Property)
class PropertyAdmin(gisadmin.OSMGeoAdmin):
    map_template = 'gis/admin/osm.html'
    default_lon = -7144296
    default_lat = -3682101
    openlayers_url = "https://cdnjs.cloudflare.com/ajax/libs/openlayers/"\
                     "2.13.1/OpenLayers.js"
    default_zoom = 12
    map_width = 1200
    map_height = 500
