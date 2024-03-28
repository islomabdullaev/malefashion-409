from django.db import IntegrityError
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from products.models import ProductModel, WishlistModel

# Create your views here.
def wishlistPageView(request):
    wishlists = WishlistModel.objects.filter(user=request.user)
    context = {
        "wishlists": wishlists
    }
    return render(request, template_name="wishlist.html", context=context)


def shopDetailView(request, pk):
    product = ProductModel.objects.get(pk=pk)
    related_products = ProductModel.objects.filter(category__title=product.category.title).exclude(pk=product.pk)
    context = {
        "product": product,
        "related_products": related_products
    }
    return render(request, template_name="shop-details.html", context=context)


@login_required
def add_to_wishlist(request, product_pk):
    product = ProductModel.objects.get(id=product_pk)
    current_path_url = request.META.get("HTTP_REFERER")
    try:
        WishlistModel.objects.create(user=request.user, product=product)
    except IntegrityError:
        WishlistModel.objects.get(user=request.user, product=product).delete()
    
    return redirect(current_path_url)


@login_required
def add_to_cart(request, pk, quantity):
    current_path_url = request.META.get("HTTP_REFERER")
    cart_data = request.session.get("data", [])
    data = {
        "pk": pk,
        "quantity": quantity
    }
    if data in cart_data:
        cart_data.remove(data)
    else:
        cart_data.append(data)
    request.session['data'] = cart_data

    return redirect(current_path_url)


@login_required
def remove_from_cart(request, pk):
    current_path_url = request.META.get("HTTP_REFERER")
    cart_data = request.session.get("data", [])
    print(cart_data)
    for data in cart_data:
        if int(data['pk']) == pk:
            to_remove = {"pk": str(pk), "quantity": data['quantity']}
            print(to_remove)
            cart_data.remove(to_remove)
    request.session['data'] = cart_data

    return redirect(current_path_url)


@login_required
def update_cart(request):
    current_path_url = request.META.get("HTTP_REFERER")
    cart_data = request.session.get("data", [])
    key1_values = request.POST.getlist('pk')
    key2_values = request.POST.getlist('quantity')
    new_data = []
    # bu yerda biz pk bilan quantity ni bir biriga boglayapmiz olyatganda
    # print(request.POST) qilib koringlar korish uchun qanday turda kelyatganini malumotni
    for pk, quantity in zip(key1_values, key2_values):
        data = {
            "pk": pk,
            "quantity": quantity
        }
        new_data.append(data)
    request.session['data'] = new_data
    return redirect(current_path_url)