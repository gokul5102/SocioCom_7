from django.shortcuts import render
# Create your views here.
from rest_framework import status,generics
from .models import Video,User,Influencer
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import json
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.db.models import Q
from .serializers import User_serializer,Video_serializer,Influencer_serializer
from rest_framework.views import APIView

# Get all videos
class GetVideos(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = Video_serializer
     model = Video
     
     def get_queryset(self):
        try:
            page = self.kwargs['pg']
            start=((page - 1)*10)
            end=start+10
            SendData= self.model.objects.all()[start:end]
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
            page = self.kwargs['pg']
            start=((page - 1)*10)
            end=start+10
            SendData= self.model.objects.all()[start:end]
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
class GetInfluencers(generics.ListAPIView):
    # permission_classes=(IsAuthenticated,)
     serializer_class = Influencer_serializer
     model = Influencer
     
     def get_queryset(self):
        try:
            page = self.kwargs['pg']
            start=((page - 1)*10)
            end=start+10
            SendData= self.model.objects.all()[start:end]
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

#update a video
class UpdateVideoById(generics.UpdateAPIView):
    serializer_class = Video_serializer
    # permission_classes = (IsAuthenticated,)
    # queryset =  Video.objects.all()
    http_method_names = ['patch']

    def update(self, request, *args, **kwargs):
        try:
            id = self.kwargs['id']
            if id is None:
                return JsonResponse({'msg':'Please Give the id'},status=status.HTTP_400_BAD_REQUEST)
            
            title=request.data.get('title')
            description=request.data.get('description')
            date_posted=request.data.get('date_posted')
            duration=request.data.get('duration')
            creator=request.data.get('creator')
    
            try:
                s=Video.objects.get(id=id)
                s.title=title
                s.description=description
                s.date_posted=date_posted
                s.duration=duration
                s.creator=creator
                s.save()
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
        