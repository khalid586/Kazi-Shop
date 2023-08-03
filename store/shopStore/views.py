from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.views import View
# Create your views here.

def home(request):
    return render(request,'home.html')

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    data = {}
    data['products'] = products
    data['categories'] = categories

    print('you are: ', request.session.get('email'))
    print('your id is : ' , request.session.get('customer_id'))

    return render(request , 'index.html', data) 

class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')

        errorMessage = None
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email': email


        }
        customer = Customer(first_name = first_name , last_name = last_name , phone = phone , email = email , password = password)

        if len(first_name) < 4:
            errorMessage = 'First Name should be atleast 4 characters'
        elif len(last_name) < 4:
            errorMessage = 'Last Name should be atleast 4 characters'
        elif(len(phone) < 11):
            errorMessage = 'Phone number should be atleast 11 characters'
        elif not email:
            errorMessage = 'Email field cannot be blank'
        elif len(password) < 4:
            errorMessage = 'Password should be atleast 4 characters'

        elif customer.isExists():
            errorMessage = 'Email already registered'

        if not errorMessage: 
            customer.password = make_password(customer.password)
            customer.register()

            return redirect('homepage')
        else:
            data = {
                'error': errorMessage,
                'values': value
            }
            return render(request,'signup.html',data)


class Login(View):

    def get(self,request):
        return render(request,'login.html')
    
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer(email)
        error_message = None

        if customer:
            flag = check_password(password , customer.password)

            if flag:
                request.session['customer_id'] = customer.id
                request.session['email'] = customer.email
                return redirect('homepage')
            else:
                error_message = 'Email or Password invalid'
        else:
            error_message = 'Email or Password invalid'

        return render(request,'login.html' , {'error': error_message})
