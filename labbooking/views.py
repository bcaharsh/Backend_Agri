from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Booking
from .serializer import Lab_Booking

@api_view(['POST'])
def labbooking(request):
    if request.method == 'POST':
        serializer = Lab_Booking(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'message': 'Lab booking created successfully.', 'data': serializer.data})
        else:
            return Response({'status': 400, 'message': 'Bad Request', 'errors': serializer.errors})
