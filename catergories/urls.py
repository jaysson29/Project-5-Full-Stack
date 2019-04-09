from django.conf.urls import url, include
from .views import all_cats, show_products
from products.views import all_products
from catergories.models import Catergory, SubCatergory

urlpatterns = [
    url(r'^&', all_cats, name='Catergories'),
    url(r'^(?P<catergory_title>[\w.@+-]+)/(?P<subCatergory>[\w.@+-]+)/', show_products, name='Show_products')
]