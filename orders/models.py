from django.db import models
from django.contrib.auth.models import User

from orders.choices import OrderStatus
from products.models import ProductModel

# Create your models here.

class OrderModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=24, choices=OrderStatus.choices,
        default=OrderStatus.pending.value)
    total_price = models.FloatField(default=0.0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"#{self.pk}: {self.user}|{self.status}|{self.total_price}"
    
    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"#{self.order.pk}|{self.product.name}|{self.quantity}"
    
    class Meta:
        verbose_name = "Order Item"
        verbose_name_plural = "Order Items"
