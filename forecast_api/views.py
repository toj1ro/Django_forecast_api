from django.core.cache import cache
from django.utils.encoding import force_str
from requests import request as req
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from Django_forecast_api.settings import OPENWEATHER_KEY, URL_FORECAST
from .service import forecast_request, chek_cache

OPENWEATHER_KEY = OPENWEATHER_KEY

URL_BASE = URL_FORECAST


class WeatherException(APIException):
    """
    Custom APIException to return proper message in case of error.
    """
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = 'A server error occurred.'

    def __init__(self, detail, status_code):
        if status_code is not None:
            self.status_code = status_code
        if detail is not None:
            self.detail = force_str(detail)


class ForecastDetail(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def check_request_parameters(request):
        if 'city' not in request.GET:
            raise WeatherException("No 'city' parameter", status.HTTP_400_BAD_REQUEST)
        elif 'temp_format' not in request.GET:
            raise WeatherException("No 'temp_format' parameter", status.HTTP_400_BAD_REQUEST)

        temp_format_parameter = request.GET['temp_format']

        if temp_format_parameter == 'C':
            temp_format = 'metric'
        elif temp_format_parameter == 'F':
            temp_format = 'imperial'
        else:
            temp_format = ''
        city = request.GET['city']
        return city, temp_format

    def get(self, request):
        if not request.user.is_authenticated:
            raise WeatherException('You not authorized', status.HTTP_401_UNAUTHORIZED)


        city, temp_format = self.check_request_parameters(request)

        forecast_json = chek_cache(city, temp_format)
        if forecast_json is None:
            forecast_json = forecast_request(city, temp_format)
        return Response(forecast_json)
