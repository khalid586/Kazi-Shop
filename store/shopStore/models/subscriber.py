from django.db import models

class Subscriber(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 15)
    email = models.EmailField()
    password = models.CharField(max_length = 500)
    
    def __str__(self):
        return self.first_name
    
    def register(self):    
        self.save()

    @staticmethod
    def get_subscriber(email):
        try:
            return Subscriber.objects.get(email = email)
        except:
            return False

    def isExists(self):
        return Subscriber.objects.filter(email = self.email)