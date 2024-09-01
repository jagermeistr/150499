# flights/models.py
from django.db import models

class Flight(models.Model):
    flight_number = models.CharField(max_length=255, unique=True)
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    origin = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    capacity = models.IntegerField()

    def __str__(self):
        return self.flight_number

# passengers/models.py
from django.db import models
from flights.models import Flight

class Passenger(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=255)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"