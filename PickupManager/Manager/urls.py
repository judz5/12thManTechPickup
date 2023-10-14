from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("newOrder", views.newOrder, name='newOrder'),
    path("viewOrders", views.viewOrders, name='viewOrders')
]