from django import template
from django.db.models import Sum

from products.models import ProductModel, WishlistModel

register = template.Library()


@register.filter(name="in_wishlist")
def in_wishlist(user, product):
    return WishlistModel.objects.filter(user=user, product=product).exists()

@register.simple_tag
def get_cart_info(request, coupon=None):
    cart_data = request.session.get("data", [])
    if not cart_data:
        return 0, 0.0
    quantity = len(cart_data)
    total_price = 0
    products = []
    for data in cart_data:
        product_data = {
            "product": ProductModel.objects.get(pk=data['pk']),
            "quantity": data['quantity']
        }
        products.append(product_data)
    for data in products:
        total_price += (data['product'].get_real_price() * float(data['quantity']))
    if coupon:
        total_price = total_price - ((total_price / 100) * coupon.discount)
    return quantity, total_price

@register.filter(name='in_cart')
def in_cart(request, pk):
    cart = request.session.get("cart", [])
    if pk in cart:
        return True
    else:
        return False


@register.filter(name='each_total_price')
def each_total_price(price, quantity):
    total_price = price * float(quantity)
    return "{:.2f}".format(total_price)