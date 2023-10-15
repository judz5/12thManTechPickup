from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.template import loader
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .forms import NewOrderForm, OrderSearchForm
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

def viewOrders(request):
    orders = Order.objects.all()
    searchForm = OrderSearchForm(request.GET)

    if(searchForm.is_valid()):
        name = searchForm.cleaned_data.get('name')
        if name:
            orders = orders.filter(name__icontains=name) # case insensitive
    
    return render(request, 'viewOrders.html', {'orders': orders, 'searchForm': searchForm})


