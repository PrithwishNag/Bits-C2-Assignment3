from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from .utils import registrationValidation
import logging

logger = logging.getLogger(__name__)


def login(request):
    logger.debug('Request came from: ' + request.get_host())
    logger.debug('User landed on loginPage')
    LOGIN_ERROR_MSG = "Login failed: invalid credentials"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        validationDetails = registrationValidation(username, password)
        if (not validationDetails[0]):
            logger.info('Unable to login: wrong credentials for ' + username)
            messages.error(request, LOGIN_ERROR_MSG)
        else:
            user = authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                logger.info('User logged in as ' + username)
                return redirect("/dashboard")
            else:
                logger.info('Unable to login: wrong credentials for ' + username)
                messages.error(request, LOGIN_ERROR_MSG)

    return render(request, 'loginPage.html')


def register(request):
    USERNMAME_ERROR_MSG = "Username is not a valid email"
    PASSWORD_ERROR_MSG = "Password entry does not meet criteria"
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        type = request.POST['type']

        validationDetails = registrationValidation(username, password)
        if (not validationDetails[0]):
            if (validationDetails[1] == 'username'):
                logger.error('Invalid email')
                messages.error(request, USERNMAME_ERROR_MSG)
            else:
                logger.error('Invalid password')
                messages.error(request, PASSWORD_ERROR_MSG)
        else:
            try:
                user = User.objects.create_user(username=username, email=None, password=password)
                user.type = type

                user.save()
                logger.info('Successfully created account for user')
                messages.success(request, "Your account has been successfully created")

            except Exception as error:
                logger.error('User model creation failed')
                messages.error(request, "Try another username")

    return render(request, 'registerPage.html')
