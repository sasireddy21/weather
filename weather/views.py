from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from .helper import CustomPagination
from django.conf import settings
from .serializers import WeatherDataSerializer,WeatherAnalysisSerializer
from .models import WeatherData,WeatherAnalysis
from django.utils.dateparse import parse_date


class GetWeather(generics.ListAPIView):
    serializer_class = WeatherDataSerializer
    pagination_class = CustomPagination
    queryset = WeatherData.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.query_params.get('date', None)
        stationId = self.request.query_params.get('station_id', None)
        if date:
            parsedDate = parse_date(date)
            if parsedDate:
              queryset = queryset.filter(date=parsedDate)
            else:
              return queryset.none()
        
        if stationId:
            queryset = queryset.filter(station_id=stationId)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset() 
        serializer = self.get_serializer(queryset, many=True) 
        page = self.paginate_queryset(serializer.data) 

        if page is not None:
            return self.get_paginated_response(page)

        return Response(serializer.data) 

class GetWeatherAnalysis(generics.ListAPIView):
    serializer_class = WeatherAnalysisSerializer
    pagination_class = CustomPagination
    queryset = WeatherAnalysis.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        stationId = self.request.query_params.get('station_id', None)
        year = self.request.query_params.get('year', None)
        if stationId:
            queryset = queryset.filter(station_id=stationId)

        if year:
            queryset = queryset.filter(year=year)

        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset() 
        serializer = self.get_serializer(queryset, many=True) 
        page = self.paginate_queryset(serializer.data) 

        if page is not None:
            return self.get_paginated_response(page)

        return Response(serializer.data) 
