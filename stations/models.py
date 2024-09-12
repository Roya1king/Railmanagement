from django.db import models

class Station(models.Model):
    station_code = models.CharField(max_length=10, unique=True)
    station_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.station_name} ({self.station_code})"


