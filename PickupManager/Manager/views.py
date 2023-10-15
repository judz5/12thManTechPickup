from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.template import loader
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

def viewOrders(request, pk):
    orders = Order.objects.all()
    searchForm = OrderSearchForm(request.GET)

    if(searchForm.is_valid()):
        name = searchForm.cleaned_data.get('name')
        if name:
            orders = orders.filter(name__icontains=name) # case insensitive
    
    if request.method == 'DELETE':
        Order.objects.get(pk=request.DELETE['delete-id']).delete()

    return render(request, 'viewOrders.html', {'orders': orders, 'searchForm': searchForm})

