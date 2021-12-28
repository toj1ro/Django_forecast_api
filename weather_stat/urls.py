from django.urls import path
from weather_stat.views import WeatherStat



urlpatterns = [
    path("", WeatherStat.as_view(),),
]