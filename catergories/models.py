from django.db import models

# Create your models here.
class Men(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.title
        
class Women(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.title
        
class Extra(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.title
    
class Catergorie(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.title