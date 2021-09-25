from django.shortcuts import render
# Create your views here.
from rest_framework import status,generics
from .models import Ecommerce_User,Payment,Seller,OrderedProducts,Product
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import json
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.db.models import Q
from .serializers import Ecommerce_User_serializer,Product_serializer,Payment_serializer,OrderedProducts_serializer,Seller_serializer
from rest_framework.views import APIView
import requests
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



# Get all users
class GetUsers(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = Ecommerce_User_serializer
     model = Ecommerce_User
     
     def get_queryset(self):
        try:
            SendData= self.model.objects.all()
            return SendData
        except self.model.DoesNotExist:
        	return  Response ({"status": 404, "message" : "Data not found"}, status=status.HTTP_404_NOT_FOUND)

     def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response ({"status": 400, "message" : "{}".format(e)}, status=status.HTTP_400_BAD_REQUEST)

# Get all sellers
class GetSellers(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = Seller_serializer
     model = Seller
     
     def get_queryset(self):
        try:
            SendData= self.model.objects.all()
            return SendData
        except self.model.DoesNotExist:
        	return  Response ({"status": 404, "message" : "Data not found"}, status=status.HTTP_404_NOT_FOUND)

     def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response ({"status": 400, "message" : "{}".format(e)}, status=status.HTTP_400_BAD_REQUEST)

#video by id
class GetProductById(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = Product_serializer
    #  permission_classes = (IsAuthenticated,)
     model = Product

     def get_queryset(self):
        try:
            id= self.kwargs['id']
            product=self.model.objects.filter(id=id)
            return product
        except self.model.DoesNotExist:
        	return  Response ({"status": 404, "message" : "Data not found"}, status=status.HTTP_404_NOT_FOUND)

     def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response ({"status": 400, "message" : "{}".format(e)}, status=status.HTTP_400_BAD_REQUEST)

#update a product by id
class UpdateProductById(generics.UpdateAPIView):
    serializer_class = Product_serializer
    # permission_classes = (IsAuthenticated,)
    queryset =  Product.objects.all()
    # video = Video.objects.get()
    http_method_names = ['patch']
    def update(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            if pk is None:
                return JsonResponse({'msg':'Please Give the id'},status=status.HTTP_400_BAD_REQUEST)
            
            title=request.data.get('title')
            description=request.data.get('description')
            price=request.data.get('price')
            discount_price=request.data.get('discount_price')
            image=request.data.get('image')
            category=request.data.get('category')

            try:
                vs=Product.objects.get(id=pk)
            except ObjectDoesNotExist:
                return JsonResponse({'msg':'Does Not Exist'},status=status.HTTP_404_NOT_FOUND)
    
           
            try:
                super(UpdateProductById, self).update(request, *args, **kwargs)
                return Response ({"status": 200, "message" : 'update successfully.'}, status=status.HTTP_201_CREATED)

            except Exception as e:
        	    print(e)
        	    return JsonResponse({'msg':f'{e}'},status=status.HTTP_400_BAD_REQUEST)
            
           

        except Exception as e:
            print(e)
            return JsonResponse({'msg':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)  


#delete product by id
class DeleteProductById(APIView):
    serializer_class = Product_serializer
    model = Product
    def delete(self,request,id):
        try:
            s=self.model.objects.get(id=id)
            s.delete()
            return JsonResponse({'msg':'Product is Successfully Deleted'},status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return JsonResponse({'msg':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
#user by id
class GetUserById(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = Ecommerce_User_serializer
    #  permission_classes = (IsAuthenticated,)
     model = Ecommerce_User

     def get_queryset(self):
        try:
            id= self.kwargs['id']
            user=self.model.objects.filter(id=id)
            return user
        except self.model.DoesNotExist:
        	return  Response ({"status": 404, "message" : "Data not found"}, status=status.HTTP_404_NOT_FOUND)

     def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response ({"status": 400, "message" : "{}".format(e)}, status=status.HTTP_400_BAD_REQUEST)

#seller by id
class GetSellerById(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = Seller_serializer
    #  permission_classes = (IsAuthenticated,)
     model = Seller

     def get_queryset(self):
        try:
            id= self.kwargs['id']
            seller=self.model.objects.filter(id=id)
            return seller
        except self.model.DoesNotExist:
        	return  Response ({"status": 404, "message" : "Data not found"}, status=status.HTTP_404_NOT_FOUND)

     def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response ({"status": 400, "message" : "{}".format(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetProductsOfSeller(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = Seller_serializer
    #  permission_classes = (IsAuthenticated,)
     model = Seller

     def get_queryset(self):
        try:
            id= self.kwargs['id']
            seller=self.model.objects.filter(id=id)
            products=Product.objects.filter(seller=seller)
            return products
        except self.model.DoesNotExist:
        	return  Response ({"status": 404, "message" : "Data not found"}, status=status.HTTP_404_NOT_FOUND)

     def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response ({"status": 400, "message" : "{}".format(e)}, status=status.HTTP_400_BAD_REQUEST)

            

class GetCartOfUser(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = Ecommerce_User_serializer
    #  permission_classes = (IsAuthenticated,)
     model = Ecommerce_User

     def get_queryset(self):
        try:
            id= self.kwargs['id']
            user=self.model.objects.filter(id=id)
            cart=OrderedProducts.objects.filter(user=user)
            return cart
        except self.model.DoesNotExist:
        	return  Response ({"status": 404, "message" : "Data not found"}, status=status.HTTP_404_NOT_FOUND)

     def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response ({"status": 400, "message" : "{}".format(e)}, status=status.HTTP_400_BAD_REQUEST)


# def home(request):
#     return render(request,'ecommerce/home.html')

#seller signup
class CreateSeller(APIView):
    def post(self,request):
        # print(id)
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            password = request.data.get('password')
            organisation_name = request.data.get('organisation_name')
            mobile_no= request.data.get('mobile-no')
            gst_no=request.data.get('gst_no')
         
            URL = "https://appyflow.in/api/verifyGST/"
            PARAMS = {'gstNo':gst_no, 'key_secret':'9r3bDyaKsPO2aB649Ae23SUllZy1'}
            r = requests.get(url = URL, params = PARAMS)
            data = r.json()
            # if data.error == True:
            #     return JsonResponse({'msg':'Gst No is incorrect'},status=status.HTTP_404_NOT_FOUND)
            u=Seller.objects.create(name=name, email=email, password=password, mobile_no=mobile_no,organisation_name=organisation_name,gst_no=gst_no)
            serializer = Seller_serializer(u)
            return JsonResponse({'msg':'Seller is Successfully Created'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse({'msg':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)  

# @login_required
# class CreateProduct(APIView):
#     def post(self,request):
#         # print(id)
#         try:
#            title=request.data.get('title')
#            description=request.data.get('description')
#            price=request.data.get('price')
#            discount_price=request.data.get('discount_price')
#            seller_id=request.data.get('seller')
#            u=Product.objects.get(id=int(seller_id))
#            v=Product.objects.create(title=title,description=description,creator=u,price=price,discount_price=discount_price)
#         #    print(u)
#         #    print("11")
#         #    print(v)
#            serializer = Product_serializer(v)
#            return JsonResponse({'msg':'Product is Successfully Created'},status=status.HTTP_200_OK)
#         except Exception as e:
#             print(e)
#             return JsonResponse({'msg':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)  


#seller login
class CheckSeller(APIView):
    def post(self,request,name):
        # print(id)
        try:
            password=request.data.get('password')
            u=Seller.objects.get(name=name)
            if(u.password==password):
                return JsonResponse({'msg':'Seller is Present'},status=status.HTTP_200_OK)
            else:
                return JsonResponse({'msg':'Password is incorrect'},status=status.HTTP_404_NOT_FOUND)
        except u.DoesNotExist:
            return JsonResponse({'msg':'Seller Does not exist'},status=status.HTTP_400_BAD_REQUEST) 

#User signup 
class CreateUser(APIView):
    def post(self,request):
        # print(id)
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            password = request.data.get('password')
            organisation_name = request.data.get('organisation_name')
            mobile_no= request.data.get('mobile-no')
            gst_no=request.data.get('gst_no')
         
            URL = "https://appyflow.in/api/verifyGST/"
            PARAMS = {'gstNo':gst_no, 'key_secret':'9r3bDyaKsPO2aB649Ae23SUllZy1'}
            r = requests.get(url = URL, params = PARAMS)
            data = r.json()
            if data.error == True:
                return JsonResponse({'msg':'Gst No is incorrect'},status=status.HTTP_404_NOT_FOUND)
            u=Seller.objects.create(name=name, email=email, password=password, mobile_no=mobile_no,organisation_name=organisation_name,gst_no=gst_no)
            serializer = Seller_serializer(u)
            return JsonResponse({'msg':'Seller is Successfully Created'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse({'msg':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST) 

#routes
# @unauthenticated_user
def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        mobile_no = request.POST['mobile_no']
        organisation_name = request.POST['organisation_name']
        gst_no = request.POST['gst_no']

        s = Seller.objects.create(name=name, email=email, password=password,mobile_no=mobile_no,organisation_name=organisation_name,gst_no=gst_no)
        return redirect('ecom/login')
    else:
        return render(request, 'ecommerce/signup.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']

        request.session['name'] = name
        s = Seller.objects.get(name=name, password=password)
        
        if s is not None:
            return redirect('/ecom/create_product')
        else:
            print("Invalid credentials of seller")
            
    return render(request, 'ecommerce/login.html')

def CreateProduct(request):
     if request.method == 'POST':
           title=request.POST['title']
           description=request.POST['description']
           price=request.POST['price']
           discount_price=request.POST['discount_price']
           image=request.POST['image']
           category=request.POST['category']
        #    print(u)
        #    print("11")
        #    print(v)
       
           print(request.session['name'])
           name = request.session['name']
           s=Seller.objects.get(name=name)
           v=Product.objects.create(title=title,description=description,seller=s,category=category,price=price,discount_price=discount_price,image=image)
           return redirect('/ecom/create_product')

     return render(request, 'ecommerce/upload_products.html')
        

def GetProducts(request):
    # permission_classes=(IsAuthenticated,)
    #  serializer_class = Product_serializer
    #  model = Product
    #   
    product_inventory_list =Product.objects.all().order_by('title')

    return render(request, "ecommerce/index.html", {"product_inventory_list": product_inventory_list})

def GetBeds(request):
    # permission_classes=(IsAuthenticated,)
    #  serializer_class = Product_serializer
    #  model = Product
    #   
    product_inventory_list =Product.objects.filter(category="beds")
    print(product_inventory_list)

    return render(request, "ecommerce/bed.html", {"product_inventory_list": product_inventory_list})

def GetTables(request):
    # permission_classes=(IsAuthenticated,)
    #  serializer_class = Product_serializer
    #  model = Product
    #   
    product_inventory_list =Product.objects.filter(category="tables")

    return render(request, "ecommerce/tables.html", {"product_inventory_list": product_inventory_list})

def Cart(request):
     return render(request, "ecommerce/cart.html")