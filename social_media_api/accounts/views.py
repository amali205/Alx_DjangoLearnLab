from django.shortcuts import render
from .models import CustomUser 
from .serializers import UserSerializer , RegisterSerializer
from rest_framework import viewsets , generics ,permissions
from rest_framework.views import APIView
from rest_framework.response import Response    
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate , get_user_model
# Create your views here.


User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer



class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer


class loginView(APIView):
   permission_classes = [permissions.AllowAny]   

   def post(self, request):
       username = request.data.get('username')
       password = request.data.get('password')
       user = authenticate(username=username, password=password)
       if user:
           token, created = Token.objects.get_or_create(user=user)
           return Response({'token': token.key})
       else:
           return Response({'error': 'Invalid Credentials'}, status=400)     


class meview(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)