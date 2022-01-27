from django.db import models


class ForecastInCity(models.Model):
    """
    Represents the weather forecast associated to the cities
    """
    city_name = models.CharField(max_length=100)
    datetime = models.DateTimeField(auto_now_add=True)
    # temperatures saved with Unit as Celsius
    temperature = models.FloatField()
    max_temperature = models.FloatField(null=True)
    min_temperature = models.FloatField(null=True)
    # pressures saved with unit as Atmospheric pressure (hPa)
    pressure = models.FloatField()
    # humidity and cloudiness as percentage
    humidity = models.FloatField()
    cloudiness = models.FloatField(null=True)
    description = models.CharField(max_length=250)
    # wind speed as meter/sec
    wind_speed = models.FloatField(null=True)
    wind_degrees = models.FloatField(null=True)

    def __str__(self):
        return 'Forecast for {} on {}'.format(self.city_name,
                                              str(self.datetime), )