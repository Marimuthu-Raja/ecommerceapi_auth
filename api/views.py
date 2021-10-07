from django.shortcuts import render
#from django.contrib.auth.models import User
from django.contrib.auth.models import *
from django.contrib.auth import login

#from rest_framework import permissions

from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import permission_classes
from django.contrib.auth.hashers import make_password

from django.contrib.auth import login

from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated,AllowAny
#from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

from rest_framework.authentication import TokenAuthentication,SessionAuthentication,BasicAuthentication

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.http import HttpResponse

from rest_framework_simplejwt.views import TokenObtainPairView



    

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        print(request)
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
class CustomerProfileAPIVIEW(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    serializer_class = CustomuserSerializers
    queryset = CustomersProfile.objects.all()
    permission_classes=[AllowAny]
    #authentication_classes=[TokenAuthentication]

    lookup_field ='user_id'

    def get(self, request , user_id = None):
        if user_id:
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)

    def put(self, request, user_id=None):
        return self.update(request, user_id)
    
    # def patch(self, request, user_ptr_id=None):
    #     return self.partial_update(request, user_ptr_id)
    
    def delete(self, request, user_id):
        return self.destroy(request, user_id)


# Create your views here.

# class UsersAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
#     queryset = Users.objects.all()
   
#     serializer_class = UsersSerializers
    
#     lookup_field = 'user_id'
#     permission_classes=[IsAuthenticated]
#     authentication_classes=[TokenAuthentication]
#     #@permission_classes(IsAuthenticated)
#     def get(sef, request, user_id = None):
#         user=request.user
#         print(user)
        
#         if user_id:
#             return sef.retrieve(request)
#         else:
#             return sef.list(request)
        
        




      
#     def post(self, request ):
#             return self.create(request)
        
          
#     def put(self, request, user_id=None):
#          return self.update(request, user_id)
    
#     def delete(self, request, user_id):
#              return self.destroy(request, user_id)


class ProductsAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Products.objects.all()
    serializer_class =ProductsSerializers

   
    # permission_classes=[IsAuthenticated]
    # authentication_classes=[TokenAuthentication]
   
    

    lookup_field = 'product_id'
       
    def get(sef, request, product_id = None):
        if product_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
   # @permission_classes([AllowAny])      
    def post(self, request):
              return self.create(request)
    
    def put(self, request, product_id=None):
             return self.update(request, product_id)
    
    def delete(self, request, product_id):
             return self.destroy(request, product_id)

class CategoryAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class =CategorySerializers

    lookup_field = 'category_id'
    permission_classes=[IsAuthenticated]
    
    def get(sef, request, category_id = None):

        user = request.user
        print(user.role)
        if user.role != 'admin':
            response = {
                'success': False,
                'status_code': status.HTTP_403_FORBIDDEN,
                'message': 'You are not authorized to perform this action'
            }
            
            return Response(response, status.HTTP_403_FORBIDDEN)
        if category_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
    
    def post(self, request):
        
        return self.create(request)
    
    def put(self, request, category_id=None):
             return self.update(request, category_id)
    
    def delete(self, request, category_id):
             return self.destroy(request, category_id)

class SubCategoryAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Subcategory.objects.all()
    serializer_class =SubCategorySerializers

    lookup_field = 'subcat_id'

    def get(sef, request, subcat_id = None):
        if subcat_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
    
    def post(self, request):
              return self.create(request)
    
    def put(self, request, subcat_id=None):
             return self.update(request, subcat_id)
    
    def delete(self, request, subcat_id):
             return self.destroy(request, subcat_id)



class OrdersAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = Orders.objects.all()
    serializer_class =OrdersSerializer

    lookup_field = 'order_id'
    #permission_classes=[AllowAny]


    def get(sef, request, order_id = None):
        if order_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
    
    def post(self, request):
              return self.create(request)
    
    def put(self, request, order_id=None):
             return self.update(request, order_id)
    
    def delete(self, request, order_id):
             return self.destroy(request, order_id)


class OrderTrackingAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    queryset = OrderTracking.objects.all()
    serializer_class =OrderTrackingSerializer

    lookup_field = 'tracking_id'

    def get(sef, request, tracking_id = None):
        if tracking_id:
            return sef.retrieve(request)
        else:
            return sef.list(request)
    
    def post(self, request):
              return self.create(request)
    
    def put(self, request, tracking_id=None):
             return self.update(request, tracking_id)
    
    def delete(self, request, tracking_id):
             return self.destroy(request, tracking_id)


#def login(request):
    #     print(request)
    #     username = request.data.get("username")
    #     password = request.data.get("password")
    #     if username is None or password is None:
    #      return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
        
    #     user = authenticate(username=username, password=password)
    #     print("hi")
    #     print(user)

    #     if not user:
    #      return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
    #     token, _ = Token.objects.get_or_create(user=user)
    #     return Response({'token': token.key}, status=HTTP_200_OK)
# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
#     username = request.data.get("username")
#     password = request.data.get("password")
#     if username is None or password is None:
#         return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
#     user = authenticate(username=username, password=password)


#     if not user:
#         return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
#     token, _ = Token.objects.get_or_create(user=user)
#     return Response({'token': token.key}, status=HTTP_200_OK)

# class CustomUserCreate(APIView):
#     permission_classes = [AllowAny]
#     serializer =  LoginSerializers
#     # def post(self, request ):
#     #         return self.create(request)

#     def post(self, request, format='json'):
#         serializer =  LoginSerializers(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 json = serializer.data
#                 return Response(json, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#pwd:nivi123

#  def post(self,request):
#         serializer = LoginSerializers(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             if user:
#                 json = serializer.data
#                 return Response(json, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

        # role=request.role
        # print(role)
        # if Users.role!=user:
        #     return Response({"response":"you don't have a permission to edit that"})
        
    # def login(self,request):
    #   username = request.data.get("email")
    #   password = request.data.get("password")

    #   if username is None or password is None:
    #      return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
        # class MyTokenObtainPairView(TokenObtainPairView):
#     serializer_class = MyTokenObtainPairSerializer
          
    

# class MyObtainTokenPairView(TokenObtainPairView):
#         permission_classes = (AllowAny,)
#         serializer_class = MyTokenObtainPairSerializer


# class LoginAPI(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin):
#     queryset = Customers.objects.all()
   
#     serializer_class = LoginSerializers
#     permission_classes=[AllowAny]
#     authentication_classes=[TokenAuthentication]
#     lookup_field = 'user_id'
    
  
#     def post(self,request):
#         data=request.data
#         print(data)
#         return self.create(request)
   
    
   
#     def perform_create(self, serializer):
#         if ('password' in self.request.data):
#             password = make_password(self.request.data['password'])
#             print(password)
#             serializer.save(password=password)
#         else:
#             serializer.save()
    
    
#     def get(sef, request, user_id = None):
#         user=request.user
      
#         print(user)
#         print(user_id)
      
#         if user_id:
#             return sef.retrieve(request)
#         else:
#             return sef.list(request)
