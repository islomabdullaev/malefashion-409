from django.shortcuts import redirect, render
from blogs.models import PostModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# models
from pages.models import BannerModel, ContactModel
from products.models import BrandModel, CategoryModel, ColorModel, ProductModel, SizeModel, TagModel
from django.db.models import Max, Min
# Create your views here.

def homePageView(request):
    banners = BannerModel.objects.filter(is_active=True)
    products = ProductModel.objects.all()
    posts = PostModel.objects.all()
    context = {
        "banners": banners,
        "products": products,
        "posts": posts
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
    price_range = request.GET.get('my_range')
    paginator = Paginator(products, 3)
    from_price = 0
    to_price = 0
    if price_range:
        price_range = price_range.split(";")
        from_price, to_price = price_range[0], price_range[1]
        products = products.filter(price__gte=from_price, price__lte=to_price)
        paginator = Paginator(products, len(products))
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
    
    page_number = int(request.GET.get('page', 1))

    try:
        page_obj = paginator.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = paginator.page(paginator.num_pages)


    context = {
        "products": products,
        "categories": CategoryModel.objects.all(),
        "brands": BrandModel.objects.all(),
        "sizes": SizeModel.objects.all(),
        "colors": ColorModel.objects.all(),
        "tags": TagModel.objects.all(),
        "min_price": ProductModel.objects.aggregate(min_price=Min("price"))['min_price'],
        "max_price": ProductModel.objects.aggregate(max_price=Max("price"))['max_price'],
        "page_obj": page_obj
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
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        text = request.POST.get("text")
        ContactModel.objects.create(name=name, email=email, text=text)
        return redirect('pages:contact')
    return render(request, template_name="contact.html")

def cartListView(request):
    cart = request.session.get("cart", [])
    products = ProductModel.objects.filter(pk__in=cart)
    context = {
        "products": products
    }
    return render(request, template_name="shopping-cart.html", context=context)