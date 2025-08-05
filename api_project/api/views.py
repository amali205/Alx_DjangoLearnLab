from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book
from rest_framework.response import Response
# Create your views here.

class BookList(generics.ListAPIView):
       def get(self , request):
              queryset = Book.objects.all()
              serializer_class = BookSerializer()
              return Response(serializer_class.data)
       



    #    def get_queryset(self):                         ####    we can use this functions for more actions we need 
    #           return Book.objects.filter()