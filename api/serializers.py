from rest_framework import serializers
from .models import *

class cropserializer(serializers.ModelSerializer):
    class Meta:
        model=CropPreservation
        fields='__all__'

class User_registration_serializer(serializers.ModelSerializer):
    class Meta:
        model=User_Registration
        fields='__all__'

class Products_serializer(serializers.ModelSerializer):
    class Meta:
        model=Fertilizer_Product
        fields='__all__'

class Contactus_serializer(serializers.ModelSerializer):
    class Meta:
        model=Contactus
        fields='__all__'

class Addcart_serializer(serializers.ModelSerializer):
    # product_details = serializers.SerializerMethodField()

    class Meta:
        model = Addtocart
        fields ='__all__' 

    # def get_product_details(self, obj):
    #     product = obj.Product_name
    #     serializer = Products_serializer(product, context=self.context)
    #     return serializer.data

class Soiltesting_serializer(serializers.ModelSerializer):
    class Meta:
        model = SoilTesting_Table
        fields = '__all__'
        
class Typeseeds_serializer(serializers.ModelSerializer):
    class Meta:
        model=SeedsInFo
        fields="__all__"    

class GovermentSchem_serializer(serializers.ModelSerializer):
    class Meta:
        model=Govermentschem
        fields="__all__"