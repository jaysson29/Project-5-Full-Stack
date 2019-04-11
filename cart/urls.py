from django.conf.urls import url
from.views import view_cart, add_to_cart, adjust_cart, add_to_cart_quick

urlpatterns = [
    url(r'^$', view_cart, name='view_cart'),
    url(r'^add/(?P<id>\d+)/quick', add_to_cart_quick, name="add_to_cart_quick"),
    url(r'^add/(?P<id>\d+)', add_to_cart, name="add_to_cart"),
    url(r'^adjust/(?P<id>\d+)', adjust_cart, name="adjust_cart"),
    ]