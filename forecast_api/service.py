from Django_forecast_api.settings import OPENWEATHER_KEY, URL_FORECAST
from requests import request as req
from django.core.cache import cache

OPENWEATHER_KEY = OPENWEATHER_KEY

URL_BASE = URL_FORECAST



def chek_cache(city, temp_format):
    cache_ = cache.get(city + temp_format)
    return cache_

def forecast_request(city, temp_format):
    forecast_json = req(url=URL_BASE.format(city, temp_format, OPENWEATHER_KEY), method='get').json()
    return forecast_json