from django.contrib import admin
from .models import Category, Product, Customer, Order

# Register your models here.
admin.site.register(Category)
# admin.site.register(Product)

class CustomerAdmin(admin.ModelAdmin):
    
    def Full_Name(self):
        return self.first_name + ' '+ self.last_name
    
    list_display=(Full_Name,'cell')
    list_filter=('email',)
    
    
admin.site.register(Customer,CustomerAdmin)

admin.site.register(Order)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id','name','purchage_price','sell_price','discount')
    list_filter=('category',)

admin.site.register(Product,ProductAdmin)



# admin.site.site_header='IT Shop'
# admin.site.index_title = 'Customization App'