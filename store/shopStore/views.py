from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category

# Create your views here.

def signup(request):
    return render(request,'signup.html')

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request , 'index.html', data) 