# Generated by Django 4.1.2 on 2022-11-12 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Modulo', '0008_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_carrera', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno2',
            fields=[
                ('matricula', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('turno', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('id_carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Modulo.carrera')),
            ],
        ),
    ]