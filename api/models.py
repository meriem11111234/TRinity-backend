from django.db import models

class User(models.Model):
    is_admin = models.BooleanField(default=False) 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    billing_address = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    brand = models.CharField(max_length=255, null=True, blank=True)
    picture = models.URLField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    nutritional_info = models.TextField(null=True, blank=True)
    available_quantity = models.IntegerField(default=0)


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
