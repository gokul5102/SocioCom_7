from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

class Ecommerce_User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255, blank=True)
    mobile_no= models.CharField(max_length=10,blank=True)
    age= models.IntegerField(default=25)
    address=models.TextField()


    def __str__(self):
        return self.name

class Seller(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255, blank=True)
    organisation_name = models.CharField(max_length=100)
    mobile_no= models.CharField(max_length=10,blank=True)
    gst_no=models.CharField(max_length=15,default='123456789012345')
    
    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    description = models.TextField(null=True)
    image = models.ImageField()
    seller= models.ForeignKey(Seller,on_delete=models.CASCADE)
    category = models.CharField(max_length=100,null=True)

    def __str__(self):
        if(self.title):
            return self.title


class OrderedProducts(models.Model):
    user = models.ForeignKey(Ecommerce_User,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    product = models.ForeignKey(Product,null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField(default=1)
    date_purchased = models.DateTimeField(default=timezone.now)

    def __str__(self):
            return f"{self.id}"

    def get_total_item_price(self):
        return self.quantity * self.product.price

    def get_total_discount_item_price(self):
        return self.quantity * self.product.discount_price


class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(Ecommerce_User,
                             on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name





