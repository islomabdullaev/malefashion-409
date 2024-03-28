from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages

from orders.models import OrderItemModel, OrderModel
from products.models import CouponModel, ProductModel

# Create your views here.

def checkout(request):
    if request.method == "POST":
        cart = request.session.get("data", [])
        total_price = request.GET.get("total_price")
        code = request.GET.get("code")
        if not cart:
            return HttpResponse("Cart is empty !")
        products = []
        for cart_data in cart:
            data = {
                "product": ProductModel.objects.get(pk=cart_data['pk']),
                "quantity": cart_data['quantity']
            }
            products.append(data)
        order = OrderModel.objects.create(user=request.user, total_price=0.0)
        if total_price:
            order.total_price = total_price
            order.save()
        if code:
            coupon = CouponModel.objects.get(code=code)
            coupon.is_active = False
            coupon.save()
        for data in products:
            OrderItemModel.objects.create(order=order, product=data['product'], quantity=data['quantity'])
        messages.add_message(request, messages.SUCCESS, "Order Created Successfully !")
        request.session['data'] = []
    return redirect("pages:cart")