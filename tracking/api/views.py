from django.db.models import Value
from django.contrib.gis.geos import LineString
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from .serializers import (TrackingSerializer, PropertySerializer,
                          VelocitySerializer)
from tracking.models import Tracking, Property

import datetime


class TrackingViewSet(viewsets.ModelViewSet):
    """
    Servicio que retorna las coordenadas de un houmer en particular.
    El houmer está identificado por un id, el cual es un parámetro obligatorio.
    """
    serializer_class = TrackingSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        id_houmer = self.request.query_params.get('id', None)
        queryset = Tracking.objects.filter(id=0)
        if id_houmer is not None:
            queryset = Tracking.objects.filter(id=id_houmer)

        return queryset


class PropertyViewSet(viewsets.ModelViewSet):
    """
    Servicio que retorna las propidades con sus coordenadas que visitó un
    houmer, además brinda el tiempo que permaneció en cada propiedad.
    """
    serializer_class = PropertySerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Property.objects.filter(id=0)
        id_houmer = self.request.query_params.get('id_houmer', None)
        date = self.request.query_params.get('date', None)
        if id_houmer is not None and date is not None:
            date_list = date.split('-')
            date = datetime.date(int(date_list[2]), int(date_list[1]),
                                 int(date_list[0]))
            tracking = Tracking.objects.filter(houmer_id=id_houmer,
                                               timestamp__date=date)
            line = LineString([t.position for t in tracking])
            queryset = Property.objects.filter(
                polygon__intersects=line).annotate(
                permanence_time=Value(0)).order_by('id')

            # add permanence time
            for q in queryset:
                tracking = tracking.filter(position__within=q.polygon)

                # tracking ordered for timestamp
                permanence_time = (tracking.first().timestamp -
                                   tracking.last().timestamp)
                q.permanence_time = permanence_time

        return queryset


class VelocityViewSet(viewsets.ModelViewSet):
    """
    Servicio que retorna todos los momentos en que el houmer se trasladó con
    una velocidad superior a cierto parámetro.
    http://localhost:8000/velocities/?id_houmer=1&date=04-12-2021&param=10
    """
    serializer_class = VelocitySerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        queryset = Tracking.objects.filter(id=0)
        id_houmer = self.request.query_params.get('id_houmer', None)
        date = self.request.query_params.get('date', None)
        param = self.request.query_params.get('param', None)
        if id_houmer is not None and date is not None and param is not None:
            date_list = date.split('-')
            date = datetime.date(int(date_list[2]), int(date_list[1]),
                                 int(date_list[0]))
            queryset = Tracking.objects.filter(houmer_id=id_houmer,
                                               timestamp__date=date,
                                               velocity__gte=param)

        return queryset
