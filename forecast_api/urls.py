from django.urls import path

from forecast_api.views import ForecastDetail

urlpatterns = [
    path("", ForecastDetail.as_view(), ),
]
