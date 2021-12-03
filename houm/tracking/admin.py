from django.contrib import admin
from django.contrib.gis import admin as gisadmin
from tracking.models import *


@gisadmin.register(Tracking)
class TrackingAdmin(gisadmin.OSMGeoAdmin):
    """ admin para modelos con GIS """

    # el template de admin.OSMGeoAdmin que anda OK
    # map_srid = 3857  # al parecer la que usa gmaps
    # map_srid = 4326  # es otra opcion usada por google
    map_template = 'gis/admin/osm.html'  # el que incluye calles y ciudades de OSM
    # map_template = 'gis/admin/openlayers.html'  # vacio, el original
    # default_lat = -31
    # default_lon = -64
    default_lon = -7144296
    default_lat = -3682101
    # TODO: Eliminar en la migracion a Django v1.11
    openlayers_url = "https://cdnjs.cloudflare.com/ajax/libs/openlayers/2.13.1/OpenLayers.js"
    # Fin
    default_zoom = 12
    map_width = 1200
    map_height = 500

@admin.register(Houmer)
class HoumerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Houmer._meta.fields]

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Property._meta.fields]
