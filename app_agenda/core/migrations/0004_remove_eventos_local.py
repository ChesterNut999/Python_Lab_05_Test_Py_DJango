# Generated by Django 3.2.5 on 2021-07-26 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210726_2019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventos',
            name='local',
        ),
    ]
