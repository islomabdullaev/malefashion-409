from django.urls import path

from products.views import wishlistPageView, add_to_wishlist, shopDetailView, add_to_cart, update_cart, remove_from_cart

app_name = "products"
urlpatterns = [
    path('<int:pk>/details', shopDetailView, name="details"),
    path("wishlist/", wishlistPageView, name="wishlist"),
    path("<int:product_pk>/add_to_wishlist/", add_to_wishlist, name="add_to_wishlist"),
    path("<int:pk>/add_to_cart/<int:quantity>/", add_to_cart, name="add_to_cart"),
    path("update_cart/", update_cart, name="update_cart"),
    path("remove_from_cart/<int:pk>/", remove_from_cart, name="remove_from_cart")
]