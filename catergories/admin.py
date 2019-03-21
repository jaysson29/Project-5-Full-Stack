from django.contrib import admin
from .models import Men, Women, Unisex, Extra

# Register your models here.
admin.site.register(Men)
admin.site.register(Women)
admin.site.register(Unisex)
admin.site.register(Extra)