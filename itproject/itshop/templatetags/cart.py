from django import template
register = template.Library()

@register.filter (name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return True
    return False;


@register.filter (name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys ()
    for id in keys:
        if int (id) == product.id:
            return cart.get (id)
    return 0;

@register.filter (name='price_total')
def price_total(product, cart):
    return product.sell_price * cart_quantity (product, cart)

@register.filter (name='total_cart_price')
def total_cart_price(products, cart):
    sum = 0;
    for p in products:
        sum += price_total (p, cart)

    return sum


@register.filter (name='TOTAL_PRICE')
def TOTAL_PRICE(products):
    total=0
    for i in products:
        s=i.sell_price-(i.sell_price*i.discount)/100
        total=total+s
    return 'Tk. ' + str(total)



@register.filter (name='grand_total')
def grand_total(products, charge):
    total=0
    for i in products:
        s=i.sell_price-(i.sell_price*i.discount)/100
        total=total+s
        total=total+charge
    return 'Tk. ' + str(total)    