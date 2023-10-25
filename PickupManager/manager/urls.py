from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("newOrder", views.newOrder, name='newOrder'),
    path("viewOrders", views.viewOrders, name='viewOrders'),
    path("order/<int:pk>/", views.order_detail_view, name='order_detail'),
    path('delete/<int:pk>/', views.order_delete, name='order_delete')
]