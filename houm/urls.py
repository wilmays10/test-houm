from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tracking.api.views import (TrackingViewSet, PropertyViewSet,
                                VelocityViewSet)

router = routers.DefaultRouter()
router.register('trackings', TrackingViewSet, basename='tracking.api.lista')
router.register('properties', PropertyViewSet, basename='property.api.lista')
router.register('velocities', VelocityViewSet, basename='velocity.api.lista')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
