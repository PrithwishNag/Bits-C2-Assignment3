from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json

@login_required(login_url="/")
def dashboard(request):
    if request.method == "POST":
        pickupLocation = request.POST['pickup-location']
        dropoffLocation = request.POST['dropoff-location']
        if pickupLocation == "" or dropoffLocation == "":
            messages.error(request, "Enter both pickup and dropoff locations")
        else:
            data = json.load(open('search/json/rideOptions.json'))
            data_string = json.dumps(data)
            return render(request, 'dashboard.html', {'rideOptions': data_string})
    return render(request, 'dashboard.html')
