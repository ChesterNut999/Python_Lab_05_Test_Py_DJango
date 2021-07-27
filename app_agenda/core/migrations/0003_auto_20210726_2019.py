# Generated by Django 3.2.5 on 2021-07-26 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210726_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='local',
            field=models.TextField(blank=True, null=True, verbose_name='Local/Endereço'),
        ),
        migrations.AlterField(
            model_name='eventos',
            name='data_criacao',
            field=models.DateTimeField(auto_now=True, verbose_name='Data de criação do evento'),
        ),
    ]