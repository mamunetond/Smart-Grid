# Generated by Django 4.2.4 on 2023-11-21 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_Trip', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='consumo_ajustado1',
            new_name='Abril',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='consumo_ajustado2',
            new_name='Agosto',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='consumo_ajustado3',
            new_name='Diciembre',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='distancia1',
            new_name='Enero',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='distancia2',
            new_name='Febrero',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='distancia3',
            new_name='Julio',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='duracion1',
            new_name='Junio',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='duracion2',
            new_name='Marzo',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='duracion3',
            new_name='Mayo',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='porcentaje_bateria1',
            new_name='Noviembre',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='porcentaje_bateria2',
            new_name='Octubre',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='porcentaje_bateria3',
            new_name='Septiembre',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='ruta1_id',
            new_name='ruta_id',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='ruta2_id',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='ruta3_id',
        ),
        migrations.AddField(
            model_name='trip',
            name='Statistics_id',
            field=models.IntegerField(default=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='carga_restante',
            field=models.IntegerField(default=75),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='consumo_ajustado',
            field=models.IntegerField(default=185),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='consumo_total',
            field=models.IntegerField(default=2350),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='distancia',
            field=models.IntegerField(default=17000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='duracion',
            field=models.IntegerField(default=1200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='fecha',
            field=models.DateField(default='2023-11-21'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='porcentaje_bateria',
            field=models.IntegerField(default=85),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='porcentaje_consumido',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
    ]