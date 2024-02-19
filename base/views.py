from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import *
from django.http import JsonResponse
from .forms import *
from decimal import Decimal
import datetime
from django.utils import timezone
from django.db.models import Sum




@login_required(login_url='user_login')
def index(request):
    total_seller = Seller.objects.all().count()
    total_customer = Customer.objects.all().count()
    total_category = Category.objects.all().count()
    total_product = Product.objects.all().count()
    total_sell_amount = sum(order.total_amount for order in Order.objects.all())
    total_order = Order.objects.all().count()
    
    now = timezone.now()
    time = datetime.timedelta(days=30)
    one = now-time
    
    last_month_total_sell_amount = sum(order.total_amount for order in Order.objects.filter(time__gte=one))
    last_month_total_order = Order.objects.filter(time__gte=one).count()
    
 

    context={
        'total_seller': total_seller,
        'total_customer': total_customer,
        'total_category': total_category,
        'total_product': total_product,
        'total_sell_amount': total_sell_amount,
        'last_month_total_sell_amount':last_month_total_sell_amount,
        'total_order': total_order,
        'last_month_total_order': last_month_total_order,
        
        
    }
    return render(request, 'base/index.html', context)

def user_login(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pw = request.POST.get('password')
        user = authenticate(username =un, password = pw)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request, 'base/login.html')


@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect('user_login')

@csrf_exempt
@login_required(login_url='user_login')
def category(request):
    
    search_term = request.GET.get('search', '')
    if search_term:
        categories = Category.objects.filter(name__icontains=search_term)
    else:
        categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    if request.method == 'POST':
        name = request.POST['name']
        code = request.POST['code']
        description = request.POST['description']
        image = request.FILES.get('image')
        print(image)
        if image:
            Category.objects.create(name= name, code =code, description= description, image = image)
        else:
            Category.objects.create(name= name, code =code, description= description)
    return render(request, 'base/category.html', context)

def delete_category(request, c_id):
    category = Category.objects.get(id = c_id)
    category.delete()
    return redirect(request.META['HTTP_REFERER'])

def delete_product(request, p_id):
    product = Product.objects.get(id = p_id)
    product.delete()
    return redirect(request.META['HTTP_REFERER'])


def edit_category(request, c_id):
    if request.method =='POST':
        pi = Category.objects.get(pk= c_id)
        fm = CategoryForm(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('manage_category')
    else:
        pi = Category.objects.get(pk= c_id)
        fm = CategoryForm(instance=pi)
    
    return render(request,'base/category_edit.html' ,{'form':fm})

def edit_product(request, p_id):
    if request.method =='POST':
        pi = Product.objects.get(pk= p_id)
        fm = ProductForm(request.POST, request.FILES, instance=pi)
        if fm.is_valid():
            fm.save()
        return redirect('manage_product')
    else:
        pi = Product.objects.get(pk= p_id)
        fm = ProductForm(instance=pi)
    
    return render(request,'base/product_edit.html' ,{'form':fm})



@login_required(login_url='user_login')
def product(request):
    search_term = request.GET.get('search', '')
    if search_term:
        products = Product.objects.filter(name__icontains=search_term)
    else:
        products = Product.objects.all()
    
    category = Category.objects.all()
    context ={
        'products': products,
        'category': category
    }
    
    if request.method == 'POST':
        name = request.POST['name']
        size = request.POST['size']
        quantity = request.POST['quantity']
        price = request.POST['price']
        category_name = request.POST['category']
        category_obj, created = Category.objects.get_or_create(name=category_name)
        description = request.POST['description']
        image = request.FILES.get('image')

        if image:
            product = Product.objects.create(name=name, size=size, quantity=quantity, price=price, description=description, image=image)
            product.categories.add(category_obj)
        else:
            product = Product.objects.create(name=name, size=size, quantity=quantity, price=price, description=description)
            product.categories.add(category_obj)

        # return JsonResponse({'Success': "Product Created"})

    return render(request, 'base/product.html', context)

@login_required(login_url='user_login')
def manage_category(request):
    search_term = request.GET.get('search', '')
    if search_term:
        categories = Category.objects.filter(name__icontains=search_term)
    else:
        categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'base/manage_category.html', context)

@login_required(login_url='user_login')
def manage_product(request):
    search_term = request.GET.get('search', '')
    if search_term:
        products = Product.objects.filter(name__icontains = search_term)
        
    else:
        products = Product.objects.all()
    context ={
        'products':products
    }
    return render(request, 'base/manage_product.html', context)


@login_required(login_url='user_login')
def seller(request):
    search_term = request.GET.get('search', '')
    if search_term:
        sellers = Seller.objects.filter(name__icontains = search_term)
        
    else:
        sellers = Seller.objects.all()
        
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        address = request.POST['address']
        number = request.POST['phone']
        status = request.POST['status']
        level = request.POST['level']
        user = User.objects.create_user(username = username, password = password, email = email, first_name = name)
        user.save()
        Seller.objects.create(user = user, name = name, email = email, address =address, number = number, status = status, level =level)
        
    context ={
        'sellers' : sellers,
    }
    return render(request, 'base/seller.html', context)


