from django.db import models

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

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices= CATEGORY_CHOICES, default='jersey')
    is_featured = models.BooleanField(default=False)
    # tambahan
    stock = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES, default='adidas')

    def __str__(self):
        return self.name
    
