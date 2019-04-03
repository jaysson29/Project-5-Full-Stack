from django.conf.urls import url, include
from .views import all_cats
from products.views import all_products

urlpatterns = [
    url(r'^$', all_cats, name='Catergories'),
    url(r'^mens/', all_products, name='Mens'),
]