@login_required(login_url='user_login')
def Administrator(request):
    search_term = request.GET.get('search', '')
    if search_term:
        administrators = Admin_Model.objects.filter(name__icontains = search_term)
        
    else:
        administrators = Admin_Model.objects.all()
        
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        number = request.POST['phone']
        user = User.objects.create_superuser(username = username, password = password, email = email, first_name = name)
        user.save()
        Admin_Model.objects.create(user = user, name = name, email = email, number = number)
        
    context ={
        'administrators' : administrators,
    }
    return render(request, 'base/Administrator.html', context)



@login_required(login_url='user_login')
def customer(request):
    search_term = request.GET.get('search', '')
    if search_term:
        customers = Customer.objects.filter(name__icontains = search_term)
        
    else:
        customers = Customer.objects.all()
        
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        number = request.POST['phone']
        status = request.POST['status']
        level = request.POST['level']
        Customer.objects.create(name = name, email = email, address =address, number = number, status = status, level =level)
        
    context ={
        'customers' : customers,
    }
    return render(request, 'base/customer.html', context)

def delete_customer(request, id):
    customer = Customer.objects.get(id = id)
    customer.delete()
    return redirect('customer')

def delete_seller(request, id):
    seller = Seller.objects.get(id = id)
    seller_user = User.objects.get(username = seller.user.username)
    seller_user.delete()
    seller.delete()
    return redirect('seller')


def delete_admin(request, id):
    admin_obj = Admin_Model.objects.get(id = id)
    admin_user = User.objects.get(username = admin_obj.user.username)
    admin_user.delete()
    admin_obj.delete()
    return redirect('Administrator')




# @login_required(login_url='user_login')
# def sales(request):
#     return render(request, 'base/sales.html')

@login_required(login_url='user_login')
def create_sales(request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_obj = Product.objects.get(name= product_name)
        
        quantity = int(request.POST['quantity']) 
        # print(quantity)
        
        price = int(product_obj.price)
        # print(price)
        
        x = quantity*price
        # print(x)
        
        ItemBucket.objects.create(seller = request.user, products=product_obj, quantity =quantity, total =x)
        
    products = Product.objects.all()
    customers = Customer.objects.all()
    
    user = request.user
    
    seller_bucket = ItemBucket.objects.filter(seller=user)
    seller_bucket_total = 0
    for i in seller_bucket:
        seller_bucket_total += i.total
        
    print(seller_bucket_total)
    context ={
        'products': products,
        'customers': customers,
        'seller_products': seller_bucket,
        'seller_bucket_total': seller_bucket_total
    }
    return render(request, 'base/create_sales.html', context)


def bucket_delete(request, b_id):
    b_obj = ItemBucket.objects.get(id = b_id)
    b_obj.delete()
    return redirect('create_sales')


def make_order(request):
    if request.method == 'POST':
        customer = request.POST['customer']
        customer_obj = User.objects.get(id= customer)
        
        user = request.user
        seller_bucket = ItemBucket.objects.filter(seller=user)
        
        items = []
        for i in seller_bucket:
            item = OrderItems.objects.create(
                product = i.products,
                quantity = i.quantity
            )
            items.append(item)
        order = Order.objects.create(seller= user, customer = customer_obj)
        for item in items:
            order.items.add(item)

    return redirect('sales')


@login_required(login_url='user_login')
def report_customer(request):
    return render(request, 'base/report_customer.html')

@login_required(login_url='user_login')
def report_product(request):
    return render(request, 'base/report_product.html')

@login_required(login_url='user_login')
def report_seller(request):
    return render(request, 'base/report_seller.html')


def make_order(request):
    if request.method == 'POST':
        customer_id = request.POST['customer']
        customer_obj = Customer.objects.get(id= customer_id)
        
        pay_amount = request.POST['pay_amount']
        
        user = request.user
        seller_bucket = ItemBucket.objects.filter(seller=user)
        
        items = []
        for i in seller_bucket:
            item = OrderItems.objects.create(
                product = i.products,
                quantity = i.quantity
            )
            items.append(item)
        order = Order.objects.create(seller= user, customer = customer_obj, pay_amount=pay_amount)
        for item in items:
            order.items.add(item)
            
        seller_bucket.delete()
    return redirect('/')


def order(request):
    if request.user.is_staff:
        order_details = Order.objects.all()
    else:
        order_details = Order.objects.filter(seller = request.user)

    context ={
        'order_details': order_details
    }
    return render(request, 'base/payments.html', context)

   

   


def make_payment(request, o_id):
    order_obj = Order.objects.get(id=o_id)
    
    if request.method == 'POST':
        new_payment_amount_str = request.POST['new_payment_amount']

        try:
            new_payment_amount = int(new_payment_amount_str)
        except ValueError:
            # Handle the case where the input is not a valid integer
            # You might want to display an error message or take appropriate action
            pass
        else:
            order_obj.pay_amount += new_payment_amount
            order_obj.save()
    # order_obj.
    context ={
        'order_detail': order_obj
    }
    return render(request, 'base/sales.html', context)
    


def payment_details(request):
    pass
