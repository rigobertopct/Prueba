from .models import Proyecto, Servicio, Anexo
from _datetime import date
proyectos=Proyecto.objects.all()
servicios=Servicio.objects.all()
anexos=Anexo.objects.all()
contratos=321
Estado_proyectos=[]
for c in proyectos:
    fecha=date(c.fecha_inicio.year,c.fecha_inicio.month,c.fecha_inicio.day)
    time=date.today()
    Estado_proyectos.append(time-fecha)
def data_templates(request):
    return {
        'estado':Estado_proyectos,
        'proyectos': proyectos.count(),
        'servicios': servicios.count(),
        'contratos': contratos,
        'encuentros': anexos.count(),
    }