<img src ="https://cdn.dribbble.com/users/398490/screenshots/1297496/dribbble_4.gif" width= "800px" height = "300px">

# <img src = "https://cdn.dribbble.com/users/2206859/screenshots/4955676/hotel_dribble1.gif" align = "center" width = "60px" height = "40px"> Introduction
Kazi departmental store is a physical store located in cumilla. The customer base is mostly people living at jhautola.

**We were given a task by one of our supervisors that we have to build a product for an enterprise.**

**This project was a part of one of our sessional courses.We decided to build a website where customers can order a product and the admin can see the products ordered by customers.**


## <img src = "https://res.cloudinary.com/practicaldev/image/fetch/s--p6EqClgv--/c_imagga_scale,f_auto,fl_progressive,h_900,q_auto,w_1600/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/fizbec05u7a429pqqllr.png" align = "center" width = "60px"> Why Django?
We decided to complete this project in django because:
  - Takes less time to build prototype.
  - Comes with SQLite as database.
  - Django comes with a default admin panel(which we later customized) which made our job easier.

# <a href = "https://youtu.be/x27qBDEJ1HY"> <img align = "center" src = "https://cdn.dribbble.com/users/1369921/screenshots/3699553/media/632fe87d30ef9413a3512dd317727b8b.gif" width = "60px" height = "40px"></a> Demo
 <p> You will find video demo &nbsp;<b>Here</b>➡️ <b><a href = "https://youtu.be/x27qBDEJ1HY">Youtube</a></b></p>



# <img src = "https://cdn.dribbble.com/users/1138721/screenshots/10809828/media/478d32b2e65c8c3194b7f2154e179231.gif" align = "center" width = "60px" height = "40px"> Features 
- [User Authentication]()
- [Category wise product selection]()
- [Adding Items to cart]()
  - Quantity Increment & Decrement
  - Checkout only when user is logged in &     have items in cart
- [Subscription Model]()
- [Customized Admin Panel]()
- [Order Tracking]() (By Admin)

<br> 

# <img src = "https://cdn.dribbble.com/users/2070959/screenshots/4169320/pc_1.gif" align = "center" width = "60px" height = "40px"> Some necessary instructions 
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
