# Generated by Django 4.0.6 on 2022-07-13 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_fichaproyecto_remove_proyecto_duracion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anexo',
            fields=[
                ('proyecto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='App.proyecto')),
                ('nombre_programa', models.CharField(max_length=250, verbose_name='Nombre del Programa')),
                ('nombre_proyecto', models.CharField(max_length=250, verbose_name='Nombre del proyecto')),
                ('codigo_proyecto', models.CharField(max_length=250, verbose_name='Código del proyecto')),
                ('clasificacion_proyecto', models.TextField(verbose_name='Clasificación del proyecto')),
                ('prioridad_establecida', models.TextField(verbose_name='PRIORIDAD ESTABLECIDA AL NIVEL QUE RESPONDE')),
                ('financiamiento', models.TextField(verbose_name='FINANCIAMIENTO')),
                ('resumen', models.TextField(verbose_name='Reumen del Proyecto')),
                ('problem_resolver', models.TextField(verbose_name='Problemas a resolver')),
                ('contexto', models.TextField(verbose_name='CONTEXTO, ANTECEDENTES Y JUSTIFICACIÓN DE PROYECTO')),
                ('beneficiarios', models.TextField(verbose_name='BENEFICIARIOS DIRECTOS')),
                ('clientes', models.TextField(verbose_name='CLIENTES o USUARIOS')),
                ('objetivog', models.TextField(verbose_name='OBJETIVO GENERAL')),
                ('objetivoe', models.TextField(verbose_name='OBJETIVOS ESPECÍFICOS')),
                ('resultados', models.TextField(verbose_name='RESULTADOS')),
                ('salidas', models.TextField(verbose_name='SALIDAS')),
                ('impactos', models.TextField(verbose_name='IMPACTOS')),
                ('riesgo', models.TextField(verbose_name='RIESGO IDENTIFICADO')),
                ('acci_mitagacion', models.TextField(verbose_name='ACCIONES MITIGACIÓN')),
                ('metodologia', models.TextField(verbose_name='METODOLOGÍAS. TECNOLOGÍAS, NORMAS Y MÉTODOS')),
            ],
            options={
                'verbose_name': 'Anexo',
                'verbose_name_plural': 'Anexos',
                'db_table': 'anexos',
            },
        ),
        migrations.DeleteModel(
            name='FichaProyecto',
        ),
    ]
