from django.forms import ModelForm

from App.models import Proyecto
from App.models import Anexo
from App.models import Servicio


class ProyectoForm(ModelForm):
    class Meta:
        model=Proyecto
        fields='__all__'

class AnexoForm(ModelForm):
    class Meta:
        model = Anexo
        fields = '__all__'

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'
