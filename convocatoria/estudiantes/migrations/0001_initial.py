# Generated by Django 5.1.1 on 2024-12-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id_estudiante', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('facultad', models.CharField(max_length=100)),
                ('estado_convocatoria', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Elegible', 'Elegible'), ('No Elegible', 'No Elegible')], default='Pendiente', max_length=50)),
            ],
        ),
    ]
