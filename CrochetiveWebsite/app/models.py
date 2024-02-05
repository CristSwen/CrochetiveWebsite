"""
Definition of models.
"""

from django.db import models

# Create your models here.

CATEGORY_CHOICES = {
     ('APPAREL', "Apparel"),
     ('TOYS', "Toys"),
     ('PETS', "Pets"),
     }

class ApparelProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

class ToysProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

class PetsProduct(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

class FeaturedItem(models.Model):
    image = models.ImageField(upload_to='featured_items/')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)