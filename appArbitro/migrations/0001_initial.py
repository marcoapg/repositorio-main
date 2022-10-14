# Generated by Django 4.1.1 on 2022-09-30 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='arbitro',
            fields=[
                ('arbitro_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('tipo_arbitro', models.CharField(choices=[('P', 'Principal'), ('J', 'Juez de Linea'), ('C', 'Cuarto Hombre'), ('V', 'Var')], default='P', max_length=1)),
                ('estado', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'arbitro',
            },
        ),
        migrations.CreateModel(
            name='terna_arbitral',
            fields=[
                ('terna_arbitral_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_terna', models.CharField(max_length=50)),
                ('estado', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'terna_arbitral',
            },
        ),
        migrations.CreateModel(
            name='tipo_terna',
            fields=[
                ('tipo_terna_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30)),
                ('siglas', models.CharField(max_length=3)),
            ],
            options={
                'verbose_name_plural': 'tipo_terna',
            },
        ),
        migrations.CreateModel(
            name='detalle_terna',
            fields=[
                ('detalle_terna_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('estado_juego', models.BooleanField()),
                ('arbitro_id', models.ForeignKey(db_column='arbitro_id', on_delete=django.db.models.deletion.CASCADE, to='appArbitro.arbitro')),
                ('terna_arbitral_id', models.ForeignKey(db_column='terna_arbitral_id', on_delete=django.db.models.deletion.CASCADE, to='appArbitro.terna_arbitral')),
                ('tipo_terna_id', models.ForeignKey(db_column='tipo_terna_id', on_delete=django.db.models.deletion.CASCADE, to='appArbitro.tipo_terna')),
            ],
            options={
                'verbose_name_plural': 'detalle_terna',
            },
        ),
    ]