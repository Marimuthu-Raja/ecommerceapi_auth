from django.urls import path,include
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    
    path('get-token/', CustomAuthToken.as_view()),
    
   
    path('customer/', CustomerProfileAPIVIEW.as_view()),
    path('customer/<int:user_id>/', CustomerProfileAPIVIEW.as_view()),

    path('products/',ProductsAPI.as_view()),
    path('products/<int:product_id>/', ProductsAPI.as_view()),

    path('category/',CategoryAPI.as_view()),
    path('category/<int:category_id>/',CategoryAPI.as_view()),

    path('subcategory/',SubCategoryAPI.as_view()),
    path('subcategory/<int:subcat_id>/',SubCategoryAPI.as_view()),
   
    path('orders/',OrdersAPI.as_view()),
    path('orders/<int:order_id>/',OrdersAPI.as_view()),

    path('ordertracking/',OrderTrackingAPI.as_view()),
    path('ordertracking/<int:tracking_id>/',OrderTrackingAPI.as_view()),

    
   
    

 
    

]