from django import template
register=template.Library()

@register.filter(name='currency')
def currency(num):
    return 'Tk. ' + str(num)

@register.filter(name='discount')
def discount(num):
    return 'Discount: ' + str(num) + '%'

@register.filter(name='price')
def price(num,num1):
    p=num1-((num*num1)/100)
    return  str(p) + 'Tk.'
 

# @register.filter(name='discount')
# def discount(num):
#     return 'Discount: '+ str(num) + ' %'

# @register.filter(name='price')
# def price(num,num1):
#     price=num-((num*num1)/100)
#     return ' Tk. ' + str(price)



# @register.filter(name='currency')
# def currency(number):
#     return "BDT "+str(number)
