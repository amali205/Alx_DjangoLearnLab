from django.shortcuts import render
from rest_framework import viewsets 
from .serializers import BookSerializer , AuthorSerializer
from .models import Book ,Author
from rest_framework import generics
# Create your views here.




class Bookviewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class Authorviewset(viewsets.ModelViewSet):
    queryset =Author.objects.all()
    serializer_class =AuthorSerializer    





class Bookgenrics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_create(self, serializer):
      serializer.save()

 
class Bookgenricsupdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def perform_update(self, serializer):
       serializer.save()  
      


