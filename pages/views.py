from django.shortcuts import render
from blogs.models import PostModel

# models
from pages.models import BannerModel
from products.models import BrandModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel
from django.db.models import Max, Min
# Create your views here.

def homePageView(request):
    banners = BannerModel.objects.filter(is_active=True)
    context = {
        "banners": banners
    }
    return render(request, template_name="home.html", context=context)


def shopPageView(request):
    products = ProductModel.objects.all().order_by("price")
    q = request.GET.get('q')
    category = request.GET.get('category')
    sort = request.GET.get('sort')
    brand = request.GET.get('brand')
    size = request.GET.get('size')
    color = request.GET.get('color')
    tag = request.GET.get('tag')

    if q:
        products = products.filter(name__icontains=q)
    elif category:
        products = products.filter(category__title=category)
    elif brand:
        products = products.filter(brand__title=brand)
    elif size:
        products = products.filter(sizes__title=size)
    elif color:
        products = products.filter(colors__name=color)
    elif tag:
        products = products.filter(tags__title=tag)
    elif sort:
        products = products.order_by(sort)


    context = {
        "products": products,
        "categories": CategoryModel.objects.all(),
        "brands": BrandModel.objects.all(),
        "sizes": SizeModel.objects.all(),
        "colors": ColorModel.objects.all(),
        "tags": TagModel.objects.all(),
        "min_price": ProductModel.objects.aggregate(min_price=Min("price"))['min_price'],
        "max_price": ProductModel.objects.aggregate(max_price=Max("price"))['max_price']
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