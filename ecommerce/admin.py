from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import *
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
     list_display = (
          'id',
          'title',
          'user'
          
          ,)
class ProductAdmin(admin.ModelAdmin):
     list_display = ('id','productname','price','stockqty','category','owner',)
     search_fields = ['id','productname']  # Fields you want to search
     list_filter = ('category',) 
     
     ordering = ['id', 'price', 'stockqty'] 
     # Default sorting order
 
class CustomerAdmin(admin.ModelAdmin):
     
     list_display = ('id','username','email','telephone',)
     search_fields = ['email','username']  # Fields you want to search
# class OrderDetailAdmin(admin.ModelAdmin):
#      list_display = ('id','created_date','product','qty','amount','method','status')

class Favoriteadmin(admin.ModelAdmin):
     list_display = ('id','user',)
     
     
# class Colorsadmin(admin.ModelAdmin):
#      list_display = ['color','code','price','stockqty','desc']
     


class Coloradmin(admin.ModelAdmin) :
     list_display = ['id','color','code','price','stockqty','desc']     
     
     
class ImageAdmin(admin.ModelAdmin) :
     list_display = ['id','images']          
class OrderAdmin(admin.ModelAdmin) :
     list_display = ['id','customer','ispaid','method','amount','status']  
     search_fields = ['id','customer__username','products__productname']  # Fields you want to search
     list_filter = ('status','method','ispaid',)       
     
class OrderProductDetailAdmin(admin.ModelAdmin) :
     list_display = ['order','product','quantity','size','colorselection']     
     search_fields = ['id']  # Fields you want to search

     


     
     
class SizeAdmin    (admin.ModelAdmin) :
      list_display = ['id','size']   

class  AddressAdmin   (admin.ModelAdmin) :
       list_display = ['customer_id','street','city','country']     


class ReviewAdmin (admin.ModelAdmin) :
       list_display = ['id','rating','product','customer','description']     

     
# class  ReviewAdmin   (admin.ModelAdmin) :
#           pass    
class AttributesAdmin (admin.ModelAdmin)    :
       list_display = ['brand','model','material_name']     
      
     
admin.site.register(Favorite,Favoriteadmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Category)
# admin.site.register(Order)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(OrderDetail,OrderAdmin)
admin.site.register(ReviewRating,ReviewAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Sizes,SizeAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Images,ImageAdmin)
admin.site.register(Attributes,AttributesAdmin)
admin.site.register(Colors,Coloradmin)
admin.site.register(SuperDeal)
admin.site.register(OrderProduct,OrderProductDetailAdmin)
admin.site.register(PasswordResetCodes)






