from django.urls import path
from orders.views import checkout

app_name = "orders"

urlpatterns = [
    path('checkout/', checkout, name='checkout')
]
