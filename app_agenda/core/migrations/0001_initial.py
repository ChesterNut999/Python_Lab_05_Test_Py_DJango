# Generated by Django 3.2.5 on 2021-07-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_evento', models.DateTimeField()),
                ('data_criacao', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Eventos',
            },
        ),
    ]
