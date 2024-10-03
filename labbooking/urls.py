from django.urls import path
from . import views

urlpatterns = [
    path('apibooking/',views.labbooking),
]