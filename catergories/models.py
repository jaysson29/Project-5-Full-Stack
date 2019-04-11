from django.db import models
from django.contrib import admin
from multiselectfield import MultiSelectField

# Create your models here.

class Catergory(models.Model):
    title = models.CharField(max_length=254, default='')
    
    class Meta:
        verbose_name_plural = 'Catergories'
    
    def __str__(self):
        return self.title
        
class Size(models.Model):
    title = models.CharField(max_length=254, default='')
    options = (
        ("XXXSmall","XXXSmall"),
        ("XXSmall","XXSmall"),
        ("XSmall","XSmall"),
        ("Small","Small"),
        ("Medium","Medium"),
        ("Large","Large"),
        ("XLarge","XLarge"),
        ("XXLarge","XXLarge"),
        ("XXXLarge","XXXLarge"),
        ("6","6"),
        ("6.5","6.5"),
        ("7","7"),
        ("7.5","7.5"),
        ("8","8"),
        ("8.5","8.5"),
        ("9","9"),
        ("10","10"),
        ("10.5","10.5"),
        ("11","11"),
        ("12","12"),
    )
    option = MultiSelectField(choices = options, null=True, default=0, blank=True,)
     
    def __str__(self):
        return self.title   

class SubCatergory(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='cats/images/')
    catergory = models.ForeignKey(Catergory, null=True, default=0, blank=True, on_delete=models.CASCADE)
    size =  models.ForeignKey(Size, null=True, default=0, blank=True)
    
    class Meta:
        verbose_name_plural = 'SubCatergories'
    
    def __str__(self):
        return self.catergory.title  + " ( " + self.title + " )"
        
        
class SubCatergoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'catergory', 'size')
    list_per_page = 25
        

