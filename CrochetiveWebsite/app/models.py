"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Category(models.Model):
    APPAREL = "Apparel"
    TOYS = "Toys"
    PETS = "Pets"

    CATEGORY_CHOICES = [
        (APPAREL, "Apparel"),
        (TOYS, "Toys"),
        (PETS, "Pets"),
        ]

    name = models.CharField(max_length=10, choices=CATEGORY_CHOICES)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products", default=1)

class FeaturedItem(models.Model):
    image = models.ImageField(upload_to='featured_items/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)