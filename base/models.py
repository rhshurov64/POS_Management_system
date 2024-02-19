from django.db import models
from django.contrib.auth.models import User
# Create your models here.


Product_Size = ( 
    ("M", "M"), 
    ("L", "L"), 
    ("XL", "XL"), 
) 
customer_level =(
    ('New Customer', 'New Customer'),
    ('Level-1', 'Level-1'),
    ('Level-2', 'Level-2'),
    ('Level-3', 'Level-3'),
    ('Top Rated Customer', 'Top Rated Customer'),
)
seller_level =(
    ('New Seller', 'New Seller'),
    ('Level-1', 'Level-1'),
    ('Level-2', 'Level-2'),
    ('Level-3', 'Level-3'),
    ('Top Rated Seller', 'Top Rated Seller'),
)
status =(
    ('Active', 'Active'),
    ('Inactive', 'Inactive')
)


class Category(models.Model):
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=500)
    description = models.CharField(max_length=5000, null=True, blank=True)
    image = models.ImageField(upload_to='category/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    
    
    
class Product(models.Model):
    name = models.CharField(max_length=500)
    code = models.CharField(max_length=500)
    size = models.CharField(max_length=100, choices=Product_Size)
    price = models.IntegerField()
    quantity = models.PositiveIntegerField()
    description = models.CharField(max_length=500)
    categories = models.ManyToManyField(Category, related_name='categories')
    image = models.ImageField(upload_to='product/', null=True, blank=True)
    
    def __str__(self):
        return self.name


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    address = models.TextField(max_length = 500)
    number = models.CharField(max_length = 15)
    status = models.CharField(max_length = 50, choices= status, default = 'Active' )
    level = models.CharField(max_length = 50, choices =seller_level, default = 'New Seller')
    joined_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return str(self.name)


class Admin_Model(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    number = models.CharField(max_length = 15)
    joined_date = models.DateTimeField(auto_now_add = True)
    
    
    def __str__(self):
        return str(self.name)



class Customer(models.Model):
    name = models.CharField(max_length = 500)
    email = models.CharField(max_length = 500)
    address = models.TextField(max_length = 500)
    number = models.CharField(max_length =15)
    status = models.CharField(max_length = 50, choices= status, default = 'Active' )
    level = models.CharField(max_length = 50, choices= customer_level, default = 'New Customer')
    joined_date = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return str(self.name)



class ItemBucket(models.Model):
    seller = models.ForeignKey(User, on_delete = models.CASCADE)
    products = models.ForeignKey(Product , on_delete = models.CASCADE)
    quantity = models.IntegerField(null = True, blank = True)
    total = models.IntegerField(null = True, blank = True)
    
    def __str__(self):
        return str(self.seller)
    

class OrderItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    
    def calculate_item_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return str(f'{self.product.name} - {self.product.quantity}')
    
class Order(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders_as_seller')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders_as_customer', null = True, blank = True)
    items = models.ManyToManyField(OrderItems, null=True, blank=True)
    pay_amount = models.IntegerField(null=True, blank=True)
    deliverd = models.BooleanField(default=False, blank=True)
    time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    
    
    @property
    def total_amount(self):
        total = 0
        for item in self.items.all():
            total = total + item.calculate_item_total()
        return total
    
    @property
    def due_amount(self):
        due = self.total_amount - self.pay_amount
        return due
    
    
    @property
    def status(self):
        if self.total_amount == self.pay_amount:
            status_value = "Completed"
        else:
            status_value = "Pending"
        return status_value
    
    def __str__(self):
        return str(self.id)
