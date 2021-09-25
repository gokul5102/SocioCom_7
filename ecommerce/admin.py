from django.contrib import admin
from .models import Ecommerce_User,Payment,Seller,OrderedProducts,Product
# Register your models here.
admin.site.register(Ecommerce_User)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(OrderedProducts)
admin.site.register(Seller)
