from rest_framework.routers import DefaultRouter
from App.api.views import ProyectoApiViewSet, ServicioApiViewSet

router_api=DefaultRouter()

router_api.register(prefix='proyectos', basename='proyectos', viewset=ProyectoApiViewSet)
router_api.register(prefix='servicios', basename='servicios', viewset=ServicioApiViewSet)