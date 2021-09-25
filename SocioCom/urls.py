
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reels/', include('reels.urls')),
    #api's
    path('ecommerce/', include('ecommerce.urls')),
   
    #routes
    path('ecom/', include('ecommerce.urls')),
    path('',TemplateView.as_view(template_name='index.html')),
]
