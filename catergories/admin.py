from django.contrib import admin
from .models import Catergory, SubCatergory, SubCatergoryAdmin

# Register your models here.
admin.site.register(Catergory)
admin.site.register(SubCatergory, SubCatergoryAdmin)
