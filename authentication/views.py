from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from .utils import registrationValidation

def login(request):

    LOGIN_ERROR_MSG = "Login failed: invalid credentials" 
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        validationDetails = registrationValidation(username, password)
        if(not validationDetails[0]):
            messages.error(request, LOGIN_ERROR_MSG)
        else:
            user = authenticate(username=username, password=password)

            if user is not None:
                return redirect("dashboard")
            else:
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
        if(not validationDetails[0]):
            if(validationDetails[1] == 'username'):
                messages.error(request, USERNMAME_ERROR_MSG)
            else:
                messages.error(request, PASSWORD_ERROR_MSG)
        else:
            try:
                user = User.objects.create_user(username=username, email=None, password=password)
                user.type = type

                user.save()
                messages.success(request, "Your account has been successfully created")

            except:
                messages.error(request, "Try another username")

    return render(request, 'registerPage.html')