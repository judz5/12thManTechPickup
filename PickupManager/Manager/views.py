from django.shortcuts import render, redirect, HttpResponse
from django.template import loader
from .forms import NewOrderForm
from .models import Cubby, Order, OrdType


# Create your views here.
def home(request):
    return render(request, 'home.html')

def newOrder(request):
    if request.POST:
        form = NewOrderForm(request.POST)
        if form.is_valid():
            print("valid form")
            form.save()
        return redirect(home)
    return render(request, 'newOrder.html', {"form": NewOrderForm})