from django.db import models

class WeatherData(models.Model):
    station_id = models.CharField(max_length=10)
    date = models.DateField()
    max_temperature = models.IntegerField(null=True)
    min_temperature = models.IntegerField(null=True)
    precipitation = models.IntegerField(null=True)

    class Meta:
        db_table = 'weather_data'
        unique_together = ('date', 'station_id')


class WeatherAnalysis(models.Model):
    station_id = models.CharField(max_length=10)
    year = models.IntegerField()
    avg_max_temperature = models.FloatField(null=True)
    avg_min_temperature = models.FloatField(null=True)
    total_precipitation = models.FloatField(null=True)
    class Meta:
        db_table = 'weather_analysis'