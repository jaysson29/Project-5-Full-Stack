from django.shortcuts import render, get_object_or_404, redirect
from project_5.settings import MEDIA_URL
from .models import Catergory, SubCatergory
from products.models import Product
from project_5.settings import MEDIA_URL
import http.client
import urllib.request
import urllib.error
from django.core.paginator import Paginator
# Create your views here.

def all_cats(request):
    Catergories = Catergory.objects.all()
    SubCatergories = SubCatergory.objects.all()
    return render(request, "cats.html",{"Catergories": Catergories,"SubCatergories": SubCatergories, "MEDIA_URL": MEDIA_URL})

def show_products(request, catergory_title, subCatergory):
    catergory_select = Catergory.objects.get(title=catergory_title)
    sub_catergory_select = SubCatergory.objects.get(title=subCatergory, catergory = catergory_select)
    product_select = Product.objects.filter(catergory = catergory_select, sub_catergory = sub_catergory_select).order_by('name')
    return render(request, "products.html", {"product_select": product_select, "MEDIA_URL": MEDIA_URL})