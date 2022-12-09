from django.urls import path

from . import views

urlpatterns = [
 
    # path('', views.navbar, name='navbar'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.user_logout, name='user_logout'),
    path('employee/', views.employee, name='employee'),
    path('role/<int:id>/', views.role, name='role'),
    path('remove_role/<int:id>/', views.remove_role, name='remove_role'),
    path('add_product/', views.add_product, name='add_product'),
    path('view_product/<int:id>/', views.view_product, name='view_product'),
    path('edit_product/<int:id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('sale/', views.sale, name='sale'),
    path('search_customer/', views.search_customer, name='search_customer'),
    path('saled_records/', views.saled_records, name='saled_records'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('relieval_employee/<int:id>/', views.relieval_employee, name='relieval_employee'),
    path('activating_employee/<int:id>/', views.activating_employee, name='activating_employee'),
    path('add_credit_balance/', views.add_credit_balance, name='add_credit_balance'),
    path('available_count/', views.available_count, name='available_count'),
    path('add_profile/', views.add_profile, name='add_profile'),
    path('add_address/', views.add_address, name='add_address'),


  

   







    


    

    



    
    
    
    ]