from django.shortcuts import render,redirect
from .models import Dojo

def index(request):
    return render(request, "index.html")
