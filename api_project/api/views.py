from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
# Create your views here.

class BookList(generics.ListAPIView):
       def get(self , request):
              queryset = Book.objects.all()
              serializer_class = BookSerializer(queryset , many=True)  # لازم امرر له البيانات 
              return Response(serializer_class.data)
       



    #    def get_queryset(self):                         ####    we can use this functions for more actions we need 
    #           return Book.objects.filter()




from rest_framework import viewsets
class BookViewSet(viewsets.ModelViewSet):  # modelviewset use the class directly like this 
              queryset = Book.objects.all()
              serializer_class = BookSerializer
              permission_classes = [IsAuthenticated]