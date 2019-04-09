from django.shortcuts import render
from catergories.views import all_cats
from catergories.models import Catergory

# Create your views here.
def index(request):
    """A view that will display index page"""
    Catergories = Catergory.objects.all()
    return render(request, "home.html", {"Catergories": Catergories})