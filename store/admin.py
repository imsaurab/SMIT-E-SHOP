
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
 Customer,
 Product,
 Cart,
 Order,
 Payment
)

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id', 'user', 'name', 'locality', 'city', 'zipcode', 'state']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'selling_price', 'discounted_price', 'description', 'brand','category', 'product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'user','product','quantity']
    
@admin.register(Order)
class OrderPlacedModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'user', 'customer', 'customer_info', 'product', 'product_info', 'quantity', 'ordered_date', 'status']

 def product_info(self, obj):
  link = reverse("admin:app_product_change", args=[obj.product.pk])
  return format_html('<a href="{}">{}</a>', link, obj.product.title)

 def customer_info(self, obj):
  link = reverse("admin:app_customer_change", args=[obj.customer.pk])
  return format_html('<a href="{}">{}</a>', link, obj.customer.name)


class PaymentAdmin(admin.ModelAdmin):
    model = Payment   
    list_display = [ "order_id" , 'get_user'  , 'status'] 
    

    def get_user(self , payment):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")
    
admin.site.register(Payment , PaymentAdmin) 
#admin.site.register(Order) 
#admin.site.register(Cart)




