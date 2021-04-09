from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

def home(request):
    # if 'user_id' in request.session:
    #     del request.session['user_id']
    return render(request, "Home.html")


def teams(request):

    return render(request, "Teams.html")


def partners(request):

    return render(request, "Partners.html")


def calendar(request):

    return render(request, "Calendar.html")


def contact(request):

    return render(request, "Contact.html")