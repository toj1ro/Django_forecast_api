import csv
import threading
from django.core.validators import ValidationError
from django import views
from django.http import HttpResponse, HttpResponseBadRequest
import schedule
from .models import ForecastInCity
from .service import forecast_for_city



class WeatherStat(views.View):
    @staticmethod
    def csv_writer(query_set):
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': "attachment; filename=weather_in_cities.csv"},
        )

        writer = csv.writer(response)
        writer.writerow(
            ['City', 'DateTime', 'Temperature', 'Max temperature', 'Min temperature', 'Pressure', 'Humidity',
             'Cloudiness', 'Description', 'Wind speed', 'Wind degrees'])

        for record in query_set:
            writer.writerow(
                [record.city_name, record.datetime, record.temperature, record.max_temperature, record.min_temperature,
                 record.pressure, record.humidity, record.cloudiness, record.description, record.wind_speed,
                 record.wind_degrees])

        return response

    def get(self, request):

        if 'start_time' not in request.GET:
            return HttpResponseBadRequest('No "start_time" parameter')

        if 'end_time' not in request.GET:
            return HttpResponseBadRequest('No "end_time" parameter')

        start_time = request.GET['start_time']
        end_time = request.GET['end_time']

        try:
            query_set = ForecastInCity.objects.filter(datetime__range=[start_time, end_time])
        except ValidationError:
            return HttpResponseBadRequest(
                'The requested date and/or time have an incorrect format.'
                'The correct format should be YYYY-MM-DDTHH:MM:SS.')

        response = self.csv_writer(query_set)

        return response
