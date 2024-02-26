from django.urls import path

from products.views import wishlistPageView, add_to_wishlist, shopDetailView

app_name = "products"
urlpatterns = [
    path('<int:pk>/details', shopDetailView, name="details"),
    path("wishlist/", wishlistPageView, name="wishlist"),
    path("<int:product_pk>/add_to_wishlist/", add_to_wishlist, name="add_to_wishlist")
]