import json
from django.http import JsonResponse
from django.core.validators import EmailValidator
from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view
from .models import User


class SignUp(APIView):
    def post(self, request):
        user_data = request.data
        first_name = user_data.get("first_name")
        last_name = user_data.get("last_name")
        email: str = user_data.get("email")
        phone_number = user_data.get("phone")
        password = user_data.get("password")
        if not user_data.get("username"):
            username = email.split("@")[0]

        print(first_name,
              last_name,
              email,
              phone_number,
              password)
        from .models import User
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            username=username,
            password=password,
        )
        user.save()
        return Response({"message": "Got some data!", "res": user_data})


@api_view(['GET'])
def validte_email(request):
    email = request.GET.get("email")
    if User.objects.filter(email=email).exists():
        return Response({"message": "email already exists", "valid": False})

    else:
        return Response({"message": "email not exists", "valid": True})


@api_view(['GET'])
def validte_username(request):
    username = request.GET.get("username")
    if User.objects.filter(username=username).exists():
        return Response({"message": "username already exists", "valid": False})
    else:
        return Response({"message": "username not exists", "valid": True})


