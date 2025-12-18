from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password

@api_view(['POST'])
def register(request):
    data = request.data
    data['password'] = make_password(data['password'])
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered"})
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login(request):
    try:
        user = User.objects.get(username=request.data['username'])
        if check_password(request.data['password'], user.password):
            return Response({"message": "Login successful"})
        return Response({"error": "Invalid password"}, status=401)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
