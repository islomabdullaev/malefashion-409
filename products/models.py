from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# validators
from products.validators import rating_value_validate

class CategoryModel(models.Model):
    title = models.CharField(max_length=24)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class BrandModel(models.Model):
    title = models.CharField(max_length=24)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"


class SizeModel(models.Model):
    title = models.CharField(max_length=24)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Size"
        verbose_name_plural = "Sizes"


class ColorModel(models.Model):
    name = models.CharField(max_length=24)
    code = models.CharField(max_length=8)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Color"
        verbose_name_plural = "Colors"


class TagModel(models.Model):
    title = models.CharField(max_length=24)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class ProductModel(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    price = models.FloatField(default=0.0)
    image = models.ImageField(upload_to="products")
    discount = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=1, validators=[rating_value_validate])
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    sizes = models.ManyToManyField(SizeModel)
    colors = models.ManyToManyField(ColorModel)
    tags = models.ManyToManyField(TagModel)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    
    def is_new(self):
        current_time = timezone.now()
        diff = (current_time - self.created_at).days
        if diff <= 3:
            return True
        else:
            return False
    
    def get_real_price(self):
        total = self.price - ((self.price / 100) * self.discount)
        return total
    
    @staticmethod
    def get_from_cart(cart):
        return ProductModel.objects.filter(pk__in=cart)

    
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductImage(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/nested_images")

    def __str__(self) -> str:
        return self.product.name
    
    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"


class WishlistModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlists"
        unique_together = ['user', 'product']

    def __str__(self) -> str:
        return f"{self.user.username} | {self.product.name}"