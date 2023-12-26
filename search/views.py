from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json
import logging

logger = logging.getLogger(__name__)


@login_required(login_url="/")
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required(login_url="/")
def getRideOptions(request):
    if request.method == "POST":
        logger.info("Received a post request for finding a driver")
        pickupLocation = request.POST['pickup-location']
        dropoffLocation = request.POST['dropoff-location']
        if pickupLocation == "" or dropoffLocation == "":
            logger.error("pickupLocation or dropoffLocation is empty")
            messages.error(request, "Enter both pickup and dropoff locations")
        else:
            data = json.load(open('search/json/rideOptions.json'))
            data_string = json.dumps(data)
            logger.info("Ride option data loaded")
            return render(request, 'dashboard.html', {'rideOptions': data_string})
    return redirect('/dashboard')


@login_required(login_url="/")
def rideStatus(request):
    rideOptionId = request.GET["id"]
    driver = None
    if (rideOptionId == "1"):
        driver = "Harrison Marquez"
    if (rideOptionId == "3"):
        driver = "Bernardo Barrera"
    if (rideOptionId == "4"):
        driver = "Matthew Park"
    logger.info("Driver allocated: " + driver)
    return render(request, 'rideStatus.html', context={'driver': driver})


def feedback(request):
    logger.info("Feedback submitted and saved in database")
    messages.info(request, "Thank you for submitting your feedback!")
    return redirect('/dashboard')
