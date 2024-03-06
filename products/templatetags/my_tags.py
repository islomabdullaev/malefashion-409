from django import template
from django.db.models import Sum

from products.models import ProductModel, WishlistModel

register = template.Library()


@register.filter(name="in_wishlist")
def in_wishlist(user, product):
    return WishlistModel.objects.filter(user=user, product=product).exists()

@register.simple_tag
def get_cart_info(request):
    cart = request.session.get("cart", [])
    if not cart:
        return 0, 0.0
    quantity, total_price = len(cart), ProductModel.get_from_cart(cart).aggregate(Sum("price"))['price__sum']
    return quantity, total_price