from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@api_view(['GET'])
def apiget(request):
    crp=CropPreservation.objects.all()
    serializerdata=cropserializer(crp,many=True)
    userdata=User_Registration.objects.all()
    userserializer=User_registration_serializer(userdata,many=True)
    Product=Fertilizer_Product.objects.all()
    productseri=Products_serializer(Product,many=True)
    contact=Contactus.objects.all()
    contactsri=Contactus_serializer(contact,many=True)
    cart=Addtocart.objects.all()
    cartsri=Addcart_serializer(cart,many=True)
    soildata=SoilTesting_Table.objects.all()
    soilsri=Soiltesting_serializer(soildata,many=True)
    seeddata=SeedsInFo.objects.all()
    seedsri=Typeseeds_serializer(seeddata,many=True)
    Govsch=Govermentschem.objects.all()
    Govsri=GovermentSchem_serializer(Govsch,many=True)
    return Response({'message':serializerdata.data,'users':userserializer.data,'product':productseri.data,'contact':contactsri.data,'Addcart':cartsri.data,'SoilData':soilsri.data,'seedinfo':seedsri.data,'GovSch':Govsri.data})

@api_view(['POST'])
def apipost(request):
    serializer=User_registration_serializer(data=request.data)
    if not serializer.is_valid():
        print(serializer.errors)
        return Response({"status":403,"message":"error occured"})
    serializer.save()
    return Response({'status':200,'message':serializer.data})

@api_view(['POST'])
def apicontactpost(request):
    serializer=Contactus_serializer(data=request.data)
    if not (serializer.is_valid()):
        print(serializer.errors)
        return Response({"status":403,"message":"error occured"})
    serializer.save()
    return Response({"message":serializer.data})

@api_view(['POST', 'DELETE'])
def apicartpost(request):
    if request.method == 'POST':
        serializer = Addcart_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": serializer.data})
        else:
            print(serializer.errors)
            return Response({"status": 400, "message": "Error occurred"}, status=400)

    elif request.method == 'DELETE':
        # Assuming you're passing the ID of the cart item to delete in the request data
        cart_item_id = request.data.get('id')
        try:
            cart_item = Addtocart.objects.get(pk=cart_item_id)
        except Addtocart.DoesNotExist:
            return Response({"status": 404, "message": "Cart item not found"}, status=404)

        cart_item.delete()
        return Response({"status": 200, "message": "Cart item deleted successfully"})


@api_view(['POST'])
def apisoilpost(request):
    if request.method == 'POST':
        serializer = Soiltesting_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": serializer.data})
        else:
            print(serializer.errors)
            return Response({"status": 400, "message": "Error occurred"}, status=400)




