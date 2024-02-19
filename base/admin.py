from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =['id','name','image','code','size', 'price','quantity','description', 'get_category']
    
    @admin.display(description='categories')
    def get_category(self, obj):
        return [category.name for category in obj.categories.all()]
    
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'code', 'get_products']

    @admin.display(description='products')
    def get_products(self, obj):
        return [product.name for product in obj.categories.all()]
    
    
    
    
@admin.register(Customer)
class CutomerAdmin(admin.ModelAdmin):
    list_display =['name','email','address','joined_date','number', 'status', 'level']
    
@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display =['user', 'name','email','address','joined_date','number', 'status', 'level']
    
@admin.register(Admin_Model)
class Admin_ModelAdmin(admin.ModelAdmin):
    list_display =['user', 'name','email','joined_date','number']
    
    
@admin.register(ItemBucket)
class Admin_ModelAdmin(admin.ModelAdmin):
    list_display =['id', 'seller','products', 'quantity', 'total']
    
   
@admin.register(OrderItems)
class Admin_ModelAdmin(admin.ModelAdmin):
    list_display =['id', 'product','quantity', 'calculate_item_total']
    
   
@admin.register(Order)
class Admin_ModelAdmin(admin.ModelAdmin):
    list_display =['id','time', 'seller','get_products', 'total_amount', 'due_amount', 'pay_amount', 'due_amount', 'status']
    
    @admin.display(description='products')
    def get_products(self, obj):
        return [item.product.name for item in obj.items.all()]
   
