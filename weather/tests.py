from django.test import TestCase
from .models import WeatherAnalysis

class WeatherAnalysisModelTest(TestCase):

    def setUp(self):
        WeatherAnalysis.objects.create(
            station_id='123',
            year='2023',
            avg_max_temperature=25.0,
            avg_min_temperature=15.0,
            total_precipitation=2.5
        )

    def test_weather_analysis_creation(self):
        weather = WeatherAnalysis.objects.get(station_id='123')
        self.assertEqual(weather.avg_max_temperature, 25.0)
        self.assertEqual(weather.avg_min_temperature, 15.0)
        self.assertEqual(weather.total_precipitation, 2.5)