from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product

# Create your views here.
def index(request):
    prods = Product.objects.all()
    return render(request , 'index.html', {'products':prods}) 