# flights/serializers.py
from rest_framework import serializers
from .models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = "__all__"

# passengers/serializers.py
from rest_framework import serializers
from .models import Passenger
from flights.serializers import FlightSerializer

class PassengerSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)

    class Meta:
        model = Passenger
        fields = "__all__"