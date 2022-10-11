from django.contrib import admin

# Register your models here.
from App.models import Proyecto
from App.models import Anexo
from App.models import Servicio


admin.site.register(Proyecto)
admin.site.register(Anexo)
admin.site.register(Servicio)