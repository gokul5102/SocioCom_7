from rest_framework import serializers
from .models import Ecommerce_User,Product,Payment,OrderedProducts,Seller

class Ecommerce_User_serializer(serializers.ModelSerializer):
    class Meta:
        model = Ecommerce_User
        # fields = '__all__'
        exclude = [ 'password' ]

class Seller_serializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        # fields = '__all__'
        exclude = [ 'password' ]

class Product_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Payment_serializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
    

class OrderedProducts_serializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProducts
        fields = '__all__'
   