from django import template
from django.db.models import Sum

from products.models import ProductModel, WishlistModel

register = template.Library()


@register.filter(name="in_wishlist")
def in_wishlist(user, product):
    return WishlistModel.objects.filter(user=user, product=product).exists()

@register.simple_tag
def get_cart_info(request, coupon=None):
    cart = request.session.get("cart", [])
    if not cart:
        return 0, 0.0
    quantity = len(cart)
    total_price = 0
    products = ProductModel.get_from_cart(cart)
    for product in products:
        total_price += product.get_real_price()
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