from django.contrib import admin
from .models import Cubby, OrdType, Order

# Register your models here.

admin.site.register(Cubby)
admin.site.register(OrdType)
admin.site.register(Order)