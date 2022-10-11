from rest_framework.serializers import ModelSerializer
from App.models import Proyecto, Servicio


class ProyectoSerializer(ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ['nombre', 'descrip', 'fecha_inicio', 'activo', 'imagen', 'file', 'programa']


class ServicioSerializer(ModelSerializer):
    class Meta:
        model = Servicio
        fields = ['nombre', 'descrip', 'activo', 'imagen', 'file']
