from django.db import models

class CropPreservation(models.Model):
    Crop_name=models.CharField(max_length=200)
    Crop_Temp=models.CharField(null=True,blank=True)
    Crop_Description=models.TextField()
    Crop_image=models.ImageField(null=True,default=None)

class User_Registration(models.Model):
    Name=models.CharField(max_length=30)
    Phone_Number=models.CharField(max_length=10)
    Email=models.EmailField(unique=True)
    Password=models.CharField(max_length=16)
    
    def __str__(self):
        return self.Name 
    
class Fertilizer_Product(models.Model):
    Product_name=models.CharField(max_length=100)
    Description=models.TextField(max_length=120)
    Price=models.IntegerField(default=0)
    Product_image=models.ImageField(null=True,default=None)

    def __str__(self):
        return self.Product_name
    
class Contactus(models.Model):
    Name=models.CharField(max_length=50)
    PhoneNumber=models.CharField(max_length=10)
    message=models.TextField()

class Addtocart(models.Model):
    Name=models.ForeignKey(User_Registration,on_delete=models.CASCADE)
    Product_name=models.ForeignKey(Fertilizer_Product,on_delete=models.CASCADE)

class SoilTesting_Table(models.Model):
    Name=models.ForeignKey(User_Registration,on_delete=models.CASCADE)
    Laboratory_Number=models.CharField(max_length=100)
    Farmer_Name=models.CharField(max_length=100)
    Village=models.CharField(max_length=100)
    Survey_Number=models.CharField(max_length=100)
    Taluka_District=models.CharField(max_length=100)
    P_H_Number_Proporstion=models.CharField(max_length=100,default='Null')
    Electrical_Conductivity_Proporstion=models.CharField(max_length=100,default='Null')
    Organic_carbon_Proporstion=models.CharField(max_length=100,default='Null')
    Avalaible_PhosPhorus_Proporstion=models.CharField(max_length=100,default='Null')
    Avalaible_Potas_Proporstion=models.CharField(max_length=100,default='Null')
    P_H_Number_Quality=models.CharField(max_length=100,default='Null')
    Electrical_Conductivity_Quality=models.CharField(max_length=100,default='Null')
    Organic_carbon_Quality=models.CharField(max_length=100,default='Null')
    Avalaible_PhosPhorus_Quality=models.CharField(max_length=100,default='Null')
    Avalaible_Potas_Quality=models.CharField(max_length=100,default='Null')
    Zinc_Analysis=models.CharField(max_length=100,default='Null')
    Cooper_Analysis=models.CharField(max_length=100,default='Null')
    Magananese_Analysis=models.CharField(max_length=100,default='Null')
    Brimstone_Analysis=models.CharField(max_length=100,default='Null')
    Boron_Analysis=models.CharField(max_length=100,default='Null')
    Lime_Analysis=models.CharField(max_length=100,default='Null')
    Gypsum_Analysis=models.CharField(max_length=100,default='Null')
    Zinc_Quality=models.CharField(max_length=100,default='Null')
    Cooper_Quality=models.CharField(max_length=100,default='Null')
    Magananese_Quality=models.CharField(max_length=100,default='Null')
    Brimstone_Quality=models.CharField(max_length=100,default='Null')
    Boron_Quality=models.CharField(max_length=100,default='Null')
    Lime_Quality=models.CharField(max_length=100,default='Null')
    Gypsum_Quality=models.CharField(max_length=100,default='Null')
    
class SeedsInFo(models.Model):
    seed={
        
        'Grains seeds':'Grains seeds',
        'Pulses seeds':'Pulses seeds',
        'Oilseeds seeds':'Oilseeds seeds',
        'Vegetables seeds':'Vegetables seeds',
        'Spices seeds':'Spices  seeds'
            }
    Seed_Name=models.CharField(max_length=100)
    Seed_Description=models.TextField(max_length=300)
    Seed_Type=models.CharField(choices=seed,default='null')
    Seed_image=models.ImageField(null=True,default=None)

class Govermentschem(models.Model):
    Title=models.CharField(max_length=100)
    Description=models.TextField(max_length=150,null=True,default=None)
    Link=models.CharField(max_length=250)
    Publish_Date=models.DateField()


                                   


