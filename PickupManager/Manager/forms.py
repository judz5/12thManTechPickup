from django.forms import ModelForm
from django import forms
from .models import Order, OrdType, Cubby

class NewOrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'datePlaced', 'complete', 'cubby', 'orderType', 'pickupDate']
        widgets = {
            'datePlaced': forms.DateInput(attrs={'type': 'date'}),
            'pickupDate': forms.DateInput(attrs={'type': 'date'})
        }