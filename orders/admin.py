from django.contrib import admin

from orders.models import OrderItemModel, OrderModel

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model = OrderItemModel

@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "total_price", "status", "created_at"]
    inlines = [OrderItemInline]