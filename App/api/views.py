from rest_framework.viewsets import ModelViewSet
from App.models import Proyecto, Servicio
from App.api.serializers import ProyectoSerializer, ServicioSerializer


# Create your views here.
class ProyectoApiViewSet(ModelViewSet):
    serializer_class = ProyectoSerializer
    queryset = Proyecto.objects.all()


class ServicioApiViewSet(ModelViewSet):
    serializer_class = ServicioSerializer
    queryset = Servicio.objects.all()
