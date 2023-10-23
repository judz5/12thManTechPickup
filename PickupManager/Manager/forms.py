from django.forms import ModelForm
from django import forms
from .models import Order, OrdType, Cubby

class NewOrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['name', 'datePlaced', 'complete', 'cubby', 'orderType', 'pickupDate']
        widgets = {
            'datePlaced': forms.DateInput(attrs={'type': 'date'}),
            'pickupDate': forms.DateInput(attrs={'type': 'date', 'required': False})
        }

    cubby = forms.ModelChoiceField(queryset=Cubby.objects.order_by('location'))
    

class OrderSearchForm(forms.Form):
    name = forms.CharField(label="Name to Search", max_length = 100, required=False)