# Generated by Django 4.2.16 on 2024-12-13 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ficha_medica', '0002_alter_disponibilidad_options_disponibilidad_ocupada_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disponibilidad',
            options={'verbose_name': 'Disponibilidad', 'verbose_name_plural': 'Disponibilidades'},
        ),
    ]
