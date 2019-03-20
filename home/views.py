from django.shortcuts import render
from catergories.views import all_cats

# Create your views here.
def index(request):
    """A view that will display index page"""
    return render(request, "home.html")