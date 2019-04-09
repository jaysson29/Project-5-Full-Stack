from django.db import models
from django.contrib import admin

# Create your models here.

class Catergory(models.Model):
    title = models.CharField(max_length=254, default='')
    
    class Meta:
        verbose_name_plural = 'Catergories'
    
    def __str__(self):
        return self.title
        
class SubCatergory(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='cats/images/')
    catergory = models.ForeignKey(Catergory, null=True, default=0, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name_plural = 'SubCatergories'
    
    def __str__(self):
        return self.title
        
        
class SubCatergoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'catergory',)
    list_per_page = 25
        

