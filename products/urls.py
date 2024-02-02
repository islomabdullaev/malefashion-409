from django.urls import path

from products.views import wishlistPageView, add_to_wishlist

app_name = "products"

urlpatterns = [
    path("wishlist/", wishlistPageView, name="wishlist"),
    path("<int:product_pk>/add_to_wishlist/", add_to_wishlist, name="add_to_wishlist")
]