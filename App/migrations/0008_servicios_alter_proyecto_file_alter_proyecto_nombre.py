# Generated by Django 4.1 on 2022-08-27 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_proyecto_programa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre del servicio')),
                ('descrip', models.TextField(max_length=250, verbose_name='Descripción del servicio')),
                ('activo', models.BooleanField(default=False)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='servicio/images')),
                ('file', models.FileField(blank=True, null=True, upload_to='servicio/documento')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'db_table': 'servicios',
            },
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='proyecto/Anexos1'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(max_length=250, verbose_name='Nombre del pipProyecto'),
        ),
    ]
