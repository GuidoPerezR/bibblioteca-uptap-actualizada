# Generated by Django 4.1.2 on 2023-03-11 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Modulo', '0007_librero_det_librero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='librero',
            name='id_usuario',
        ),
        migrations.DeleteModel(
            name='Det_Librero',
        ),
        migrations.DeleteModel(
            name='Librero',
        ),
    ]