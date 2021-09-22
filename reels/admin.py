from django.contrib import admin
from .models import User,Video,Influencer
# Register your models here.
admin.site.register(User)
admin.site.register(Video)
admin.site.register(Influencer)