from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from catergories.models import Catergory
from .models import Profiles


# Create your views here.
def index(request):
    """A view that displays the index page"""
    Catergories = Catergory.objects.all()
    return render(request, "index.html", {"Catergories": Catergories})

def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))

def login(request):
    """A view that manages the login form"""
    Catergories = Catergory.objects.all()
    if request.method == 'POST':
        user_form = UserLoginForm(request.POST)
        if user_form.is_valid():
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])

            if user:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")

                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                else:
                    return redirect(reverse('index'))
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    else:
        user_form = UserLoginForm()

    args = {'user_form': user_form, 'next': request.GET.get('next', ''), "Catergories": Catergories}
    return render(request, 'login.html', args)

@login_required(login_url='/account/login/')
def profile(request, user):
    """A view that displays the profile page of a logged in user"""
    Catergories = Catergory.objects.all()
    return render(request, 'profile.html', {"Catergories": Catergories})

@login_required(login_url='/account/login/')
def settings(request, user):
    Catergories = Catergory.objects.all()
    Profile = Profiles.objects.all()
    return render(request, 'settings.html', {"Catergories": Catergories, "Profile": Profile})
    
@login_required(login_url='/account/login/')
def orders(request, user):
    Catergories = Catergory.objects.all()
    return render(request, 'orders.html', {"Catergories": Catergories})
    
@login_required(login_url='/account/login/')
def reviews(request, user):
    Catergories = Catergory.objects.all()
    return render(request, 'reviews.html', {"Catergories": Catergories})
    
@login_required(login_url='/account/login/')
def payment(request, user):
    Catergories = Catergory.objects.all()
    return render(request, 'payments.html', {"Catergories": Catergories})

@login_required(login_url='/account/login/')
def address(request, user):
    Catergories = Catergory.objects.all()
    return render(request, 'address.html', {"Catergories": Catergories})

@login_required(login_url='/account/login/')
def support(request, user):
    Catergories = Catergory.objects.all()
    return render(request, 'support.html', {"Catergories": Catergories})

def register(request):
    """A view that manages the registration form"""
    Catergories = Catergory.objects.all()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))

            if user:
                auth.login(request, user)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form, "Catergories": Catergories}
    return render(request, 'register.html', args)
