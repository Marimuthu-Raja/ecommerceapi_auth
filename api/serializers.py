
from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework_simplejwt.tokens import RefreshToken
#from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login



class CustomuserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)
    first_name = models.CharField(max_length=255,null=False,blank=False,validators=[RegexValidator('^[a-zA-Z]*$',message='Firstname must be in Character')])
    last_name = models.CharField(max_length=255,null=False,blank=False,validators=[RegexValidator('^[a-zA-Z]*$',message='Lastname must be in Character')])
    verified_email=models.BooleanField(default=False)
    verified_mobile_no =models.BooleanField(default=False)
    mobile_no     =models.BigIntegerField(null=False,blank=False,validators=[RegexValidator(r'^([0-9]{10})$',message='mobile no must have 10 digit')])
    role=         models.CharField(max_length=20,null=False,default='guest',validators=[RegexValidator(r'^[a-zA-Z -.\'\_]+$',message='Role must be in Character')])
    user_role=         models.CharField(max_length=20,null=False,default='guest',validators=[RegexValidator(r'^[a-zA-Z -.\'\_]+$',message='Role must be in Character')])
    is_customer = models.BooleanField(default=True)
    address=models.TextField(null=False,blank=False)


    class Meta:
         model = CustomersProfile
         fields=('email','verified_email','password','first_name','last_name','mobile_no','verified_mobile_no','role','address','is_customer')
         extra_kwargs = {'password': {'write_only': True}}
    
    
    
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        # as long as the fields are the same, we can just use this
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance




    
    
class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model= Products
        fields='__all__'
    

    

    
class CategorySerializers(serializers.ModelSerializer):
   
    class Meta:
        model=Category
        fields='__all__'

class SubCategorySerializers(serializers.ModelSerializer):
    #category=CategorySerializers(many=True)
    class Meta:
        model=Subcategory
        fields='__all__'

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Orders
        fields='__all__'

class OrderTrackingSerializer(serializers.ModelSerializer):
    users=CustomuserSerializers(read_only=True,many=False)
    products=ProductsSerializers(read_only=True,many=False)
    category=CategorySerializers(read_only=True,many=False)
    subcategories=SubCategorySerializers(read_only=True,many=False)
    orders=OrdersSerializer(read_only=True,many=False)


   
    class Meta:
        model=OrderTracking
        fields='__all__'



        
 