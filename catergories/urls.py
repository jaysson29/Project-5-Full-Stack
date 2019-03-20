from django.conf.urls import url, include
from .views import all_cats

urlpatterns = [
    url(r'^$', all_cats, name='Catergories'),
]