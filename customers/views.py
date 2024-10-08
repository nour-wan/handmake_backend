from django.shortcuts import render
from.serializer import CustomerSignupSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Customer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import make_password
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import generics ,permissions
from users.serializer import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from users.permissions import IsCustomerUser

# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class=CustomerSignupSerializer
    def post( self, request , *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        customer = Customer.objects.get(user=user)
        response_data = {
            "user_id": user.id,
            "admin_id": customer.id,
            "username": user.username,
            "email": user.email,
            "name": customer.name,
            "phone_number": customer.phone_number,
        }
        return Response({
            "user" : response_data,
            "token": Token.objects.get(user=user).key,
            "message":"account created successfully"
        },status=status.HTTP_200_OK)
    



class LoginView(ObtainAuthToken):
    def post( self, request , *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request} )
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_data['user']
        customer = Customer.objects.get(user=user)
        token, create=Token.objects.get_or_create(user=user)
        response_data = {
            "user_id": user.id,
            "admin_id": customer.id,
            "username": user.username,
            "email": user.email,
            "name": customer.name,
            "phone_number": customer.phone_number,
        }
        return Response({
            "user" : response_data,
            "token": token.key,
            "message":"login successfully"
        },status=status.HTTP_200_OK)
    
    
class LogoutView(APIView):
    def post(self, request , format=None):
        request.auth.delete()
        response_data = {
            "user_id":"" ,
            "admin_id": "",
            "username": "",
            "email":"" ,
            "name": "",
            "phone_number":"" ,
        }
        return Response({
            "user" : response_data,
            "token": "",
            "message":"account logout successfully"
        },status=status.HTTP_200_OK)
    
 

