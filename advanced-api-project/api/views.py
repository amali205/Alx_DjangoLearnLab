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





class ListView (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
      


