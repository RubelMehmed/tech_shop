from django.db import models

# Create your models here.

from django.db import models
import datetime

class Category(models.Model):
    name=models.CharField(max_length=40)
    
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
    
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=50)
    purchage_price=models.IntegerField(default=0)
    sell_price=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='uploads/products/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    
    @staticmethod
    def get_products_by_category_id(category_id):
        if category_id: 
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()
    
class Customer(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    cell=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=20)

    def register(self):
        self.save()
   
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False

class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    delevery_address=models.CharField(max_length=200)
    price=models.IntegerField(default=0)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)
    phone=models.CharField(max_length=15)
    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
