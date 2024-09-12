from django.db import models
from django.utils import timezone
from stations.models import Station

class Passenger(models.Model):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def get_tickets(self):
        return self.tickets.all()  # Access related tickets

class Train(models.Model):
    train_number = models.CharField(max_length=20, unique=True)
    train_name = models.CharField(max_length=100)
    source = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='trains_as_source')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='trains_as_destination')
    journey_date = models.DateField()
    seats_available = models.PositiveIntegerField()

    def __str__(self):
        return f"Train {self.train_number} - {self.train_name}"

class Ticket(models.Model):
    pnr = models.CharField(max_length=20, unique=True)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, related_name='tickets')
    train = models.ForeignKey(Train, on_delete=models.CASCADE, related_name='tickets')
    journey_date = models.DateField()
    source = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='tickets_as_source')
    destination = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='tickets_as_destination')
    ticket_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=10, choices=[('Booked', 'Booked'), ('Cancelled', 'Cancelled')])
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Ticket {self.ticket_number} - PNR {self.pnr} - {self.passenger.user.email}"
