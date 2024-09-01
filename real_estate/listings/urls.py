# airline_booking_system/urls.py
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from flights import views as flight_views
from passengers import views as passenger_views

router = DefaultRouter()
router.register(r"flights", flight_views.FlightViewSet, basename="flights")
router.register(r"passengers", passenger_views.PassengerViewSet, basename="passengers")

urlpatterns = [
    path("", include(router.urls)),
]