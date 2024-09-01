# 150499
Assignment
Project Setup
Clone the Repository:
--git clone

Create a Virtual Environment:
--python -m venv venv

Activate the Virtual Environment:

On Windows:
--venv\Scripts\activate

Install Dependencies:
--pip install -r requirements.txt
--pip install django djangorestframework

Create and Apply Migrations:
--python manage.py makemigrations
--python manage.py migrate



Running the Project
--python manage.py runserver
--Visit http://127.0.0.1:8000/ in your browser to access the application.
--For the admin interface, navigate to http://127.0.0.1:8000/admin/.

Models

The models are designed to represent the data structures used in the airline booking system. There are two models: Flight and Passenger.

Flight: This model represents a flight in the airline system. It has the following fields:
flight_number: A unique identifier for the flight.
departure: The date and time of departure.
arrival: The date and time of arrival.
origin: The origin airport.
destination: The destination airport.
capacity: The total number of seats available on the flight.
Passenger: This model represents a passenger in the system. It has the following fields:
first_name: The first name of the passenger.
last_name: The last name of the passenger.
email: The unique email address of the passenger.
phone_number: The contact number of the passenger.
flight: A foreign key referencing the Flight model, which relates the passenger to a specific flight.
Serializers

The serializers are used to convert the data from the models into a format that can be easily consumed by the API. There are two serializers: FlightSerializer and PassengerSerializer.

FlightSerializer: This serializer is used to serialize the Flight model. It includes all the fields from the model.
PassengerSerializer: This serializer is used to serialize the Passenger model. It includes all the fields from the model, as well as a nested FlightSerializer to represent the related flight.
Views/ViewSets

The views/viewsets are used to define the API endpoints and handle the CRUD operations. There are two viewsets: FlightViewSet and PassengerViewSet.

FlightViewSet: This viewset is used to handle the CRUD operations for the Flight model. It provides endpoints for listing all flights, retrieving a single flight, creating a new flight, updating an existing flight, and deleting a flight.
PassengerViewSet: This viewset is used to handle the CRUD operations for the Passenger model. It provides endpoints for listing all passengers, retrieving a single passenger, creating a new passenger, updating an existing passenger, and deleting a passenger.
