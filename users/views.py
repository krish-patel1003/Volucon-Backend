from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.conf import settings
from django.middleware import csrf
from rest_framework import status
from .serializers import RegisterSerializer
from .utils import get_tokens_for_user
# Create your views here.

class RegisterView(APIView):

    serializer_class = RegisterSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, format=None):
        data =  request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"data": serializer.data, "mssg": "user created"}, status=status.HTTP_201_CREATED)
        

class LoginView(APIView):
    authentication_classes = []

    def post(self, request, format=None):
        data = request.data
        response = Response()
        print("data:", data)
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)
        print("user:", user)

        if user is not None:
            if user.is_active:
                data = get_tokens_for_user(user)
                response.set_cookie(
                    key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                    value=data['access'],
                    expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                    secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                    httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                    samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
                )
                csrf.get_token(request)
                response.data = {
                    "Success": " Login Successfully!!", "data": data}
                return response
            else:
                return Response({"No active": "This account is not active"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"Invalid": " Invalid email or password"}, status=status.HTTP_404_NOT_FOUND)
