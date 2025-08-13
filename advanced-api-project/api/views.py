from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer , AuthorSerializer
from .models import Book ,Author
# Create your views here.




class Bookviewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class Authorviewset(viewsets.ModelViewSet):
    queryset =Author.objects.all()
    serializer_class =AuthorSerializer    
