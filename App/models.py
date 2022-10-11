import random

from django.db import models


# Create your models here.
from django.db.models.functions import datetime
from django.utils.datetime_safe import date


class Proyecto(models.Model):
    nombre=models.CharField(max_length=250, verbose_name="Nombre del pipProyecto")
    descrip=models.TextField(max_length=250, verbose_name="Descripción del Proyecto")
    fecha_inicio=models.DateField(verbose_name="Fecha de Inicio")
    activo=models.BooleanField(default=False)
    imagen=models.ImageField(upload_to='proyecto/', null= True, blank=True)
    file=models.FileField(upload_to='proyecto/Anexos1', null=True, blank=True)
    programa = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name="Programa", null=True, blank=True)


    def __str__(self):
        return self.nombre
    def porciento(self):
        return datetime.Now-self.fecha_inicio
    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        db_table='proyectos'


class Anexo(models.Model):
    proyecto = models.OneToOneField(
        Proyecto,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nombre_programa = models.CharField(max_length=250, verbose_name="Nombre del Programa")
    nombre_proyecto = models.CharField(max_length=250, verbose_name="Nombre del proyecto")
    codigo_proyecto = models.CharField(max_length=250, verbose_name="Código del proyecto")
    clasificacion_proyecto = models.TextField(verbose_name="Clasificación del proyecto")
    prioridad_establecida= models.TextField(verbose_name="PRIORIDAD ESTABLECIDA AL NIVEL QUE RESPONDE")
    financiamiento= models.TextField(verbose_name="FINANCIAMIENTO")
    resumen= models.TextField(verbose_name="Reumen del Proyecto")
    problem_resolver= models.TextField(verbose_name="Problemas a resolver")
    contexto= models.TextField(verbose_name="CONTEXTO, ANTECEDENTES Y JUSTIFICACIÓN DE PROYECTO")
    beneficiarios= models.TextField(verbose_name="BENEFICIARIOS DIRECTOS")
    clientes= models.TextField(verbose_name="CLIENTES o USUARIOS")
    objetivog= models.TextField(verbose_name="OBJETIVO GENERAL")
    objetivoe= models.TextField(verbose_name="OBJETIVOS ESPECÍFICOS")
    resultados= models.TextField(verbose_name="RESULTADOS")
    salidas= models.TextField(verbose_name="SALIDAS")
    impactos= models.TextField(verbose_name="IMPACTOS")
    riesgo= models.TextField(verbose_name="RIESGO IDENTIFICADO")
    acci_mitagacion= models.TextField(verbose_name="ACCIONES MITIGACIÓN")
    metodologia= models.TextField(verbose_name="METODOLOGÍAS. TECNOLOGÍAS, NORMAS Y MÉTODOS")

    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Anexo'
        verbose_name_plural='Anexos'
        db_table='anexos'

class Servicio(models.Model):
    nombre=models.CharField(max_length=250, verbose_name="Nombre del servicio")
    descrip=models.TextField(max_length=250, verbose_name="Descripción del servicio")
    activo=models.BooleanField(default=False)
    imagen=models.ImageField(upload_to='servicio/images', null= True, blank=True)
    file=models.FileField(upload_to='servicio/documento', null=True, blank=True)



    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
        db_table='servicios'





