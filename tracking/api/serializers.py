from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from tracking.models import Tracking, Property


class TrackingSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Tracking
        geo_field = "position"
        fields = ('timestamp', 'id', 'velocity')


class VelocitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Tracking
        fields = ('timestamp', 'id', 'velocity')


class PropertySerializer(GeoFeatureModelSerializer):
    permanence_time = serializers.CharField()

    class Meta:
        model = Property
        geo_field = 'polygon'
        fields = ('id', 'description', 'permanence_time')
