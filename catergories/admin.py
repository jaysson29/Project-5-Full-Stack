from django.contrib import admin
from .models import Catergory, SubCatergory, SubCatergoryAdmin, Size

# Register your models here.
admin.site.register(Catergory)
admin.site.register(SubCatergory, SubCatergoryAdmin)
admin.site.register(Size)
