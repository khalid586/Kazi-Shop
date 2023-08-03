from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 15)
    email = models.EmailField()
    password = models.CharField(max_length = 500)
    
    def __str__(self):
        return self.first_name
    
    def register(self):    
        self.save()

    def isExists(self):
        return Customer.objects.filter(email = self.email)