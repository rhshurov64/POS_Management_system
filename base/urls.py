from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('category/', views.category, name='category'),
    path('product/', views.product, name='product'),
    path('manage_category/', views.manage_category, name='manage_category'),
    path('manage_product/', views.manage_product, name='manage_product'),
]
