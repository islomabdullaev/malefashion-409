# Generated by Django 5.0.1 on 2024-01-31 12:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productmodel_options_alter_productmodel_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wishlistmodel',
            options={'verbose_name': 'Wishlist', 'verbose_name_plural': 'Wishlists'},
        ),
        migrations.AlterUniqueTogether(
            name='wishlistmodel',
            unique_together={('user', 'product')},
        ),
    ]
