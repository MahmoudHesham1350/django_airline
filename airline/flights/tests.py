
from django.db.models import Max
from django.test import Client, TestCase

from .models import Airport, Flight, Passenger
# Create your tests here.

class FlightTestCase(TestCase):

    def setUp(self):

        # Creating Airports
        port1 = Airport.objects.create(code="AAA", city="City A")
        port2 = Airport.objects.create(code="BBB", city="City B")

        # Create Flights
        Flight.objects.create(origin=port1, destination=port2, duration=100)
        Flight.objects.create(origin=port1, destination=port1, duration=200)
        Flight.objects.create(origin=port1, destination=port2, duration=-100)

    def test_departures_count(self):
        port = Airport.objects.get(code="AAA")
        self.assertEqual(port.departures.count(), 3)

    def test_arrivals_count(self):
        port = Airport.objects.get(code="AAA")
        self.assertEqual(port.arrivals.count(), 1)

    def test_valid_flight(self):
        port1 = Airport.objects.get(code="AAA")
        port2 = Airport.objects.get(code="BBB")
        flight = Flight.objects.get(origin=port1, destination=port2, duration=100)
        self.assertTrue(flight.is_valid_flight())
    
    def test_invalid_flight(self):
        port1 = Airport.objects.get(code="AAA")
        flight = Flight.objects.get(origin=port1, destination=port1)
        self.assertFalse(flight.is_valid_flight())

    def test_invalid_duration(self):
        port1 = Airport.objects.get(code="AAA")
        port2 = Airport.objects.get(code="BBB")
        flight = Flight.objects.get(origin=port1, destination=port2, duration=-100)
        self.assertFalse(flight.is_valid_flight())

    def test_index(self):
        dummyClient = Client()
        response = dummyClient.get("/flights/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["flights"].count(), 3)

    def test_valid_flight_page(self):
        port1 = Airport.objects.get(code="AAA")
        flight = Flight.objects.get(origin=port1, destination=port1)
        
        dummyClient = Client()
        response = dummyClient.get(f"/flights/{flight.id}")
        self.assertEqual(response.status_code, 200)

    def test_invalid_flight_page(self):
        max_id = Flight.objects.all().aggregate(Max("id"))["id__max"]
          
        dummyClient = Client()
        response = dummyClient.get(f"/flights/{max_id + 1}")
        self.assertEqual(response.status_code, 404)

    def test_flight_page_passengers(self):
        flight = Flight.objects.get(pk=1)
        passenger = Passenger.objects.create(first="Alice", last="Adams")
        flight.passengers.add(passenger)
    
        dummyClient = Client()
        response = dummyClient.get(f"/flights/{flight.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["passengers"].count(), 1)
    
    def test_flight_page_non_passengers(self):
        flight = Flight.objects.get(pk=1)
        passenger = Passenger.objects.create(first="Alice", last="Adams")
    
        dummyClient = Client()
        response = dummyClient.get(f"/flights/{flight.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["non_passengers"].count(), 1)
