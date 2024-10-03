from django.urls import path
from . import views

urlpatterns = [
    path("order/create/",views.CreateOrderAPIView.as_view()),
    path("order/complete/",views.TransactionAPIView.as_view())
]