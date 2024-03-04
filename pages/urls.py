from django.urls import path
from pages.views import cartListView, homePageView, shopPageView, aboutPageView, blogPageView, contactPageView

app_name = "pages"

urlpatterns = [
    path('', homePageView, name="home"),
    path('shop/', shopPageView, name="shop"),
    path('about/', aboutPageView, name="about"),
    path('blog/', blogPageView, name="blog"),
    path('contact/', contactPageView, name="contact"),
    path('cart/', cartListView, name='cart')
]