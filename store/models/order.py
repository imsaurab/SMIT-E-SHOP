from django.db import models
from .product import Product
from .customer import Customer
import datetime
from django.contrib.auth.models import User


STATUS_CHOICES=(
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
)    

class Order(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')    
    
# Below Property will be used by orders.html page to show total cost

@property
def total_cost(self):
   return self.quantity * self.product.discounted_price