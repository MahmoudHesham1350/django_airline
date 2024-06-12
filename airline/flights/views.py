from django.shortcuts import render

from .models import Flight

# Create your views here.
def index(request):
    return render(request, "flights/index.html",{
        "flights": Flight.objects.all(),
    })

def flight(request, flight_id: int):
    flight = Flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html",{
        "flight": flight,
        "passengers": flight.passengers.all()
    })

def book(request, flight_id):
    raise("book function in flights/views.py not yet finished")

