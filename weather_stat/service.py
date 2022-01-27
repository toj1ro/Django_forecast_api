import csv
from django.http import HttpResponse


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
