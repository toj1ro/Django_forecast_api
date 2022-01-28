from django.core.cache import cache
from django.utils.encoding import force_str
from requests import request as req
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from Django_forecast_api.settings import OPENWEATHER_KEY, URL_FORECAST
from .service import get_forecast
from .serializers import SerializerAPI

OPENWEATHER_KEY = OPENWEATHER_KEY

URL_BASE = URL_FORECAST


class ForecastDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = SerializerAPI(data=request.GET)

        data.is_valid(raise_exception=True)  # сделать один формат ошибки

        city = data.validated_data.get('city')
        temp_format = data.validated_data.get('temp_format')

        forecast_json = get_forecast(city, temp_format)

        return Response(forecast_json)
