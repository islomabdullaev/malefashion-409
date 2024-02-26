from django.contrib import admin

from pages.models import BannerModel, ContactModel

# Register your models here.
admin.site.register(BannerModel)
admin.site.register(ContactModel)