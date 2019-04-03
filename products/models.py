from django.db import models
from catergories.models import Men, Women, Unisex, Extra

# Create your models here.

class Product(models.Model):
    catergory_choices = (
        ('Men', 'Mens'),
        ('Women', 'Womens'), 
        ('Unisex', 'Unisexs'), 
        ('Extra', 'Extras'), 
    )
    
    
    name = models.CharField(max_length=254, default='')
    catergory = models.CharField(max_length=8,choices=catergory_choices,default=0, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name