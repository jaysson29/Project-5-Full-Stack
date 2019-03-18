from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
class OrderLineAdminIline(admin.TabularInline):
    model = OrderLineItem
    
class OrderAdmin(admin.ModelAdmin):
    inlines= (OrderLineAdminIline, )
    
admin.site.register(Order, OrderAdmin)