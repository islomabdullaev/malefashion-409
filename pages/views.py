from django.shortcuts import render
from blogs.models import PostModel

# models
from pages.models import BannerModel
from products.models import BrandModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel

# Create your views here.

def homePageView(request):
    banners = BannerModel.objects.filter(is_active=True)
    context = {
        "banners": banners
    }
    return render(request, template_name="home.html", context=context)


def shopPageView(request):

    context = {
        "products": ProductModel.objects.all(),
        "categories": CategoryModel.objects.all(),
        "brands": BrandModel.objects.all(),
        "sizes": SizeModel.objects.all(),
        "colors": ColorModel.objects.all(),
        "tags": TagModel.objects.all()
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