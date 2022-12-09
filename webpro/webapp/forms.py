from dataclasses import fields
from django import forms
from .models import User,Customer,Product,ItemsSaled,Profile,Address
from django.contrib.auth.forms import UserCreationForm



class RegisterForm(UserCreationForm):
   
   class Meta:
        model=User
        fields=['first_name','last_name','username','adhar_number','email','address','password1','password2','age','phone_number','profile_img']
        labels={'email':'Email'}

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields='__all__'




class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'

class SaleForm(forms.ModelForm):   
   class Meta:
        model=ItemsSaled
        fields=['product','sell_quantity','total_amount','amount_paid','credit_balance','customer']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['customer_name','phone']

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields='__all__'

