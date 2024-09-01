# flights/admin.py
from django.contrib import admin
from .models import Flight

class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'departure', 'arrival', 'origin', 'destination', 'capacity')
    list_filter = ('origin', 'destination')
    search_fields = ('flight_number', 'origin', 'destination')

admin.site.register(Flight, FlightAdmin)