from django.db import IntegrityError
from django.shortcuts import redirect, render

from products.models import ProductModel, WishlistModel

# Create your views here.
def wishlistPageView(request):
    wishlists = WishlistModel.objects.filter(user=request.user)
    context = {
        "wishlists": wishlists
    }
    return render(request, template_name="wishlist.html", context=context)


def add_to_wishlist(request, product_pk):
    product = ProductModel.objects.get(id=product_pk)
    current_path_url = request.META.get("HTTP_REFERER")
    try:
        WishlistModel.objects.create(user=request.user, product=product)
    except IntegrityError:
        WishlistModel.objects.get(user=request.user, product=product).delete()
    
    return redirect(current_path_url)
