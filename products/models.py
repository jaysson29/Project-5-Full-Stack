from django.db import models
from catergories.models import Catergory, SubCatergory

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    catergory = models.ForeignKey(Catergory, null=True, default=0, blank=True, on_delete=models.CASCADE)
    sub_catergory = models.ForeignKey(SubCatergory, null=True, default=0, blank=True, on_delete=models.CASCADE)
    description = models.TextField()
    ratings = (
        ("1/10","1/10"),
        ("2/10","2/10"),
        ("3/10","3/10"),
        ("4/10","4/10"),
        ("5/10","5/10"),
        ("6/10","6/10"),
        ("7/10","7/10"),
        ("8/10","8/10"),
        ("9/10","9/10"),
        ("10/10","10/10"),
    )
    rating =  models.CharField(choices = ratings, max_length=5, null=True, default=0, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name