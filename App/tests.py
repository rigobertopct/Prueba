from django.test import TestCase

from .models import Proyecto
from _datetime import date
proyectos=Proyecto.objects.all()
Estado_proyectos=[]
for c in proyectos:
    fecha=date(c.fecha_inicio.year,c.fecha_inicio.month,c.fecha_inicio.day)
    time=date.today()
    Estado_proyectos.append(time-fecha)
def data_templates(request):
    return {
        'estado':Estado_proyectos
    }
