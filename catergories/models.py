from django.db import models

# Create your models here.
class Men(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='cats/mens')
    
    class Meta:
        verbose_name = 'A Mens Catergory'
        verbose_name_plural = 'Mens'
    
    def __str__(self):
        return self.title
        
class Women(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='cats/womens')
    
    class Meta:
        verbose_name = 'A Womens Catergory'
        verbose_name_plural = 'Womens'
    
    def __str__(self):
        return self.title

class Unisex(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='cats/unisex')
    
    class Meta:
        verbose_name = 'A Unisexs Catergory'
        verbose_name_plural = 'Unisexs'
    
    def __str__(self):
        return self.title
        
class Extra(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='cats/extra')
    
    class Meta:
        verbose_name = 'A Extras Catergory'
        verbose_name_plural = 'Extras'
    
    def __str__(self):
        return self.title