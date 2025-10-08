import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    CATEGORY_CHOICES = [
    ('jersey', 'Jersey'),
    ('shoes', 'Sepatu'),
    ('ball', 'Bola'),
    ('merch', 'Merchandise'),
    ]

    BRAND_CHOICES = [
        ('nike', 'Nike'),
        ('adidas', 'Adidas'),
        ('puma', 'Puma'),
        ('under_armour', 'Under Armour'),
        ('reebok', 'Reebok'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices= CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    # tambahan
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, default='adidas')
    # hubungin model dengan user
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # tambahkan ini

    def __str__(self):
        return self.name