from .models import CustomUser
from rest_framework import serializers  
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

user = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['__all__']




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
       
       
        user = user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        Token.objects.create(user=user)  # Create a token for the new user
        return user        