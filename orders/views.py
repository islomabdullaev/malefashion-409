from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from orders.models import OrderItemModel, OrderModel
from products.models import CouponModel, ProductModel

# Create your views here.

def checkout(request):
    if request.method == "POST":
        cart = request.session.get("cart", [])
        total_price = request.GET.get("total_price")
        code = request.GET.get("code")
        if not cart:
            return HttpResponse("Cart is empty !")
        products = ProductModel.get_from_cart(cart)
        order = OrderModel.objects.create(user=request.user, total_price=0.0)
        if total_price:
            order.total_price = total_price
            order.save()
        if code:
            coupon = CouponModel.objects.get(code=code)
            coupon.is_active = False
            coupon.save()
        for product in products:
            OrderItemModel.objects.create(order=order, product=product, quantity=1)
        messages.add_message(request, messages.SUCCESS, "Order Created Successfully !")
        request.session['cart'] = []
    return redirect("pages:cart")