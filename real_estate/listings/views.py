# flights/views.py
from rest_framework import viewsets
from .models import Flight
from .serializers import FlightSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

# passengers/views.py
from rest_framework import viewsets
from .models import Passenger
from .serializers import PassengerSerializer

class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer