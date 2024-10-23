# Generated by Django 4.1.5 on 2024-10-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(max_length=10)),
                ('year', models.IntegerField()),
                ('avg_max_temperature', models.FloatField(null=True)),
                ('avg_min_temperature', models.FloatField(null=True)),
                ('total_precipitation', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'weather_analysis',
            },
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('max_temperature', models.IntegerField(null=True)),
                ('min_temperature', models.IntegerField(null=True)),
                ('precipitation', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'weather_data',
                'unique_together': {('date', 'station_id')},
            },
        ),
    ]
