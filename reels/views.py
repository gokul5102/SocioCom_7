from django.shortcuts import render
# Create your views here.
from rest_framework import status,generics
from .models import Video,User
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import json
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.db.models import Q
from .serializers import User_serializer,Video_serializer
from rest_framework.views import APIView
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.applications import imagenet_utils
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import itertools
import os
import shutil
import random
import matplotlib.pyplot as plt
# %matplotlib inline
from io import BytesIO
from urllib.request import urlopen
import requests
from django.db.models import Max
# Get all videos
class GetVideos(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = Video_serializer
     model = Video
     
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

# Get all users
class GetUsers(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = User_serializer
     model = User
     
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

# Get all influencers
# class GetInfluencers(generics.ListAPIView):
#     # permission_classes=(IsAuthenticated,)
#      serializer_class = Influencer_serializer
#      model = Influencer
     
#      def get_queryset(self):
#         try:
#             SendData= self.model.objects.all()
#         except self.model.DoesNotExist:
#         	return  Response ({"status": 404, "message" : "Data not found"}, status=status.HTTP_404_NOT_FOUND)

#      def list(self, request, *args, **kwargs):
#         try:
#             serializer = self.get_serializer(self.get_queryset(), many=True)
#             return Response(serializer.data)
#         except Exception as e:
#             print(e)
#             return Response ({"status": 400, "message" : "{}".format(e)}, status=status.HTTP_400_BAD_REQUEST)

#video by id
class GetVideoById(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = Video_serializer
    #  permission_classes = (IsAuthenticated,)
     model = Video

     def get_queryset(self):
        try:
            id= self.kwargs['id']
            video=self.model.objects.filter(id=id)
            return video
        except self.model.DoesNotExist:
        	return  Response ({"status": 404, "message" : "Data not found"}, status=status.HTTP_404_NOT_FOUND)

     def list(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response ({"status": 400, "message" : "{}".format(e)}, status=status.HTTP_400_BAD_REQUEST)

#signup
class CreateUser(APIView):
    def post(self,request):
        # print(id)
        try:
            name = request.data.get('name')
            email = request.data.get('email')
            password = request.data.get('password')
            mobile_no= request.data.get('mobile_no')
            age= request.data.get('age')
            u=User.objects.create(name=name, email=email, password=password, mobile_no=mobile_no, age=age)
            serializer = User_serializer(u)
            return JsonResponse({'msg':'User is Successfully Created'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse({'msg':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)  

#login
class CheckUser(APIView):
    def post(self,request,name):
        # print(id)
        try:
            password=request.data.get('password')
            u=User.objects.get(name=name)
            if(u.password==password):
                return JsonResponse({'msg':'User is Present'},status=status.HTTP_200_OK)
            else:
                return JsonResponse({'msg':'Password is incorrect'},status=status.HTTP_404_NOT_FOUND)
        except u.DoesNotExist:
            return JsonResponse({'msg':'User Does not exist'},status=status.HTTP_400_BAD_REQUEST)  


class CreateVideo(APIView):
    def post(self,request):
        # print(id)
        try:
           title=request.data.get('title')
           description=request.data.get('description')
           url=request.data.get('url')
           creator_id=request.data.get('creator')
           u=User.objects.get(id=int(creator_id))
           v=Video.objects.create(title=title,description=description,creator=u,url=url)
        #    print(u)
        #    print("11")
        #    print(v)
           serializer = Video_serializer(v)
           return JsonResponse({'msg':'Video is Successfully Created'},status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return JsonResponse({'msg':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)  

        
#update a video
class UpdateVideoById(generics.UpdateAPIView):
    serializer_class = Video_serializer
    # permission_classes = (IsAuthenticated,)
    queryset =  Video.objects.all()
    # video = Video.objects.get()
    def patch(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            if pk is None:
                return JsonResponse({'msg':'Please Give the id'},status=status.HTTP_400_BAD_REQUEST)
            
            title=request.data.get('title')
            description=request.data.get('description')
            date_posted=request.data.get('date_posted')
            duration=request.data.get('duration')
            creator=request.data.get('creator')
    
            try:
                s=Video.objects.get(id=pk)
                s.title=title
                s.description=description
                s.date_posted=date_posted
                s.duration=duration
                s.creator=creator
                s.save()
                serializer = Video_serializer(s)
                return Response(serializer.data)
            except ObjectDoesNotExist:
                return JsonResponse({'msg':'Video Does Not Exist'},status=status.HTTP_404_NOT_FOUND)

        
        except Exception as e:
            print(e)
            return JsonResponse({'msg':'{}'.format(e)},status=status.HTTP_400_BAD_REQUEST)  


#delete video by id
class DeleteVideoById(APIView):
    serializer_class = Video_serializer
    model = Video
    def delete(self,request,id):
        try:
            s=self.model.objects.get(id=id)
            s.delete()
            return JsonResponse({'msg':'Video is Successfully Deleted'},status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return JsonResponse({'msg':'Not Found'},status=status.HTTP_404_NOT_FOUND)


class MlModel(APIView):
    serializer_class = Video_serializer
    model = Video
    def prepare_image(self,request):
        highest_likes = Video.objects.aggregate(Max('quantity'))
        url = highest_likes.url
        # def loadImage(URL):
        #     with urllib.request.urlopen(URL) as url:
        #         img = image.load_img(BytesIO(url.read()), target_size=(125, 125))

        #     return image.img_to_array(img)
        # mobile = tf.keras.applications.mobilenet.MobileNet()
        mobile = tf.keras.applications.mobilenet.MobileNet()
        response = requests.get(url)
        file = open("sample_image.png", "wb")
        file.write(response.content)
        file.close()
        img_path = '/sample_image.png/'
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array_expanded_dims = np.expand_dims(img_array, axis=0)
        return imagenet_utils.decode_predictions(mobile.predict(tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)))
    # preprocessed_image = prepare_image(url)
    # predictions = mobile.predict(prepare_image(<url>))
    # results = imagenet_utils.decode_predictions(predictions)

# class Nlp(APIView):
#     model = Video
#     def recomendations(seld, request):
#         for i in Video.objects.all():
#             desc = i.description()
#             dic = {}
#             for j in desc:
#                 if j in dic:
#                     dic[j] +=1
#                 else:
#                     dic[j] = 1
#             for j in i.user_liked:
                
        