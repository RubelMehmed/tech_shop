from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import Product, Category, Order, Customer

from django.views import View


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



# class Signup(View):
#     pass

# class Login(View):
#     pass


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
