from weather.views import GetWeather,GetWeatherAnalysis
from django.urls import path
#from rest_framework_simplejwt import views as jwt_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   # path('', index),
   # path("weather",GetWeather.as_view()),
    path("weather",GetWeather.as_view()),
    path("weather/stats",GetWeatherAnalysis.as_view()),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)