from django.urls import path

from products.views import wishlistPageView, add_to_wishlist, shopDetailView, add_to_cart

app_name = "products"
urlpatterns = [
    path('<int:pk>/details', shopDetailView, name="details"),
    path("wishlist/", wishlistPageView, name="wishlist"),
    path("<int:product_pk>/add_to_wishlist/", add_to_wishlist, name="add_to_wishlist"),
    path("<int:pk>/add_to_cart/", add_to_cart, name="add_to_cart")
]