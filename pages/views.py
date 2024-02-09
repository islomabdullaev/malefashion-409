from django.shortcuts import render
from blogs.models import PostModel

# models
from pages.models import BannerModel
from products.models import ProductModel

# Create your views here.

def homePageView(request):
    banners = BannerModel.objects.filter(is_active=True)
    context = {
        "banners": banners
    }
    return render(request, template_name="home.html", context=context)


def shopPageView(request):
    products = ProductModel.objects.all()
    context = {
        "products": products
    }
    return render(request, template_name="shop.html", context=context)


def aboutPageView(request):
    return render(request, template_name="about.html")


def blogPageView(request):
    posts = PostModel.objects.all()
    tag = request.GET.get('tag')
    if tag:
        posts = PostModel.objects.filter(tags__title=tag)
    context = {
        "posts": posts
    }
    return render(request, template_name="blog.html", context=context)


def contactPageView(request):
    return render(request, template_name="contact.html")