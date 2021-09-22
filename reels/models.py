from django.db import models
from django.utils import timezone
# Create your models here.



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255, blank=True)
    organisation_name = models.CharField(max_length=100)
    mobile_no= models.CharField(max_length=10,blank=True)
    age= models.IntegerField(default=25)


    def __str__(self):
        return self.name

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    duration = models.IntegerField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    likes=models.IntegerField(null=True,default=0)
    review = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.title

class Influencer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255, blank=True)
    mobile_no= models.CharField(max_length=10)
    charges= models.IntegerField()
    
    def __str__(self):
        return self.name