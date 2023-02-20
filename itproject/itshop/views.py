from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import HttpResponseRedirect, redirect, render
from django.views import View

from .models import Category, Customer, Order, Product


# Create your views here.
class Index(View):

    def post(self , request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        print('cart' , request.session['cart'])
        return redirect('homepage')

    def get(self , request):
        # print()
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')

def store(request):
    cart = request.session.get('cart')
    if not cart:
        request.session['cart'] = {}   
         
    products = None
    categories = Category.get_all_categories()
    
    categoryID = request.GET.get('category')
    
    if categoryID:
        products = Product.get_products_by_category_id(categoryID)
    else:
        products = Product.get_all_products()

    data = {}
    data['products'] = products
    data['cats'] = categories

    # print('you are : ', request.session.get('email'))
    return render(request, 'itshop/index.html', data)

class Cart(View) :
    def get(self,request):
        ids=list(request.session.get('cart').keys())
        products=Product.get_product_by_id(ids)
        return render(request, 'itshop/cart.html', {'products':products})
        
# class Cart(View):
#     def get(self , request):
#         ids = list(request.session.get('cart').keys())
#         products = Product.get_product_by_id(ids)
#         return render(request , 'itshop/cart.html' , {'products' : products} )



class Signup(View):
    pass


class Check_out(View):
    def post(self,request):
        name=request.POST.get('name')
        address=request.POST.get('address')
        cell=request.POST.get('cell')
        customer = request.session.get('customer')
        # customer=Customer.objects.get(id=1)
        cart=request.session.get('cart')
        products=Product.get_product_by_id(list(cart.keys()))

        for product in products:
            order = Order(
                product=product,
                customer=customer,
                quantity=1,
                delevery_address=address,
                price=product.sell_price - (product.sell_price * product.discount / 100),
                status=False,
                phone=cell
            )


            # order=Order(
            #     product=product,
            #     customer=customer,
            #     quantity=1,
            #     delivery_address=address,
            #     price=product.sell_price-(product.sell_price*product.discount)/100,
            #     status='pending',
            #     phone=cell

            # )
            order.placeOrder()
            orders=Order.get_orders_by_customer(customer.id)
        request.session['cart'] = {}
        return render(request, 'itshop/orders.html', {'products':products})


# class CheckOut(View):
#     def post(self, request):
#         address = request.POST.get('address')
        
#         phone = request.POST.get('phone')
#         # print('++++++++++++++++++++'+ phone + '++++++++++++++++')
#         # customer = request.session.get('customer')
#         # customer=Customer.objects.get(1)
       
        
#         cart = request.session.get('cart')
#         products = Product.get_product_by_id(list(cart.keys()))
        
#         for product in products:
#             print(cart.get(str(product.id)))
#             order = Order(
#                           customer=Customer(id=1),
#                         #   customer=Customer.objects.get(1),
#                           product=product,
#                           price=product.sell_price,
#                           delevery_address=address,
#                           phone=phone,
#                           quantity=cart.get(str(product.id)))
#             order.save()
#         request.session['cart'] = {}

#         return redirect('cart')


# class OrderView(View):
#     def get(self , request ):
#         customer = request.session.get('customer')
#         orders = Order.get_orders_by_customer(customer)
#         print(orders)
#         return render(request , 'orders.html'  , {'orders' : orders})


# def logout(request):
#     request.session.clear()
#     return redirect('login')


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get ('return_url')
        return render (request, 'itshop/login.html')

    def post(self, request):
        email = request.POST.get ('email')
        password = request.POST.get ('password')
        customer = Customer.get_customer_by_email (email)
        error_message = None
        if customer:
            flag = check_password (password, customer.password)
            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect (Login.return_url)
                else:
                    Login.return_url = None
                    return redirect ('homepage')
            else:
                error_message = 'Invalid !!'
        else:
            error_message = 'Invalid !!'

        print (email, password)
        return render (request, 'itshop/login.html', {'error': error_message})