from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/token', obtain_auth_token, name='token'),
    path('api/auth/', include('djoser.urls')),
    path("api/weather_stat/", include('weather_stat.urls')),
    path("api/city_forecast/", include('forecast_api.urls')),

]
