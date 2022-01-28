from Django_forecast_api.settings import OPENWEATHER_KEY, URL_FORECAST
from requests import request as req
from django.core.cache import cache

OPENWEATHER_KEY = OPENWEATHER_KEY

URL_BASE = URL_FORECAST


def forecast_request(city, temp_format):
    forecast_json = req(url=URL_BASE.format(city, temp_format, OPENWEATHER_KEY), method='get').json()
    return forecast_json


def get_forecast(city, temp_format):

    forecast_json =   cache.get(city + temp_format)

    if forecast_json is None:
        forecast_json = forecast_request(city, temp_format) # Сделать исключение чтобы не кешировалась ошибка
        cache.set(city + temp_format, forecast_json)

    return forecast_json

