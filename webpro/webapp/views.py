from django.shortcuts import render,redirect

from .forms import RegisterForm,CustomerForm,ProductForm,SaleForm,ProfileForm,AddressForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as log
from .models import Customer,Product,ItemsSaled
import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required,login_required
from django.contrib.auth.models import Group
from.models import User,Role
from django.http import JsonResponse


# Create your views here.





def navbar(request):
    user=request.user
    return render(request,"webapp/navbar.html",{'user':user})

def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST, request.FILES)
        # image=request.FILES['profile_img']    
      
        if form.is_valid():  
            form.save() 
            # User.objects.create(profile_image=image)      
            messages.success(request, 'Account created successfully') 
            return redirect('login_view')
        else:
            print(form.errors)
            return render(request,'webapp/register.html', {'form':form})             
    else:        
        form=RegisterForm()
        return render(request, 'webapp/register.html',{'form':form}) 


def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request=request,data=request.POST) 
        if form.is_valid():
            username=form.cleaned_data.get('username')            
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)            
            if user:    
                    log(request,user)
                    return redirect('add_product')
                                 
            else:
                messages.error(request,'Not user')    
                return render(request,'webapp/login.html',{'form':form})          
        else:
            print(form.errors)
            return render(request,'webapp/login.html',{'form':form})     
    else:      
        form=AuthenticationForm()
        return render(request,'webapp/login.html',{'form':form})

def user_logout(request):
    logout(request)
    return redirect('login_view')

def employee(request):
    employee=User.objects.exclude(username='admin').order_by('-is_active')
    
    print(employee)
    
    return render(request,"webapp/employee.html",{'employee':employee})

def role(request,id):
    use=User.objects.get(id=id)
    group=Group.objects.all() 
    if request.method=="POST":
       grou=request.POST.get('role')
       Role.objects.create(user_id=id,role=grou)
       rule=User.objects.get(id=id)
       my_group = Group.objects.get(id=grou) 
       my_group.user_set.add(rule)

       rule.group_id=my_group
       rule.save()
       return redirect('employee')


    return render(request,"webapp/role.html",{'group':group,'use':use})

def remove_role(request,id):
    
    us=User.objects.get(id=id) 
    print(us)

    assigned_roles = Role.objects.get(role=us.group_id)
    assigned_roles.delete()
    us.group_id=None
    us.save()

    return redirect('employee')

def relieval_employee(request,id):
    relieval=User.objects.get(id=id)
    relieval.is_active=False
    relieval.save()
    return redirect('employee')

def activating_employee(request,id):
    activating=User.objects.get(id=id)
    activating.is_active=True
    activating.save()
    return redirect('employee')


def add_customer(request):
    y=  Customer.objects.all()
    if request.method=="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            
            return render(request,'webapp/add_customer.html',{'x':form,'y':y})  
        else:
            form = CustomerForm()
            return render(request,'webapp/add_customer.html',{'form':form})         
       
    else:
        form = CustomerForm()
        return render(request,'webapp/add_customer.html',{'form':form,'y':y})


# @login_required
# @permission_required('webapp.add_product')
def add_product(request):
     y=  Product.objects.all()
     if request.method=="POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            
            return render(request,'webapp/add_product.html',{'x':form,'y':y})  
        else:
            form = ProductForm()
            return render(request,'webapp/add_product.html',{'form':form})         
       
     else:
        form = ProductForm()
        return render(request,'webapp/add_product.html',{'form':form,'y':y})

def view_product(request, id):
    product = Product.objects.get(id = id)
    return render(request, 'webapp/product_details.html', {'product': product})

def edit_product(request,id):
    edit_product=Product.objects.get(id=id)
    form=ProductForm(instance=edit_product)
    
    if request.method=="POST":
        form=ProductForm(request.POST,instance=edit_product)
        if form.is_valid():
            edit=form.save()
            edit.save()
            return redirect('add_product')
        else:
            print(form.errors)
            return render(request,"webapp/edit_product.html",{'edit_product':edit_product,'form':form})
    else:
        
        return render(request,"webapp/edit_product.html",{'edit_product':edit_product,'form':form})

def delete_product(request,id):
    x = Product.objects.get(id=id)
    x.delete()
    return redirect('add_product')

