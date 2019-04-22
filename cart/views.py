from django.shortcuts import render, redirect, reverse
from project_5.settings import MEDIA_URL
from catergories.models import Catergory
from django.http import HttpResponseRedirect




# Create your views here.
def view_cart(request):
    """
    A view that renders the cart contents page
    """
    Catergories = Catergory.objects.all()
    return render(request, "cart.html", {"MEDIA_URL": MEDIA_URL, "Catergories": Catergories})
    
def add_to_cart(request, id):
    """
    Add a quantity of the specified product to the cart
    """
    quantity=int(request.POST.get('quantity'))
    
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return redirect(reverse('index'))
    
def add_to_cart_quick(request, id):
    """
    Add a quantity of the specified product to the cart
    """
    quantity=1
    prev = request.POST.get('prev')
    
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return HttpResponseRedirect(prev)
    
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
def remove_cart_item(request, id):
    """
    remove a quantity of the specified product to the cart
    """
    cart = request.session.get('cart', {})
    
    cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
    
def remove_cart_item_quick(request, id):
    """
    Add a quantity of the specified product to the cart
    """
    quantity=0
    prev = request.POST.get('prev')
    
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    
    request.session['cart'] = cart
    return HttpResponseRedirect(prev)