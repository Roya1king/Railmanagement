from django.db import models
from django.utils import timezone

class Schedule(models.Model):
    train = models.ForeignKey('reservations.Train', on_delete=models.CASCADE, related_name='schedules')
    departure_station = models.ForeignKey('stations.Station', on_delete=models.CASCADE, related_name='departure_schedules')
    arrival_station = models.ForeignKey('stations.Station', on_delete=models.CASCADE, related_name='arrival_schedules')
    departure_time = models.DateTimeField(default=timezone.now)
    arrival_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"Train {self.train.train_number} - {self.departure_station.station_name} to {self.arrival_station.station_name}"
