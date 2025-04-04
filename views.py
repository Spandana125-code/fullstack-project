from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from shopitem_app.models import product

# Create your views here.
def basic(request):
    return render(request, 'basic.html')

def contactus(request):
    return render(request, 'contactus.html')

def aboutus(request):
    return render(request, 'aboutus.html')
def home(request):
    return render(request, 'home.html')

def products_list(request):
    p=product.objects.all()
    return render(request, 'products_list.html', {'products_list':p})

def customerregister(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'customerregister.html', {'form': form})

def customerlogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'customerlogin.html', {'form': form})

def home(request):
    return render(request, 'home.html')