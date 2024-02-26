from django.db import models

# Create your models here.

class BannerModel(models.Model):
    title = models.CharField(max_length=64)
    collection = models.CharField(max_length=24)
    description = models.TextField()
    image = models.ImageField(upload_to="banners")
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.collection}: {self.title}"
    
    class Meta:
        verbose_name = "Banner"
        verbose_name_plural = "Banners"


class ContactModel(models.Model):
    name = models.CharField(max_length=36)
    email = models.EmailField(max_length=64)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}: {self.text}"
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"