import random

from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from . models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = User
      fields = ['username', 'email']
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'
   
class ImageSerializerEdit(serializers.ModelSerializer):
      
      class Meta:
       model = Images
       
       fields = [ 'id']

# class CategorySerializerV2(serializers.ModelSerializer):
#    imgid = ImageSerializer(many=False)
#    class Meta:
#       model = Category
#       fields = ['id', 'categoryname','imgid']
class CategorySerializerV2(serializers.ModelSerializer):
    imgid = ImageSerializer(many=False)

    class Meta:
        model = Category
        fields = ['id', 'categoryname', 'imgid']

    def create(self, validated_data):
        # Extract the nested imgid data
        imgid_data = validated_data.pop('imgid', None)

        # Create the Category instance
        category = Category.objects.create(**validated_data)

        # Create the Image instance if imgid_data is present
        if imgid_data:
            imgid_instance = Images.objects.create(**imgid_data)
            category.imgid = imgid_instance  # Assuming a ForeignKey relationship
            category.save()

        return category
      
class ColorSerialzer(serializers.ModelSerializer) :
  imgid = ImageSerializer(many=False,read_only=True)
  class Meta:
    model = Colors
    fields= '__all__'      
    
    
class SizeSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Sizes
    fields= '__all__'   
        
class AttributesSerialzer(serializers.ModelSerializer) :
  colorid = ColorSerialzer(many= True)
  size = SizeSerializer(many=True)
  class Meta:
    model = Attributes
    fields= '__all__'      
class ProductSerializerV2(serializers.ModelSerializer):
    category =  CategorySerializerV2(many=False,read_only=False)
    owner = UserSerializer(many=False)
    imgid = ImageSerializer(many=True)
    attribution = AttributesSerialzer(many=False)
    class Meta:
      model = Product
      fields ='__all__'


class MessageSerializer(serializers.ModelSerializer):
  user = UserSerializer(many=False,read_only=True)
  class Meta:
    model = Message
    fields ='__all__'
class ProductSerializer(serializers.ModelSerializer):
    attribution = serializers.PrimaryKeyRelatedField(many=False, queryset=Attributes.objects.all())
    imgid = serializers.PrimaryKeyRelatedField(many=True, queryset=Images.objects.all())
    colorid = serializers.PrimaryKeyRelatedField(many=True, queryset=Colors.objects.all(), source='attribution.colorid')
    size = serializers.PrimaryKeyRelatedField(many=True, queryset=Sizes.objects.all(), source='attribution.size')
    # attribution = AttributesSerialzer(many=False)
    # imgid = ImageSerializer(many=True)
    class Meta:
      model = Product
      fields ='__all__'


class CategorySerializer(serializers.ModelSerializer):
  
   product =  ProductSerializerV2(many=True,read_only=True)
  
   imgid = ImageSerializer(many=False)

   class Meta:
      model = Category
      # fields = ['id', 'categoryname','product','imgid']
      fields = '__all__'

class OrderProductSerializer(serializers.ModelSerializer):
    
    product = ProductSerializerV2()
    size = SizeSerializer(many=False)
    colorselection  = ColorSerialzer(many=False)
    imageproduct = ImageSerializer(many=False)
    # product_id = serializers.IntegerField(write_only=True)



    class Meta:
        model = OrderProduct
        fields = ['product', 'quantity','colorselection','imageproduct','size']



# class OrderSerializer(serializers.ModelSerializer):
#    class Meta:
#       model =Order
#       fields = '__all__'
class CustomerSerializerResetPassword(serializers.ModelSerializer):
  class Meta:
      model =Customer
      fields = ['email']
      
class SuperDealSerializer(serializers.ModelSerializer) :
  product = ProductSerializerV2(many=True)
  imgid = ImageSerializer(many=False)
  class Meta:
    model = SuperDeal
    fields='__all__'

class CustomerSerializerLogin(serializers.ModelSerializer):
  
  class Meta:
      model =Customer
      fields = ['id','email','password']

class PasswordResetCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PasswordResetCodes
        fields = ['user', 'code']
        
class CustomerSerializerV2(serializers.ModelSerializer):
  class Meta:
      model =Customer
      fields = ('username','email','password','telephone')
class CustomerSerializerV3(serializers.ModelSerializer):
  class Meta:
      model =Customer
      fields = ('email',)
      
      
      
class CustomerSerializerGoogle(serializers.ModelSerializer):
   imgid = ImageSerializer(many=False,read_only=True)
   
   class Meta:
      model =Customer
      # read_only_fields = ('password',)

      fields = ['id','email','telephone','gender','imgid','username','password','created_date'] 
      
            
class CustomerSerializerV2(serializers.ModelSerializer):
   imgid = ImageSerializer(many=False,read_only=True)
   
   class Meta:
      model =Customer
      # read_only_fields = ('password',)

      fields = ['id','firstname','lastname','email','telephone','gender','imgid','username','created_date']


class CustomerSerializer(serializers.ModelSerializer):
    # Remove the ImageSerializer relationship here since we don't need it for creation
    class Meta:
        model = Customer
        fields = ['id', 'firstname', 'lastname', 'email', 'telephone', 'gender', 'password', 'username']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Hash password and create customer without any image
        password = make_password(validated_data.pop('password'))
        customer = Customer.objects.create(
            password=password,
            **validated_data
        )
        return customer

 
 
 

     
 
 
class AddressSerializer(serializers.ModelSerializer):
   customer_id  = CustomerSerializer(many=False,read_only= True)
   class Meta:
      model =Address
      fields = '__all__'
class OrderDetailSerializer(serializers.ModelSerializer):
   address = AddressSerializer(many=False,read_only=True) 
   products = OrderProductSerializer(source='orderproduct_set', many=True,read_only=True)

   class Meta:
      model =OrderDetail

      read_only_fields = ('amount','address')

      fields = '__all__'

class CustomerSerializerId(serializers.ModelSerializer):

   class Meta:
      model =Customer
      fields = ['id','isowner']    
class CustomerSerializerEdit(serializers.ModelSerializer):
  #  imgid=ImageSerializer(many=False)
  #  imgid = serializers.PrimaryKeyRelatedField(many=False )
   class Meta:
     model = Customer
     fields =('username','firstname','lastname','telephone','gender','imgid')
class CustomerSerializerReview(serializers.ModelSerializer):
   imgid=ImageSerializer(many=False)

   class Meta:
     model = Customer
     fields =('username','firstname','lastname','telephone','gender','imgid')  
class OrderDetailStatusSerializer(serializers.ModelSerializer):

    
    class Meta:

      model =OrderDetail

      read_only_fields = ('customer','method','qty','amount','product',)

      fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
  
  
    customer = CustomerSerializerReview(many=False,read_only=True)
    product = ProductSerializer(many=False,read_only=True)
    class Meta:
      model = ReviewRating
      fields ='__all__'
      read_only_fields = ('avg_rating',)
      
class FavoriteSerializer(serializers.ModelSerializer):
   products = ProductSerializerV2(many=True,read_only=True)
   class Meta:
     model = Favorite
     fields ='__all__'