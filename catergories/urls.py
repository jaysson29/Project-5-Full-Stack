from django.conf.urls import url, include
from .views import all_cats, show_products, show_product, show_subcats
from products.views import all_products
from catergories.models import Catergory, SubCatergory

urlpatterns = [
    url(r'^&', all_cats, name='Catergories'),
    url(r'^(?P<catergory_title>[\w.@+-]+)/(?P<subCatergory>[\w.@+-]+)/(?P<product>[\w.@+-]+)', show_product, name='Show_product'),
    url(r'^(?P<catergory_title>[\w.@+-]+)/(?P<subCatergory>[\w.@+-]+)', show_products, name='Show_products'),
    url(r'^(?P<catergory_title>[\w.@+-]+)/', show_subcats, name='Show_subcats'),
]