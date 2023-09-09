# Introduction
Kazi departmental store is a physical store located in cumilla. The customer base is mostly people living at jhautola.

### Reason for choosing django
We were given a task by one of our supervisors that we have to build a product for an enterprise.This project was a part of one of our sessional courses.We decided to build this website where customers can order a product and the admin can see the products ordered by customers.We decided to complete this project in django because django comes with a default admin panel(which we later customized) which made our job easier.

# Demo
 <p><a href = "https://youtu.be/x27qBDEJ1HY"> <img align = "center" src = "https://cdn.dribbble.com/users/1369921/screenshots/3699553/media/632fe87d30ef9413a3512dd317727b8b.gif" width = "70px"></a> You will find video demo &nbsp;<b>Here</b>➡️ <b><a href = "https://youtu.be/x27qBDEJ1HY">Youtube</a></b></p>

# Features 
- User Authentication
- Category wise product selection
- Adding Items to cart
  - Quantity Increment & Decrement
  - Checkout only when user is logged in &     have items in cart
- Subscription Model
- Customized Admin Panel
- Order Tracking (By Admin)

<br> 

# Some necessary instructions 
<details> 
<summary>How to create a django project</summary>

To install django and create a django project first open a folder and then move into that folder and open terminal do the following steps(in the terminal).

1. Install django
```
pip install django
```
2. Upgrade django (If needed)
```
pip install django --upgrade
```
3. Create Project
```
django-admin startproject store
```
4. go to the project folder
```
cd store
```
5. Run server
```
python manage.py runserver
```

You can use any preferred name instead of `store` .

</details>

<details> 
<summary>How to create a django app</summary>

To install app after creating a project run the following command in the terminal.

```
python manage.py startapp shopStore
```

You can use any preferred name instead of `shopStore` .

</details>

<details> 
<summary>What to do after making migrations(Ex.models.py or admin.py)</summary>

Run the following commands in the terminal 

```
python manage.py makemigrations
python manage.py migrate
```
</details>

<details> 
<summary>How to create a Customized Admin Panel</summary>

We have to install jazzmin using terminal

To install ,
Run the following commands in the terminal 
```
pip install -U django-jazzmin
```
Then go to `settings.py` and type `'jazzmin',` in the INSTALLED APPS

</details>
