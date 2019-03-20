from django.shortcuts import render
from project_5.settings import MEDIA_URL
from .models import Catergorie, Men, Women, Extra
# Create your views here.

def all_cats(request):
    Cats = Catergorie.objects.all()
    Mens = Men.objects.all()
    Womens = Women.objects.all()
    Extras = Extra.objects.all()
    return render(request, "cats.html",{"Cats": Cats,"Mens": Mens,"Womens": Womens,"Extras": Extras, "MEDIA_URL": MEDIA_URL})
