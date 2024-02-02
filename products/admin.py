from django.contrib import admin

# models
from products.models import (
    CategoryModel, BrandModel, SizeModel,
    ColorModel, TagModel, ProductModel, WishlistModel)

# Register your models here.
admin.site.register(ProductModel)
admin.site.register(CategoryModel)
admin.site.register(BrandModel)
admin.site.register(SizeModel)
admin.site.register(ColorModel)
admin.site.register(TagModel)
admin.site.register(WishlistModel)