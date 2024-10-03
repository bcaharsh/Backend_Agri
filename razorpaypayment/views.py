from django.shortcuts import render
from rest_framework import status
from  rest_framework.response import Response
from .serializer import CreateOrderSerializer,TransactionModelSerailizer
from rest_framework.views import APIView
from .main import RazorpayClient

rz_client=RazorpayClient()

class CreateOrderAPIView(APIView):
    def post(self,request):
        create_order_seralizer=CreateOrderSerializer(data=request.data)
        if create_order_seralizer.is_valid():
            order_response=rz_client.create_order(
                amount=create_order_seralizer.validated_data.get("amount"),
                currency=create_order_seralizer.validated_data.get("currency")
            )
            response={
                "status_code":status.HTTP_201_CREATED,
                "message":"order Created",
                "data":order_response
            }
            return Response(response,status=status.HTTP_201_CREATED)
        else:
            response={
                "status_code":status.HTTP_400_BAD_REQUEST,
                "message":"bad request",
                "error":create_order_seralizer.errors
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        

class TransactionAPIView(APIView):
    def post(self,request):
        transaction_serializer=TransactionModelSerailizer( data= request.data )
        if  transaction_serializer.is_valid():
            rz_client.varify_payment(
                razorpay_order_id=transaction_serializer.validated_data.get("order_id"),
                razorpay_payment_id=transaction_serializer.validated_data.get("payment_id"),
                razorpay_signature=transaction_serializer.validated_data.get("signature")
            )
            transaction_serializer.save()
            response={
                "status_code":status.HTTP_201_CREATED,
                "message":"order Created",
            }
            return Response(response,status=status.HTTP_201_CREATED)
        else:
            response={
                "status_code":status.HTTP_400_BAD_REQUEST,
                "message":"bad request",
                "error":transaction_serializer.errors
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

