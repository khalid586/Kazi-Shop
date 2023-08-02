from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    
    return HttpResponse(request.POST.get('email'))

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request , 'index.html', data) 