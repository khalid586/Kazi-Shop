An online departmental store which makes customer's life easy.

### You will find some necessary instructions below
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

1. Create Project
```
django-admin startproject store
```
1. go to the project folder
```
cd store
```
1. Run server
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
<summary>Customized Admin Panel</summary>

We have to install jazzmin using terminal

Run the following commands in the terminal 
```
pip install -U django-jazzmin
```
Then go to settings and type `'jazzmin',` in the INSTALLED APPS

</details>