def sale(request):
    product=Product.objects.all()

    y=ItemsSaled.objects.all()
    if request.method=="POST":
        form=SaleForm(request.POST)
        if form.is_valid():
            x=form.save()            
            value=x.sell_quantity
            
            
            pro=Product.objects.get(id=x.product.id)
            
            sq=pro.stock_quantity-value
          
            
            if sq > 5:
                pro.stock_quantity=sq

                pro.save() 
                return render(request,"webapp/sale.html",{'x':x,'product':pro,'y':y})
            elif sq < 5 and sq >= 0:
                pro.stock_quantity=sq
                pro.save()           
                messages.success(request,f"ISSUED SUCCESSFULLY {sq} {pro.product} s now in store") 
                return render(request,"webapp/sale.html",{'x':x,'product':pro,'y':y})
            elif sq<0:

                messages.warning(request,"OUT OF STOCK ")
                messages.warning(request,f"Cannot be issued {-sq} needed remaining")

                return render(request,"webapp/sale.html",{'x':x,'product':pro,'y':y})
        else:
                return render(request,"webapp/sale.html",{'x':x,'product':product,'y':y})

       
    else:
            form=SaleForm()
            y=ItemsSaled.objects.all()
            return render(request,"webapp/sale.html",{'form':form})





def search_customer(request):
    search=Customer.objects.all()
    # balance=ItemsSaled.objects.all()

    if request.method=="POST":
        customer_name=request.POST.get("customer_name")
        
        
        customer=Customer.objects.filter(id=customer_name)
       
        return render(request,"webapp/search_customer.html",{'search':customer})

    return render(request,"webapp/search_customer.html",{'search':search})

def saled_records(request):
    saled_details=ItemsSaled.objects.all()  
    if request.method=="POST": 
        start_date=request.POST.get("start_date")
        end_date=request.POST.get("end_date")
     
        if start_date and end_date:
            start_date_time_obj = datetime.datetime.strptime(str(start_date), '%Y-%m-%d').date()
            end_date_time_obj = datetime.datetime.strptime(str(end_date), '%Y-%m-%d').date()
            search_result=ItemsSaled.objects.filter(created_at__lte=end_date_time_obj,created_at__gte=start_date_time_obj)

        elif start_date:
            start_date_time_obj = datetime.datetime.strptime(str(start_date), '%Y-%m-%d').date()
            search_result=ItemsSaled.objects.filter(created_at__contains=start_date)
        elif end_date:
            end_date_time_obj = datetime.datetime.strptime(str(end_date), '%Y-%m-%d').date()
            search_result=ItemsSaled.objects.filter(created_at__contains=end_date)
        else:
            search_result=[]
            messages.error("Not valid date")

        return render(request,'webapp/saled_details.html',{'saled_details':search_result})
      

    return render(request,"webapp/saled_details.html",{'saled_details':saled_details})


# def enable_employee_role(request,id):
    
#         enable = User.objects.get(id=id)
#         enable.is_active=True
#         enable.save()
#         return redirect('list_product_details')        
#     # return render(request,"management/edit_product_details.html",{'enable':enable, 'form':form})
#     else:
#         return HttpResponse('not permit')


def add_credit_balance(request):
    if request.method == "POST":
        id = request.POST.get('consultingName')
        x=Customer.objects.get(id=id)
        product=ItemsSaled.objects.filter(customer_id=x.id)
        credit=0
        for i in product:
            y=i.credit_balance
           
            credit += y

        data={'credit':credit}
        return JsonResponse(data)


def available_count(request):
    if request.method == "POST":
        product=request.POST.get('consultingName')
        print(product)
        price=Product.objects.get(id=product)
        count=price.stock_quantity 
        z=price.unit_price 
        data={'unit':z,
        'count':count} 
        return JsonResponse(data)

def add_profile(request):
    if request.method=="POST":
        form=ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"webapp/profile.html")
        else:
            return render(request,"webapp/profile.html")
    else:
        form=ProfileForm()
        return render(request,"webapp/profile.html",{'form':form})

def add_address(request):
    if request.method=="POST":
        form=AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"webapp/profile.html")
        else:
            return render(request,"webapp/profile.html")
    else:
        form=AddressForm()
        return render(request,"webapp/profile.html",{'form':form})




        
        
