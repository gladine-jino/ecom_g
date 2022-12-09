from django.db import models

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.db.models import signals
from django.dispatch import receiver


class User(AbstractUser):
    profile_img = models.ImageField(default='media_root/reg.jpg')    
    age=  models.IntegerField(null=True)
    address=models.TextField(null=True)
    phone_number=models.IntegerField(null=True)
    adhar_number=models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group=models.ForeignKey(Group,related_name="group",on_delete=models.CASCADE,null=True,blank=True)
    

#     class Meta:  
#         permissions=(
#             ('is_owner','is_owner'),
#         ('is_inventory_staff','is_inventory_staff'),
#         ('is_service_staff','is_service_staff'), 
#         ) 

new_group, created = Group.objects.get_or_create(name='owner')

new_group, created = Group.objects.get_or_create(name='inventory_staff')

new_group, created = Group.objects.get_or_create(name='service_staff')

# ----Simple store=------


class Role(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    role=models.CharField(max_length=30,null=True,blank=True)

    def __str__(self):
        return f'{self.user.username}' 

class Customer(models.Model):
    name=models.CharField(max_length=30)
    phone_number=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'{self.name}' 

class Product(models.Model):
    product=models.CharField(max_length=30)
        
    stock_quantity=models.IntegerField()
    unit_price=models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    


    def __str__(self):
        return f'{self.product}'  
    

class ItemsSaled(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)   
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)  
    sell_quantity=models.IntegerField()    
    total_amount=models.IntegerField()
    amount_paid=models.IntegerField(null=True)
    credit_balance=models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Ecommm store-----
class Address(models.Model):

    appartment_address=models.TextField()
    street_address=models.TextField()
    district=models.CharField(max_length=200)
    state=models.CharField(max_length=200)   
    city=models.CharField(max_length=200)
    country=models.CharField(max_length=200)    
    zipcode=models.CharField(max_length=200)

     

class Profile(models.Model):
    customer_name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)    
    date_joined=models.DateTimeField(auto_now_add=True)

    def _str_(self):
         return f'{self.customer_name}' 

# @receiver(signals.post_save,sender=Profile)
# def create_profile(sender,instance,created,**kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(signals.post_save,sender=Profile)
# def save_profile(sender,instance,created,**kwargs):
#     instance.profile.save()




    
