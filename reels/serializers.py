from rest_framework import serializers
from .models import User,Video

class User_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        exclude = [ 'password' ]

# class Influencer_serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Influencer
#         # fields = '__all__'
#         exclude = [ 'password' ]

class Video_serializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'
   