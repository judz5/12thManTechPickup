from django.shortcuts import render, redirect, HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    return render(request, 'home.html')
