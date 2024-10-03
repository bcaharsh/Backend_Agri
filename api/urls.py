from django.urls import path
from . import views

urlpatterns = [
    path('apiget/',views.apiget),
    path('apipost/',views.apipost),
    path('apicontact/',views.apicontactpost),
    path('apicart/',views.apicartpost),
    path('apisoil/',views.apisoilpost)
]