from django.db import models
from catergories.models import Catergory, SubCatergory

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    catergory = models.ForeignKey(Catergory, null=True, default=0, blank=True, on_delete=models.CASCADE)
    sub_catergory = models.ForeignKey(SubCatergory, null=True, default=0, blank=True, on_delete=models.CASCADE)
    
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name