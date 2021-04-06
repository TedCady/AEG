from django.shortcuts import render, redirect
from .models import *
import bcrypt
from django.contrib import messages

def index(request):
    # if 'user_id' in request.session:
    #     del request.session['user_id']
    return render(request, "index.html")
