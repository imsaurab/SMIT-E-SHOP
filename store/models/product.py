from django.db import models


CATEGORY_CHOICES=(
    ('M','Agreculture'),
    ('U','Unstensils'),
    ('TW','Wepons'),
    ('T','Tools'),
)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')

    def __str__(self):
        return str(self.id)