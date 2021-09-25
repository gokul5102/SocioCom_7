from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from .views import CreateProduct,CreateSeller,GetProductById,UpdateProductById,DeleteProductById,GetSellers,GetProductsOfSeller,GetUsers,GetUserById,GetCartOfUser,GetSellerById
from .views import signup,login,GetProducts,GetBeds,GetTables,Cart

urlpatterns = [
    # path("", include("ecommerce.apps.catalogue.urls", namespace="catalogue")),
    # path("checkout/", include("ecommerce.apps.checkout.urls", namespace="checkout")),
    # path("basket/", include("ecommerce.apps.basket.urls", namespace="basket")),
    # path("account/", include("ecommerce.apps.account.urls", namespace="account")),
    # path("orders/", include("ecommerce.apps.orders.urls", namespace="orders")),

    # html pages
    # path('/',views.home,name='home'),

# products
   path('view_product/<int:id>/',GetProductById.as_view(),name='get-product-by-id'),
  
   
#    seller
   path('view_sellers/',GetSellers.as_view(),name='all-sellers'),
   path('create_seller/',CreateSeller.as_view(),name='create-seller'),
   path('view_products_of_seller/<int:id>',GetProductsOfSeller.as_view(),name='get-products-of-seller'),
   path('view_seller/<int:id>',GetSellerById.as_view(),name='get-seller-by-id'),

# users
   path('view_users/',GetUsers.as_view(),name='all-users'),
  
   path('view_user/<int:id>',GetUserById.as_view(),name='get-user-by-id'),
   path('view_cart/<int:id>',GetCartOfUser.as_view(),name='get-cart-of-user'),



   #routes for seller
   path('signup/',signup,name='seller-sign-up'),
   path('login/',login,name='seller-login'),
   path('create_product/',CreateProduct,name='create-product'),
   # path('login/',login,name='seller-login'),

   #routes for customer
   path('get-products/',GetProducts,name='get-products'),
   path('beds/',GetBeds,name='get-beds'),
   path('tables/',GetTables,name='get-tables'),
   path('cart/',Cart,name='cart'),
   # path('beds/',GetBeds,name='get-beds'),
   



]

