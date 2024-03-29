"""
URL configuration for rideshare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from authentication import views as auth_view
from search import views as search_view

urlpatterns = [
    path('', auth_view.login),
    path('register', auth_view.register),
    path('dashboard', search_view.dashboard),
    path('dashboard/getRideOptions', search_view.getRideOptions),
    path('rideStatus', search_view.rideStatus),
    path('rideStatus/feedback', search_view.feedback),
]
