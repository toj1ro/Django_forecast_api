from django import views
from django.http import HttpResponseBadRequest
from .forms import DateTimeForm
from .models import ForecastInCity
from .service import csv_writer


class WeatherStat(views.View):

    def get_records_from_db(self, start_time, end_time):
        query_set = ForecastInCity.objects.filter(datetime__range=[start_time, end_time])
        return query_set

    def get(self, request):
        datetime = DateTimeForm(request.GET)

        if not datetime.is_valid():
            return HttpResponseBadRequest(datetime.errors.as_json(), content_type='application/json')

        start_time = datetime.clean_start_time()
        end_time = datetime.clean_end_time()
        query_set = self.get_records_from_db(start_time, end_time)
        response = csv_writer(query_set)
        return response
