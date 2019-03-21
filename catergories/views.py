from django.shortcuts import render
from project_5.settings import MEDIA_URL
from .models import Men, Women, Unisex, Extra
# Create your views here.

def all_cats(request):
    Mens = Men.objects.all()
    Womens = Women.objects.all()
    Unisexs = Unisex.objects.all()
    Extras = Extra.objects.all()
    return render(request, "cats.html",{"Mens": Mens,"Womens": Womens,"Unisexs": Unisexs,"Extras": Extras, "MEDIA_URL": MEDIA_URL})
