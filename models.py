from django.db import models
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your models here.
class customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.customer_name+" "+self.contact_number+" "+self.address+" "+self.email
    

class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ManyToManyField(customer)
    
    def __str__(self):
        return self.product_name+" "+str(self.price)+" "+str(self.customer)