from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=254, null=False, blank=False)
    middle_name = models.CharField(max_length=254, null=False, blank=True)
    last_name = models.CharField(max_length=254, null=False, blank=False)
    mobile_number = models.CharField(max_length=254, null=False, blank=True)
    
    # Address
    country = models.CharField(max_length=254, null=False, blank=True)
    postcode = models.CharField(max_length=20, null=False, blank=True)
    town_or_city = models.CharField(max_length=254, null=False, blank=True)
    street_address1 = models.CharField(max_length=254, null=False, blank=True)
    street_address2 = models.CharField(max_length=254, null=False, blank=True)
    
    class Meta:
        ordering = ('-user',)
        verbose_name_plural = 'Profiles'
        
    def __str__(self):
        return "{0}".format(self.user)