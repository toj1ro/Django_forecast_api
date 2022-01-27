from requests import request
from weather_stat.models import ForecastInCity
from Django_forecast_api.settings import OPENWEATHER_KEY, URL_BASE

CITIES = [
    'Shanghai',
    'Buenos Aires',
    'Mumbai',
    'Mexico City',
    'Karachi',
    'Istanbul',
    'Delhi',
    'Manila',
    'Moscow',
    'Dhaka',
    'Seoul',
    'Sao Paulo',
    'Lagos',
    'Jakarta',
    'Tokyo',
    'Zhumadian',
    'New York',
    'Taipei',
    'Kinshasa',
    'Lima',
    'Cairo',
    'London',
    'Beijing',
    'Tehran',
    'Nanchong',
    'Bogota',
    'Hong Kong',
    'Lahore',
    'Rio de Janeiro',
    'Baghdad',
    'Taian',
    'Bangkok',
    'Bangalore',
    'Yueyang',
    'Santiago',
    'Kaifeng',
    'Kolkata',
    'Toronto',
    'Yangon',
    'Sydney',
    'Chennai',
    'Riyadh',
    'Wuhan',
    'Petersburg',
    'Chongqing',
    'Chengdu',
    'Chittagong',
    'Alexandria',
    'Los Angeles',
    'Tianjin',
    'Melbourne',
    'Ahmadabad',
    'Pusan',
    'Abidjan',
    'Kano',
    'Hyderabad',
    'Puyang',
    'Yokohama-shi',
    'Ibadan',
    'Singapore',
    'Ankara',
    'Shenyang',
    'Ho Chi Minh',
    'Shiyan',
    'Cape Town',
    'Berlin',
    'Montreal',
    'Madrid',
    'Harbin',
    'Xian',
    'Pyongyang',
    'Lanzhou',
    'Guangzhou',
    'Casablanca',
    'Durban',
    'Nanjing',
    'Kabul',
    'Shenzhen',
    'Caracas',
    'Pune',
    'Surat',
    'Jeddah',
    'Kanpur',
    'Luanda',
    'Addis Ababa',
    'Nairobi',
    'Taiyuan',
    'Salvador',
    'Jaipur',
    'Dar es Salaam',
    'Chicago',
    'Incheon',
    'Yunfu',
    'Al Basrah',
    'Osaka-shi',
    'Mogadishu',
    'Taegu',
    'Rome',
    'Changchun',
    'Kiev',
]

OPENWEATHER_KEY = OPENWEATHER_KEY

URL_BASE = URL_BASE


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


def forecast_for_city() -> None:
    for city in CITIES:
        forecast_json = request(url=URL_BASE.format(city, OPENWEATHER_KEY), method='get').json()
        saving_in_db(forecast_json)


forecast_for_city()
