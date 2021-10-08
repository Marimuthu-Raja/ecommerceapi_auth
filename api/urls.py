from django.urls import path,include
from .views import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.views import TokenRefreshView

from rest_framework_simplejwt.views import TokenObtainPairView

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

    
   
    

  # path('clientadmincreate/', CustomUserCreate.as_view(), name="create_user"),
   # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

      # from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
# )
#from auth.views import MyObtainTokenPairView
#from  rest_framework.authtoken import views

    # # path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    

]