from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, profile, logout, login, settings, orders, reviews, payment, address, support

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^(?P<user>[\w.@+-]+)/settings/', settings, name='profile'),
    url(r'^(?P<user>[\w.@+-]+)/orders/', orders, name='profile'),
    url(r'^(?P<user>[\w.@+-]+)/reviews/', reviews, name='profile'),
    url(r'^(?P<user>[\w.@+-]+)/payment/', payment, name='profile'),
    url(r'^(?P<user>[\w.@+-]+)/address/', address, name='profile'),
    url(r'^(?P<user>[\w.@+-]+)/support/', support, name='profile'),
    url(r'^(?P<user>[\w.@+-]+)', profile, name='profile'),
]