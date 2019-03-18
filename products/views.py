from django.shortcuts import render
from project_5.settings import MEDIA_URL
from .models import Product
# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html",{"products": products, "MEDIA_URL": MEDIA_URL})
