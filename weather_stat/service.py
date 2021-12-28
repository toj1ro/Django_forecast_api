import environ
from requests import request
from .models import ForecastInCity

env = environ.Env(
    DEBUG=(bool, False)
)

env.read_env('.env')

OPENWEATHER_KEY = env('OPENWEATHER_KEY')

URL_BASE = env('URL_WEATHER')

CITIES = []

with open("CITIES.txt") as countries:
    for country in countries:
        CITIES.append(country[:-1])


def saving_in_db(forecast_json: dict) -> None:
    if forecast_json['cod'] == 200:
        new_db_record = ForecastInCity(city_name=forecast_json['name'],
                                       temperature=forecast_json['main']['temp'],
                                       max_temperature=forecast_json['main']['temp_max'],
                                       min_temperature=forecast_json['main']['temp_min'],
                                       pressure=forecast_json['main']['pressure'],
                                       humidity=forecast_json['main']['humidity'],
                                       cloudiness=forecast_json['clouds']['all'],
                                       description=forecast_json['weather'][0]['description'],
                                       wind_speed=forecast_json['wind']['speed'],
                                       wind_degrees=forecast_json['wind']['deg']
                                       )

        new_db_record.save()
    else:
        print(forecast_json)


def forecast_for_city() -> None:
    for city in CITIES:
        forecast_json = request(url=URL_BASE.format(city, OPENWEATHER_KEY), method='get').json()
        saving_in_db(forecast_json)