from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    email = models.EmailField(unique = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self) -> str:
        return self.username


class Category(models.Model):
    CATEGORY_CHOICES = (
        ('Clothing&Fashion', 'Clothing & Fashion'),
        ('Electronics', 'Electronics'),
        ('Home&Garden', 'Home & Garden'),
        ('Health&Beauty', 'Health & Beauty'),
        ('Sports&Outdoors', 'Sports & Outdoors'),
        ('Food&Beverage', 'Food & Beverage'),
        ('Toys&Games', 'Toys & Games'),
        ('Automotive', 'Automotive'),
    )

    category = models.CharField(max_length = 100, choices = CATEGORY_CHOICES, unique = True)
    def __str__(self) -> str:
        return self.category


class Shop(models.Model):
    user = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200, unique = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    address = models.TextField()
    state = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    pincode = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    image = models.ImageField(null = True)
    name = models.CharField(max_length = 100)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.name