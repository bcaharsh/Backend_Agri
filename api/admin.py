from django.contrib import admin
from .models import *

class  CropPreservationAdmin(admin.ModelAdmin):
    list_display=['Crop_name','Crop_Temp','Crop_Description','Crop_image']

class  UserRegistrationAdmin(admin.ModelAdmin):
    list_display=['id','Product_name']

class Addtocartadmin(admin.ModelAdmin):
    list_display=['Name','Product_name']

admin.site.register(CropPreservation,CropPreservationAdmin)
admin.site.register(User_Registration)
admin.site.register(Fertilizer_Product,UserRegistrationAdmin)
admin.site.register(Contactus)
# admin.site.register(Addtocart,Addtocartadmin)
# admin.site.register(SoilTesting_Table)
admin.site.register(SeedsInFo)
admin.site.register(Govermentschem)
