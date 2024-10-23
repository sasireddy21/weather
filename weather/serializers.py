from rest_framework import serializers
from .models import WeatherData, WeatherAnalysis


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__' 

class WeatherAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherAnalysis
        fields = '__all__'
