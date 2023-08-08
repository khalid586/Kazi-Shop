from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password , check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.views import View
from .models.subscriber import Subscriber
from .models.orders import Order
# Create your views here.

def home(request):
    return render(request,'home.html')

class Index(View):
    def post(self,request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        # print(product)

        cart = request.session.get('cart')
        
        if cart: # if cart exists I have to do something else I'll do something else
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:   
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1 
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart
        print(cart)
        
        return redirect('homepage')

    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session.cart = {}
            
        products = Product.objects.all()
        categories = Category.objects.all()

        categoryID = request.GET.get('category')

        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()
        data = {}
        data['products'] = products
        data['categories'] = categories

        # print('you are: ', request.session.get('email'))
        # print('your id is : ' , request.session.get('customer_id'))

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

            return redirect('login')
        else:
            data = {
                'error': errorMessage,
                'values': value
            }
            return render(request,'signup.html',data)
        
class Subscribe(View):
    def get(self,request):
        return render(request,'subscribe.html')
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        address = postData.get('address')
        subs = {
                'firstName' : first_name,
                'lastName'  : last_name,
                'address' : address,
                'phone' : phone,
                'email': email
            }

        errorMessage = None
        value = {
            'first_name' : first_name,
            'last_name' : last_name,
            'phone' : phone,
            'email': email,
            'address': address,
        }
        subscriber = Subscriber(first_name = first_name , last_name = last_name , phone = phone , address = address ,email = email)

        if len(first_name) < 4:
            errorMessage = 'First Name should be atleast 4 characters'
        elif len(last_name) < 4:
            errorMessage = 'Last Name should be atleast 4 characters'
        elif(len(phone) < 11):
            errorMessage = 'Phone number should be atleast 11 characters'
        elif not email:
            errorMessage = 'Email field cannot be blank'

        elif subscriber.isExists():
            errorMessage = 'You have already subscribed with this email'

        if not errorMessage: 
            subscriber.register()
            return render(request,'successful_subscribe.html',subs)
        else:
            data = {
                'error': errorMessage,
                'values': value
            }
            return render(request,'subscribe.html',data)


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
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                return redirect('homepage')
            else:
                error_message = 'Email or Password invalid'
        else:
            error_message = 'Email or Password invalid'

        return render(request,'login.html' , {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('homepage')


def cart(request):
    cart_session = request.session.get('cart')

    if cart_session is not None :
        ids = list(request.session.get('cart').keys())
        products = Product.get_products_by_id(ids)
        print(products)
        return render(request,'cart.html' , {'products':products})    
    else:
         return render(request,'EmptyCart.html')    
        # return HttpResponse("<h1>Your Cart</h1> <br><b>Your Cart is empty</b>")  

    
class Order(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        customer = request.session.get('customer')

        print(products)

        for product in products:
            order = Order(customer = customer ,
                          product = product,
                          price = product.price,
                          address = address,
                          phone = phone,
                          quantity = cart.get(str(product.id))
                          )
            # order.save()
        
        request.session['cart'] = {}
        return render(request,'orders.html')



