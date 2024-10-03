from rest_framework import serializers
from .models import *

class Lab_Booking(serializers.ModelSerializer):
    class Meta:
        model=Booking
        fields='__all__'