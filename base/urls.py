from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('category/', views.category, name='category'),
    path('product/', views.product, name='product'),
    path('manage_category/', views.manage_category, name='manage_category'),
    path('delete_category/<int:c_id>/', views.delete_category, name='delete_category'),
    path('delete_product/<int:p_id>/', views.delete_product, name='delete_product'),
    path('edit_category/<int:c_id>/', views.edit_category, name='edit_category'),
    path('edit_product/<int:p_id>/', views.edit_product, name='edit_product'),
    
    path('manage_product/', views.manage_product, name='manage_product'),
    path('Administrator/', views.Administrator, name='Administrator'),
    path('delete_admin/<int:id>/', views.delete_admin, name='delete_admin'),
    path('seller/', views.seller, name='seller'),
    path('delete_seller/<int:id>/', views.delete_seller, name='delete_seller'),
    path('customer/', views.customer, name='customer'),
    path('delete_customer/<int:id>/', views.delete_customer, name='delete_customer'),
    # path('sales/', views.all_order_details, name='sales'),
    path('create_sales/', views.create_sales, name='create_sales'),
    path('bucket_delete/<int:b_id>/', views.bucket_delete, name='bucket_delete'),
    path('report_customer/', views.report_customer, name='report_customer'),
    path('report_seller/', views.report_seller, name='report_seller'),
    path('report_product/', views.report_product, name='report_product'),
    
    path('make_order/', views.make_order, name='make_order'),
    path('make_payment/<int:o_id>/', views.make_payment, name='make_payment'),
    path('order/', views.order, name='order'),
    # path('pending_order/', views.pending_order, name='pending_order'),
    
    
    
    
    
    
    
    
]
